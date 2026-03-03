from textnode import TextNode, TextType

def main():
    print("hello world")
    
    # Chapter 2, lesson 1: create a new TextNode object with dummy values
    # print the object to ensure it looks like our expected format
    dummy_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(dummy_node)

if __name__ == "__main__":
    main()
