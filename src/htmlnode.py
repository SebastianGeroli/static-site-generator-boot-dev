
type Props = dict[str,str]

class HTMLNode:
    def __init__(self, tag:str = None, value:str = None, children:list["HTMLNode"] = None, props:Props = None):
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

    
        
