
type Props = dict[str, str | None]

class HTMLNode:
    def __init__(self, tag:str | None = None, value:str | None = None, children:list["HTMLNode"] | None = None, props:Props | None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        props = ""
        if not self.props:
            return props
        for item in self.props.items():
            key, value = item
            props +=f' {key}="{value}"'
        return props

    def __repr__(self):
        return f"HTMLNode({self.tag},{self.value},{self.children},{self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag:str, children:list[HTMLNode], props:Props | None = None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Parent node must have a tag")
        if not self.children:
            raise ValueError("Parent must have childrens")
        childrenHtml = []
        for child in self.children:
            childrenHtml.append(child.to_html())
        return f'<{self.tag}>{"".join(childrenHtml)}</{self.tag}>'

class LeafNode(HTMLNode):
    def __init__(self, tag:str | None, value:str, props:Props | None = None):
        super().__init__(value=value, tag=tag, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("No value found on leaf")
        if self.tag:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        else:
            return self.value

    def __repr__(self):
        return f"LeafNode({self.tag},{self.value},{self.props})"
        
    
        
