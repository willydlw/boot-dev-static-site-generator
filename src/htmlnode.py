class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        """
            tag:    string representing the HTML tag name (e.g. "p", "a")
            value:  string representing the value of the HTML tag
                    (e.g. the text inside a paragraph)
            children: list of HTMLNode objects representing the children of this node 
            props:  A dictionary of key-value pairs representing the attributes 
                    of the HTML tag
        """
        self.tag = tag 
        self.value = value 
        self.children = children
        self.props = props 
    
    def to_html(self):
        """Child classes will override this to render HTML"""
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        """Returns a string representing HTML attributes."""
        if self.props is None or len(self.props) == 0:
            return ""

        props_str = ""
        for key, value in self.props.items():
            """ Leading space is important. HTML attributes are 
                always separated by spces.
            """
            props_str += f' {key}="{value}"'
        return props_str
    
    def __repr__(self):
        return (f"HTMLNode(tag={self.tag}, value={self.value}, "
                f"children={self.children}, props={self.props})")
    

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        """
        tag: string representing the HTML tag name (e.g. "p", "a")
        value: string representing the value of the HTML tag (e.g. the text inside a paragraph)
        props: A dictionary of key-value pairs representing the attributes of the HTML tag
        """

        # Leaf nodes should not allow children, so we explicity pass children as None
        super().__init__(tag, value, children=None, props=props)
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
    
    def to_html(self):
        """Renders leaf node as an HTML string"""
        if self.tag is None:
            return self.value 
        # Get the HTML attributes string from the parent class method 
        props_str = self.props_to_html()
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        """Overrides the __repr__ method to not include children in the string"""
        return (f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})")
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        # tag and children are mandatory, no value argument 
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: ParentNode must have a tag.")
        if self.children is None:
            raise ValueError("Invalid HTML: ParentNode must have children.")
        
        children_html = ""
        for child in self.children:
            # recursively calls to_html() 
            children_html += child.to_html() 
        
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
