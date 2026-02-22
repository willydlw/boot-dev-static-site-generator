import unittest 
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected)

    def test_leaf_to_html_div_with_attrs(self):
        node = LeafNode("div", "Content here", {"class": "container", "id": "main"})
        expected = '<div class="container" id="main">Content here</div>'
        self.assertEqual(node.to_html(), expected)

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just raw text.")
        self.assertEqual(node.to_html(), "Just raw text.")

    def test_leaf_to_html_no_value_error(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

    def test_repr(self):
        node = LeafNode("span", "Some text", {"style": "color: red;"})
        expected = "LeafNode(tag=span, value=Some text, props={'style': 'color: red;'})"
        self.assertEqual(repr(node), expected)

if __name__ == "__main__":
    unittest.main()