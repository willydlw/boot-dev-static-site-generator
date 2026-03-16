import unittest 

from gencontent import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        md = "# Hello"
        self.assertEqual(extract_title(md), "Hello")

    def test_extract_title_with_whitespace(self):
        md = "#    Hello World    "
        self.assertEqual(extract_title(md), "Hello World")

    def test_extract_title_multiline(self):
        md = """
This is a paragraph.
# The Real Title
## Subtitle
"""
        self.assertEqual(extract_title(md), "The Real Title")

    def test_no_h1_raises_exception(self):
        md = "## Only a subtitle"
        with self.assertRaises(Exception) as cm:
            extract_title(md)
        self.assertEqual(str(cm.exception), "No h1 header found in markdown")

if __name__ == "__main__":
    unittest.main()