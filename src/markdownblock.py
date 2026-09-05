import enum

class BlockType(enum.Enum):
    PARAGRAPH = 1
    HEADING = 2
    CODE = 3
    QUOTE = 4
    UNORDERED_LIST = 5
    ORDERED_LIST = 6

def block_to_block_type(text:str)->BlockType:

    # Heading
    for i in range(0, 6):
        if i > len(text) or i+1 > len(text):
            break
        if text[i] == "#" and text[i+1] == " ":
            return BlockType.HEADING
    # Code
    code_text = text.strip("\n").strip()
    if code_text.startswith("```\n") and code_text.endswith("```"):
        return BlockType.CODE
    # Quote
    
    lines = text.split("\n")
    is_quote = True
    for line in lines:
        if line == "":
            continue
        if not line.startswith(">"):
            is_quote = False
            break
    if is_quote:
        return BlockType.QUOTE
    # Unordered list
    is_unordered_list = True
    for line in lines:
        if line == "":
            continue
        if not line.startswith("- "):
            is_unordered_list = False
            break
    if is_unordered_list:
        return BlockType.UNORDERED_LIST
    # Ordered list
    is_ordered_list = True
    count = 1
    for line in lines:
        if line == "":
            continue
        if not line.startswith(f"{count}. "):
            is_ordered_list = False
            break
        count += 1
    if is_ordered_list:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH


    
     
        
