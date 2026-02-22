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
    

