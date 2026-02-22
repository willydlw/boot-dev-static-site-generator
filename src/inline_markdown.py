from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        # We only split nodes that are of type TEXT
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        split_nodes = []
        sections = old_node.text.split(delimiter)
        
        # If the length is even, it means a delimiter was not closed
        # e.g. "text **bold" splits into ["text ", "bold"] (length 2)
        if len(sections) % 2 == 0:
            raise ValueError(f"Invalid markdown: matching delimiter '{delimiter}' not found")
        
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                # Even indices are the text outside the delimiters
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                # Odd indices are the text inside the delimiters
                split_nodes.append(TextNode(sections[i], text_type))
        
        new_nodes.extend(split_nodes)
        
    return new_nodes
