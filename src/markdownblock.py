import enum

from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextNode, TextType, text_node_to_html_node, text_to_textnodes

class BlockType(enum.Enum):
    PARAGRAPH = 1
    HEADING = 2
    CODE = 3
    QUOTE = 4
    UNORDERED_LIST = 5
    ORDERED_LIST = 6

def markdown_to_blocks(markdown:str)->list[str]:
    blocks:list[str] = []
    markdown_splitted = markdown.split("\n\n")
    for raw_block in markdown_splitted:
        if raw_block == "":
            continue
        block = raw_block.strip()
        blocks.append(block)
    return blocks

def block_to_block_type(text:str)->BlockType:
    lines = text.split("\n")
    if text.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if text.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if text.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if text.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown:str)->HTMLNode:
    markdown_blocks = markdown_to_blocks(markdown)
    children:list[HTMLNode] = []
    for block in markdown_blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children)


def block_to_html_node(text_block:str)->HTMLNode:
    block_type = block_to_block_type(text_block)
    match(block_type):
        case BlockType.PARAGRAPH:
            return paragraph_to_html_node(text_block)
        case BlockType.HEADING:
            return heading_to_html_node(text_block)
        case BlockType.CODE:
            return code_to_html_node(text_block)
        case BlockType.QUOTE:
            return quote_to_html_node(text_block)
        case BlockType.UNORDERED_LIST:
            return unordered_list_to_html_node(text_block)
        case BlockType.ORDERED_LIST:
            return ordered_list_to_html_node(text_block)
        case _:
            raise ValueError("invalid block type")
        

def text_to_children(text:str)->list[HTMLNode]:
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def paragraph_to_html_node(text_block:str)->ParentNode:
    lines = text_block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(text_block:str)->ParentNode:
    level = 0
    for char in text_block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(text_block):
        raise ValueError(f"invalid heading level: {level}")
    text = text_block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(text_block:str)->ParentNode:
    if not text_block.startswith("```") or not text_block.endswith("```"):
        raise ValueError("invalid code block")
    text = text_block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])


def quote_to_html_node(text_block:str)->ParentNode:
    lines = text_block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)


def unordered_list_to_html_node(text_block:str)->ParentNode:
    items = text_block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def ordered_list_to_html_node(text_block:str)->ParentNode:
    items = text_block.split("\n")
    html_items = []
    for item in items:
        parts = item.split(". ", 1)
        text = parts[1]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)