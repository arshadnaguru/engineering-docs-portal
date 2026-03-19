# Automate Testing with Pytest

> **Author:** Arshad Naguru · **Last Updated:** March 2026 · **Category:** How-To

Write and run automated tests for Python projects using pytest.

## Install Pytest

```bash
pip install pytest pytest-cov
```

## Write Your First Test

Create `tests/test_utils.py`:

```python
from src.utils import format_title, calculate_word_count

def test_format_title():
    assert format_title("hello world") == "Hello World"
    assert format_title("") == ""
    assert format_title("ALREADY CAPS") == "Already Caps"

def test_calculate_word_count():
    assert calculate_word_count("hello world") == 2
    assert calculate_word_count("") == 0
    assert calculate_word_count("one") == 1

def test_format_title_with_special_chars():
    assert format_title("hello-world") == "Hello-World"
```

## Run Tests

```bash
# Run all tests
pytest

# Verbose output
pytest -v

# Run specific file
pytest tests/test_utils.py

# Run specific test
pytest tests/test_utils.py::test_format_title

# With coverage report
pytest --cov=src --cov-report=html
```

## Project Structure

```
project/
├── src/
│   ├── __init__.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_utils.py
│   └── test_api.py
├── pytest.ini
└── requirements.txt
```

## Configure pytest.ini

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_functions = test_*
addopts = -v --tb=short
```

---

*Last updated: March 2026 · Author: Arshad Naguru*
