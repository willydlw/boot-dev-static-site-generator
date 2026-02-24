import unittest
from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode("This is **bold** and **more bold**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("more bold", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is italic _word_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is italic ", TextType.TEXT),
                TextNode("word", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is code `block`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is code ", TextType.TEXT),
                TextNode("block", TextType.CODE),
            ],
            new_nodes,
        )

    def test_unclosed_delimiter(self):
        node = TextNode("This is **invalid bold", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD)


class TestMarkdownExtractors(unittest.TestCase):
    
    # --- Image Extraction Tests ---
    
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)


    def test_extract_multiple_images(self):
        text = "![alt1](url1.png) and some filler ![alt2](url2.gif)"
        matches = extract_markdown_images(text)
        self.assertListEqual([("alt1", "url1.png"), ("alt2", "url2.gif")], matches)

    def test_extract_images_with_no_alt_text(self):
        text = "An image with no alt: ![](https://example.com/logo.png)"
        matches = extract_markdown_images(text)
        self.assertListEqual([("", "https://example.com/logo.png")], matches)

    # --- Link Extraction Tests ---

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "Check out [Boot.dev](https://www.boot.dev)"
        )
        self.assertListEqual([("Boot.dev", "https://www.boot.dev")], matches)

    def test_extract_multiple_links(self):
        text = "Links to [Google](https://google.com) and [YouTube](https://youtube.com)"
        matches = extract_markdown_links(text)
        self.assertListEqual([("Google", "https://google.com"), ("YouTube", "https://youtube.com")], matches)

    # --- Cross-Pollination Tests (The Tricky Parts) ---

    def test_links_do_not_extract_images(self):
        """
        The extract_markdown_links function should NOT return images,
        even though they share a similar bracket structure.
        """
        text = "This is a [link](https://link.com) and an !(https://img.com)"
        matches = extract_markdown_links(text)
        self.assertListEqual([("link", "https://link.com")], matches)

    def test_no_matches(self):
        text = "This text has no markdown links or images."
        self.assertEqual(extract_markdown_images(text), [])
        self.assertEqual(extract_markdown_links(text), [])

if __name__ == "__main__":
    unittest.main()
