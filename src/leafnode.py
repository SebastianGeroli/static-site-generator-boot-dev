from src.htmlnode import HTMLNode, Props

class LeafNode(HTMLNode):
    def __init__(self, tag:str | None, value:str, props:Props | None = None):
        super().__init__(value=value, tag=tag, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("No value found on leaf")
        if self.tag:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        else:
            return self.value

    def __repr__(self):
        return f"LeafNode({self.tag},{self.value},{self.props})"