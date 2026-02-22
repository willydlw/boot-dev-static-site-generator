from htmlnode import HTMLNode
from leafnode import LeafNode

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

