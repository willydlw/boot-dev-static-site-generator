import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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
        

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    # New Edge Case Tests
    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold Title"),
                LeafNode(None, " & Subtitle"),
            ],
        )
        self.assertEqual(node.to_html(), "<h2><b>Bold Title</b> & Subtitle</h2>")

    def test_to_html_with_props(self):
        node = ParentNode(
            "div",
            [LeafNode("p", "content")],
            {"class": "container", "id": "main"}
        )
        self.assertEqual(
            node.to_html(),
            '<div class="container" id="main"><p>content</p></div>'
        )

    def test_to_html_no_tag(self):
        node = ParentNode(None, [LeafNode("b", "child")])
        with self.assertRaises(ValueError) as cm:
            node.to_html()
        self.assertEqual(str(cm.exception), "Invalid HTML: ParentNode must have a tag.")

    def test_to_html_no_children(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError) as cm:
            node.to_html()
        self.assertEqual(str(cm.exception), "Invalid HTML: ParentNode must have children.")

    def test_empty_children_list(self):
        # A list that is empty should still render tags, just with nothing inside
        node = ParentNode("div", [])
        self.assertEqual(node.to_html(), "<div></div>")


if __name__ == "__main__":
    unittest.main()
