import re
from pygments import lexers
from pygments.token import Comment
from comment_parser import comment_parser
from comment_parser.comment_parser import UnsupportedError

def extract_comments_from_file(file_path):
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

    # Handle Python multiline comments (docstrings) which may not be captured by the lexer
    if lexer.name == 'Python':
        docstring_pattern = r'(\'\'\'[\s\S]*?\'\'\'|"""[\s\S]*?""")'
        docstrings = re.findall(docstring_pattern, content, re.MULTILINE)
        comments.extend(docstrings)

    # Handle JavaScript comments which may not be captured by the lexer
    if lexer.name == 'JavaScript':
        single_line_comment_pattern = r'//.*'
        multi_line_comment_pattern = r'/\*[\s\S]*?\*/'
        single_line_comments = re.findall(single_line_comment_pattern, content)
        multi_line_comments = re.findall(multi_line_comment_pattern, content)
        comments.extend(single_line_comments)
        comments.extend(multi_line_comments)

    return comments
