from textnode import TextNode, TextType

def main():
    print("hello world")
    
    # Create a dummy TextNode as requested
    dummy_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(dummy_node)

if __name__ == "__main__":
    main()
