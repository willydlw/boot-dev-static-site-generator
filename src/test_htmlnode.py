import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        # Test case 1: Multiple attributes
        node = HTMLNode(
            tag="a",
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_empty(self):
        # Test case 2: No attributes (None)
        node = HTMLNode(tag="p")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_empty_dict(self):
        # Test case 3: Empty dictionary attributes
        node = HTMLNode(tag="p", props={})
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        # Test case 4: Check representation
        node = HTMLNode(tag="h1", value="Hello")
        expected = "HTMLNode(tag=h1, value=Hello, children=None, props=None)"
        self.assertEqual(repr(node), expected)

if __name__ == "__main__":
    unittest.main()
