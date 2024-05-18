# Comment Extractor Library Usage Guide

This guide provides instructions on how to use the Comment Extractor library to extract comments from various programming language files.

## Installation

To use the Comment Extractor library, you need to have Python installed on your system. You can then install the library using the following command:

```bash
pip install comment-extractor
```

## Basic Usage

To extract comments from a file, you can use the `extract_comments_from_file` function from the `core` module. Here's an example of how to use this function:

```python
from comment_extractor.core import extract_comments_from_file

# Replace 'path_to_file' with the actual file path
comments = extract_comments_from_file('path_to_file')

# Print the extracted comments
for comment in comments:
    print(comment)
```

## Supported Languages

The library currently supports the following programming languages:
- Python
- Java
- C++
- JavaScript

## Examples

### Extracting Comments from a Python File

```python
comments = extract_comments_from_file('example.py')
for comment in comments:
    print(comment)
```

### Extracting Comments from a Java File

```python
comments = extract_comments_from_file('Example.java')
for comment in comments:
    print(comment)
```

### Extracting Comments from a C++ File

```python
comments = extract_comments_from_file('example.cpp')
for comment in comments:
    print(comment)
```

### Extracting Comments from a JavaScript File

```python
comments = extract_comments_from_file('example.js')
for comment in comments:
    print(comment)
```

For more detailed documentation and advanced usage, please refer to the `README.md` file in the library's root directory.
