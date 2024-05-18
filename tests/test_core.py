import unittest
from core import extract_comments_from_file

class TestExtractComments(unittest.TestCase):

    def test_extract_comments_python(self):
        # Test extraction from a Python file
        python_comments = extract_comments_from_file('test_files/test_python.py')
        self.assertIn("# This is a single-line comment in Python", python_comments)
        # Check for multiline comment start without relying on a specific index
        self.assertTrue(any('"""' in comment for comment in python_comments))

    def test_extract_comments_java(self):
        # Test extraction from a Java file
        java_comments = extract_comments_from_file('test_files/test_java.java')
        self.assertIn("// This is a single-line comment in Java", java_comments)
        self.assertIn("/*", java_comments[1])  # Check for multiline comment start

    def test_extract_comments_cpp(self):
        # Test extraction from a C++ file
        cpp_comments = extract_comments_from_file('test_files/test_cpp.cpp')
        # Adjust assertion to account for newline character at the end of the comment
        self.assertIn("// This is a single-line comment in C++\n", cpp_comments)
        self.assertIn("/*", cpp_comments[1])  # Check for multiline comment start

    def test_extract_comments_javascript(self):
        # Test extraction from a JavaScript file
        js_comments = extract_comments_from_file('test_files/test_javascript.js')
        self.assertIn("// This is a single-line comment in JavaScript", js_comments)
        self.assertIn("/*", js_comments[1])  # Check for multiline comment start
        self.assertIn("// This is an inline comment in JavaScript", js_comments)  # Check for inline comment

    def test_no_comments(self):
        # Test a file with no comments
        no_comments = extract_comments_from_file('test_files/test_no_comments.txt')
        self.assertEqual(len(no_comments), 0)

    def test_file_not_found(self):
        # Test file not found error handling
        with self.assertRaises(IOError):
            extract_comments_from_file('test_files/non_existent_file.txt')

    def test_unsupported_language(self):
        # Test unsupported language error handling
        with self.assertRaises(ValueError):
            extract_comments_from_file('test_files/test_unsupported.lang')

if __name__ == '__main__':
    unittest.main()
