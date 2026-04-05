#!/usr/bin/env python3
"""
format_notes.py - Convert raw, unstructured notes into standardized Markdown.

Usage:
    python format_notes.py --input raw_notes.txt --output docs/how-to/my-guide.md
    python format_notes.py --input-dir drafts/ --output-dir docs/tutorials/
    python format_notes.py --input notes.txt --output guide.md --category tutorial --verbose
"""

import argparse
import re
import os
from datetime import datetime
from pathlib import Path


VALID_CATEGORIES = ["tutorial", "how-to", "reference", "explanation"]

CODE_INDICATORS = [
    r"^\$\s",
    r"^\s{4,}",
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
    "sql": ["SELECT ", "INSERT ", "UPDATE ", "DELETE ", "CREATE TABLE"],
    "yaml": ["version:", "services:", "image:", "ports:"],
    "javascript": ["const ", "let ", "var ", "function ", "console.log"],
}

SECTION_KEYWORDS = [
    "steps", "requirements", "prerequisites", "troubleshooting",
    "overview", "setup", "installation", "usage", "notes",
    "procedure", "checklist", "output", "configuration"
]


def generate_metadata_header(title: str, author: str, category: str) -> str:
    date_str = datetime.now().strftime("%B %Y")
    category_display = category.replace("-", " ").title()
    header = f"# {title}\n\n"
    header += f"> **Author:** {author} · **Last Updated:** {date_str} · **Category:** {category_display}\n\n"
    return header


def detect_language(line: str) -> str:
    for lang, indicators in LANGUAGE_HINTS.items():
        for indicator in indicators:
            if indicator in line:
                return lang
    return "bash"


def is_code_line(line: str) -> bool:
    for pattern in CODE_INDICATORS:
        if re.match(pattern, line):
            return True
    return False


def is_section_heading(line: str) -> bool:
    stripped = line.strip().lower().rstrip(":")
    if stripped in SECTION_KEYWORDS:
        return True
    if line.strip().endswith(":") and len(line.strip().split()) <= 4 and not is_code_line(line):
        return True
    return False


def normalize_heading(line: str) -> str:
    stripped = line.strip()
    if stripped.startswith("#"):
        return stripped
    if stripped.isupper() and len(stripped.split()) <= 8 and len(stripped) > 3:
        return f"## {stripped.title()}"
    if is_section_heading(stripped):
        return f"## {stripped.rstrip(':').title()}"
    return None


def normalize_list_item(line: str) -> str:
    stripped = line.strip()
    if re.match(r"^[*+]\s", stripped):
        return f"- {stripped[2:]}"
    match = re.match(r"^(\d+)[.):\]]\s*(.*)", stripped)
    if match:
        return f"{match.group(1)}. {match.group(2)}"
    return None


def convert_note_to_admonition(line: str) -> str:
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


def auto_detect_category(text: str) -> str:
    text_lower = text.lower()
    tutorial_score = sum([
        text_lower.count("learn"),
        text_lower.count("first time"),
        text_lower.count("introduction"),
        text_lower.count("beginner"),
        text_lower.count("getting started"),
    ])
    howto_score = sum([
        text_lower.count("how to"),
        text_lower.count("steps"),
        text_lower.count("procedure"),
        text_lower.count("setup"),
        text_lower.count("configure"),
    ])
    reference_score = sum([
        text_lower.count("reference"),
        text_lower.count("spec"),
        text_lower.count("parameter"),
        text_lower.count("option"),
        text_lower.count("flag"),
    ])
    explanation_score = sum([
        text_lower.count("why"),
        text_lower.count("because"),
        text_lower.count("concept"),
        text_lower.count("understand"),
        text_lower.count("overview"),
    ])
    scores = {
        "tutorial": tutorial_score,
        "how-to": howto_score,
        "reference": reference_score,
        "explanation": explanation_score,
    }
    return max(scores, key=scores.get)


def extract_title_from_text(text: str) -> str:
    for line in text.split("\n"):
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("-") or stripped.startswith("*"):
            continue
        if re.match(r"^\d+[.)]\s", stripped):
            continue
        if any(stripped.upper().startswith(k) for k in NOTE_KEYWORDS):
            continue
        clean = re.sub(r"^#+\s*", "", stripped)
        return clean.title()
    return "Untitled Document"


def generate_footer(author: str) -> str:
    date_str = datetime.now().strftime("%B %Y")
    return f"\n---\n\n*Last updated: {date_str} · Author: {author} · Submit corrections via merge request*\n"


def format_document(raw_text: str, title: str, author: str, category: str, verbose: bool = False) -> str:
    lines = raw_text.split("\n")
    output_lines = []
    in_code_block = False
    code_buffer = []
    code_language = "bash"
    first_content_line = True

    output_lines.append(generate_metadata_header(title, author, category))

    for line in lines:
        stripped = line.strip()

        if not stripped:
            if in_code_block:
                code_buffer.append("")
            else:
                output_lines.append("")
            continue

        if first_content_line:
            first_content_line = False
            if not stripped.startswith("-") and not stripped.startswith("*"):
                if not any(stripped.upper().startswith(k) for k in NOTE_KEYWORDS):
                    if not stripped.startswith("#"):
                        continue

        if is_code_line(stripped) and not in_code_block:
            in_code_block = True
            code_language = detect_language(stripped)
            clean_line = re.sub(r"^[$>]\s*", "", stripped)
            code_buffer.append(clean_line)
            if verbose:
                print(f"  [CODE] {stripped[:50]}")
            continue

        if in_code_block and not is_code_line(stripped):
            output_lines.append(f"```{code_language}")
            output_lines.extend(code_buffer)
            output_lines.append("```\n")
            code_buffer = []
            in_code_block = False

        if in_code_block:
            clean_line = re.sub(r"^[$>]\s*", "", stripped)
            code_buffer.append(clean_line)
            continue

        admonition = convert_note_to_admonition(stripped)
        if admonition:
            output_lines.append(admonition)
            if verbose:
                print(f"  [ADMONITION] {stripped[:50]}")
            continue

        heading = normalize_heading(stripped)
        if heading:
            output_lines.append(f"\n{heading}\n")
            if verbose:
                print(f"  [HEADING] {stripped} → {heading}")
            continue

        list_item = normalize_list_item(stripped)
        if list_item:
            output_lines.append(list_item)
            continue

        output_lines.append(stripped)

    if in_code_block and code_buffer:
        output_lines.append(f"```{code_language}")
        output_lines.extend(code_buffer)
        output_lines.append("```\n")

    output_lines.append(generate_footer(author))
    return "\n".join(output_lines)


def process_file(input_path: str, output_path: str, author: str, category: str, verbose: bool = False):
    with open(input_path, "r", encoding="utf-8") as f:
        raw_text = f.read()

    title = extract_title_from_text(raw_text)

    if category == "auto":
        category = auto_detect_category(raw_text)
        if verbose:
            print(f"  [AUTO] Detected category: {category}")

    formatted = format_document(raw_text, title, author, category, verbose)
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(formatted)

    print(f"Done: {input_path} → {output_path} [{category}]")


def process_directory(input_dir: str, output_dir: str, author: str, category: str, verbose: bool = False):
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

    print(f"\nDone: {len(files)} files → {output_dir}")


def main():
    parser = argparse.ArgumentParser(
        description="Convert raw notes into structured Markdown documentation.",
        epilog="Example: python format_notes.py --input notes.txt --output docs/how-to/guide.md",
    )
    parser.add_argument("--input", "-i", help="Path to input file")
    parser.add_argument("--output", "-o", help="Path for output Markdown file")
    parser.add_argument("--input-dir", help="Directory of files to batch process")
    parser.add_argument("--output-dir", help="Output directory for batch processing")
    parser.add_argument("--author", "-a", default="Arshad Naguru", help="Author name")
    parser.add_argument(
        "--category", "-c",
        default="auto",
        choices=VALID_CATEGORIES + ["auto"],
        help="Diátaxis category (default: auto-detect)",
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="Print transformation details")

    args = parser.parse_args()

    if args.input and args.output:
        process_file(args.input, args.output, args.author, args.category, args.verbose)
    elif args.input_dir and args.output_dir:
        process_directory(args.input_dir, args.output_dir, args.author, args.category, args.verbose)
    else:
        parser.error("Provide --input/--output or --input-dir/--output-dir")


if __name__ == "__main__":
    main()