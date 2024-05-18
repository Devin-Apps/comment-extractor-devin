import re
from pygments import lexers
from pygments.token import Comment
from comment_parser import comment_parser, UnsupportedError

def extract_comments(file_path):
    # Determine the lexer for the given file based on its extension
    try:
        lexer = lexers.get_lexer_for_filename(file_path)
    except ValueError:
        raise ValueError(f"No lexer found for file {file_path}")

    comments = []

    # Read the content of the file
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except (IOError, OSError) as e:
        raise IOError(f"Error opening or reading file {file_path}: {e}")
    except UnicodeDecodeError as e:
        raise UnicodeDecodeError(f"Encoding error in file {file_path}: {e}")

    # Extract tokens from the content using the lexer
    tokens = lexer.get_tokens(content)

    # Filter out the comment tokens
    comments.extend([token[1] for token in tokens if token[0] in Comment])

    # Additionally, use comment_parser for languages that are not well-supported by pygments
    try:
        parsed_comments = comment_parser.extract_comments(file_path)
        comments.extend([comment.text() for comment in parsed_comments])
    except UnsupportedError:
        pass  # If the language is not supported by comment_parser, just ignore

    return comments
