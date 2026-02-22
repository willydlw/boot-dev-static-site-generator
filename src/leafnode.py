from htmlnode import HTMLNode 

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
    