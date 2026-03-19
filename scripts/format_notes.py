#!/usr/bin/env python3
"""
format_notes.py - Convert raw, unstructured notes into standardized Markdown.

This script takes messy drafts, meeting notes, or student logs and reformats
them into structured Markdown following the portal's style guide. It handles:
- Adding metadata headers (title, author, date, category)
- Converting headings to proper Markdown hierarchy
- Wrapping code snippets in fenced code blocks
- Normalizing lists into consistent Markdown format
- Inserting admonition blocks for notes/warnings
- Adding a standard footer

Usage:
    # Single file
    python format_notes.py --input raw_notes.txt --output docs/how-to/my-guide.md

    # Batch processing
    python format_notes.py --input-dir drafts/ --output-dir docs/tutorials/

    # With options
    python format_notes.py --input notes.txt --output guide.md --author "Arshad Naguru" --category tutorial --verbose
"""

import argparse
import re
import os
import sys
from datetime import datetime
from pathlib import Path


# ──────────────────────────────────────────────
# Configuration
# ──────────────────────────────────────────────
VALID_CATEGORIES = ["tutorial", "how-to", "reference", "explanation"]

CODE_INDICATORS = [
    r"^\$\s",           # Lines starting with $
    r"^>\s",            # Lines starting with >
    r"^\s{4,}",         # Lines indented 4+ spaces
    r"^(docker|git|pip|python|npm|curl|cd|mkdir|ls|cat|sudo|chmod)\s",
]

NOTE_KEYWORDS = {
    "NOTE": "note",
    "TIP": "tip",
    "WARNING": "warning",
    "WARN": "warning",
    "DANGER": "danger",
    "IMPORTANT": "warning",
    "CAUTION": "warning",
}

LANGUAGE_HINTS = {
    "python": ["import ", "def ", "class ", "print(", "pip install"],
    "bash": ["docker ", "git ", "cd ", "mkdir ", "sudo ", "curl ", "npm ", "pip "],
    "sql": ["SELECT ", "INSERT ", "UPDATE ", "DELETE ", "CREATE TABLE", "ALTER "],
    "yaml": ["version:", "services:", "image:", "ports:"],
    "json": ["{", '{"'],
    "javascript": ["const ", "let ", "var ", "function ", "console.log"],
}


# ──────────────────────────────────────────────
# Core Formatting Functions
# ──────────────────────────────────────────────
def generate_metadata_header(title: str, author: str, category: str) -> str:
    """Generate a standard metadata header for the document."""
    date_str = datetime.now().strftime("%B %Y")
    category_display = category.replace("-", " ").title()
    header = f"# {title}\n\n"
    header += f"> **Author:** {author} · **Last Updated:** {date_str} · **Category:** {category_display}\n\n"
    return header


def detect_language(line: str) -> str:
    """Attempt to detect the programming language of a code line."""
    for lang, indicators in LANGUAGE_HINTS.items():
        for indicator in indicators:
            if indicator in line:
                return lang
    return "bash"  # default to bash for command-like content


def is_code_line(line: str) -> bool:
    """Check if a line looks like code or a command."""
    for pattern in CODE_INDICATORS:
        if re.match(pattern, line):
            return True
    return False


def normalize_heading(line: str) -> str:
    """Convert various heading formats to Markdown headings."""
    stripped = line.strip()

    # Already a Markdown heading
    if stripped.startswith("#"):
        return stripped

    # ALL CAPS lines (likely headings)
    if stripped.isupper() and len(stripped.split()) <= 8 and len(stripped) > 3:
        return f"## {stripped.title()}"

    # Lines ending with colon (often section headers)
    if stripped.endswith(":") and len(stripped.split()) <= 6 and not is_code_line(stripped):
        return f"## {stripped.rstrip(':')}"

    return None  # Not a heading


def normalize_list_item(line: str) -> str:
    """Convert various list formats to standard Markdown lists."""
    stripped = line.strip()

    # Convert * and + bullets to -
    if re.match(r"^[*+]\s", stripped):
        return f"- {stripped[2:]}"

    # Handle numbered lists with various formats (1), 1., 1:
    match = re.match(r"^(\d+)[.):\]]\s*(.*)", stripped)
    if match:
        return f"{match.group(1)}. {match.group(2)}"

    return None  # Not a list item


def convert_note_to_admonition(line: str) -> str:
    """Convert NOTE/TIP/WARNING markers into MkDocs admonitions."""
    stripped = line.strip()
    for keyword, admonition_type in NOTE_KEYWORDS.items():
        patterns = [
            rf"^{keyword}:\s*(.*)",
            rf"^{keyword}\s*-\s*(.*)",
            rf"^\[{keyword}\]\s*(.*)",
        ]
        for pattern in patterns:
            match = re.match(pattern, stripped, re.IGNORECASE)
            if match:
                content = match.group(1).strip()
                return f'\n!!! {admonition_type}\n    {content}\n'
    return None


def generate_footer(author: str) -> str:
    """Generate a standard document footer."""
    date_str = datetime.now().strftime("%B %Y")
    return f"\n---\n\n*Last updated: {date_str} · Author: {author}*\n"


# ──────────────────────────────────────────────
# Main Processing
# ──────────────────────────────────────────────
def format_document(raw_text: str, title: str, author: str, category: str, verbose: bool = False) -> str:
    """
    Process raw text and convert it into structured Markdown.

    Args:
        raw_text: The raw, unformatted input text
        title: Document title
        author: Author name
        category: Diátaxis category (tutorial, how-to, reference, explanation)
        verbose: Print transformation details

    Returns:
        Formatted Markdown string
    """
    lines = raw_text.split("\n")
    output_lines = []
    in_code_block = False
    code_buffer = []
    code_language = "bash"

    # Add metadata header
    output_lines.append(generate_metadata_header(title, author, category))

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Skip empty lines (preserve them in output)
        if not stripped:
            if in_code_block:
                code_buffer.append("")
            else:
                output_lines.append("")
            continue

        # Handle code blocks
        if is_code_line(stripped) and not in_code_block:
            in_code_block = True
            code_language = detect_language(stripped)
            # Clean the line (remove leading $ or >)
            clean_line = re.sub(r"^[$>]\s*", "", stripped)
            code_buffer.append(clean_line)
            if verbose:
                print(f"  [CODE] Detected code block ({code_language}): {stripped[:50]}...")
            continue

        if in_code_block and not is_code_line(stripped):
            # Close the code block
            output_lines.append(f"```{code_language}")
            output_lines.extend(code_buffer)
            output_lines.append("```\n")
            code_buffer = []
            in_code_block = False

        if in_code_block:
            clean_line = re.sub(r"^[$>]\s*", "", stripped)
            code_buffer.append(clean_line)
            continue

        # Check for admonitions (NOTE, WARNING, etc.)
        admonition = convert_note_to_admonition(stripped)
        if admonition:
            output_lines.append(admonition)
            if verbose:
                print(f"  [ADMONITION] Converted: {stripped[:50]}...")
            continue

        # Check for headings
        heading = normalize_heading(stripped)
        if heading:
            output_lines.append(f"\n{heading}\n")
            if verbose:
                print(f"  [HEADING] Converted: {stripped} → {heading}")
            continue

        # Check for list items
        list_item = normalize_list_item(stripped)
        if list_item:
            output_lines.append(list_item)
            continue

        # Regular paragraph text
        output_lines.append(stripped)

    # Close any remaining code block
    if in_code_block and code_buffer:
        output_lines.append(f"```{code_language}")
        output_lines.extend(code_buffer)
        output_lines.append("```\n")

    # Add footer
    output_lines.append(generate_footer(author))

    return "\n".join(output_lines)


def extract_title_from_text(text: str) -> str:
    """Try to extract a title from the first non-empty line of text."""
    for line in text.split("\n"):
        stripped = line.strip()
        if stripped:
            # Remove Markdown heading markers
            clean = re.sub(r"^#+\s*", "", stripped)
            return clean.title()
    return "Untitled Document"


def process_file(input_path: str, output_path: str, author: str, category: str, verbose: bool = False):
    """Process a single file."""
    with open(input_path, "r", encoding="utf-8") as f:
        raw_text = f.read()

    title = extract_title_from_text(raw_text)
    formatted = format_document(raw_text, title, author, category, verbose)

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(formatted)

    if verbose:
        print(f"\n  ✓ Formatted: {input_path} → {output_path}")


def process_directory(input_dir: str, output_dir: str, author: str, category: str, verbose: bool = False):
    """Process all .txt and .md files in a directory."""
    input_path = Path(input_dir)
    output_path = Path(output_dir)

    files = list(input_path.glob("*.txt")) + list(input_path.glob("*.md"))

    if not files:
        print(f"No .txt or .md files found in {input_dir}")
        return

    print(f"Processing {len(files)} files from {input_dir}...\n")

    for file in files:
        out_name = file.stem.replace(" ", "-").replace("_", "-").lower() + ".md"
        out_file = output_path / out_name
        process_file(str(file), str(out_file), author, category, verbose)

    print(f"\n✓ Processed {len(files)} files → {output_dir}")


# ──────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        description="Convert raw notes into structured Markdown documentation.",
        epilog="Example: python format_notes.py --input notes.txt --output docs/how-to/guide.md",
    )
    parser.add_argument("--input", "-i", help="Path to a single input file")
    parser.add_argument("--output", "-o", help="Path for the output Markdown file")
    parser.add_argument("--input-dir", help="Directory of files to batch process")
    parser.add_argument("--output-dir", help="Output directory for batch processing")
    parser.add_argument("--author", "-a", default="Arshad Naguru", help="Author name for metadata")
    parser.add_argument(
        "--category", "-c",
        default="how-to",
        choices=VALID_CATEGORIES,
        help="Diátaxis category (default: how-to)",
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="Print transformation details")

    args = parser.parse_args()

    if args.input and args.output:
        process_file(args.input, args.output, args.author, args.category, args.verbose)
    elif args.input_dir and args.output_dir:
        process_directory(args.input_dir, args.output_dir, args.author, args.category, args.verbose)
    else:
        parser.error("Provide either --input/--output for a single file, or --input-dir/--output-dir for batch processing.")


if __name__ == "__main__":
    main()
