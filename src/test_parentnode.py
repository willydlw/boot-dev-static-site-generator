import unittest 
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode


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