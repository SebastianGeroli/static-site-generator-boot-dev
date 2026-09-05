import unittest

from markdownblock import BlockType, block_to_block_type

class TestMarkdownBlocks(unittest.TestCase):
    def test_headings(self):
        headings = [
            "# Heading 1",
            "## Heading 2",
            "### Heading 3",
            "#### Heading 4",
            "##### Heading 5", 
            "###### Heading 6",
        ]
        expected = [
            BlockType.HEADING,
            BlockType.HEADING,
            BlockType.HEADING,
            BlockType.HEADING,
            BlockType.HEADING,
            BlockType.HEADING,
        ]
        block_types = []
        for heading in headings:
            block_type = block_to_block_type(heading)
            block_types.append(block_type)
        self.assertEqual(block_types, expected)

    def test_quotes(self):
        quotes = [
"""
> This is a quote
""",
"""
> This is quote
> This is also a quote 
""",
        ]
        expected = [
            BlockType.QUOTE,
            BlockType.QUOTE
        ]
        block_types = []
        for quote in quotes:
            block_type = block_to_block_type(quote)
            block_types.append(block_type)
        self.assertEqual(block_types, expected)

    def test_code(self):
        codes = [
"""
```
This is a code block
```
""",
"""
```
this is a code block
with multiple lines
```
""",
        ]
        expected = [
            BlockType.CODE,
            BlockType.CODE
        ]
        block_types = []
        for code in codes:
            block_type = block_to_block_type(code)
            block_types.append(block_type)
        self.assertEqual(block_types, expected)


    def test_unordered_list(self):
        unordered_lists = [
"""
- this is an unordered list
""",
"""
- this is an unordered list
- this is an unordered list
- this is an unordered list
"""
        ]
        expected = [
            BlockType.UNORDERED_LIST,
            BlockType.UNORDERED_LIST
        ]
        block_types = []
        for list in unordered_lists:
            block_type = block_to_block_type(list)
            block_types.append(block_type)
        self.assertEqual(block_types, expected)

    def test_ordered_list(self):
        ordered_lists = [
"""
1. ordered list
""",
"""
1. ordered list
2. ordered list
3. ordered list 
"""
        ]
        expected = [
            BlockType.ORDERED_LIST,
            BlockType.ORDERED_LIST
        ]
        block_types = []
        for list in ordered_lists:
            block_type = block_to_block_type(list)
            block_types.append(block_type)
        self.assertEqual(block_types, expected)

    def test_paragraph(self):
        paragraphs = [
"""
this is a paragraph.
""",
"""
####### this is also a paragraph
""",
"""
- this is a paragraph
because multiline is not a list
""",
"""
1. this is a paragraph
because multiline is not a list
""",
"""
``` this is a paragraph
because code is not between the backticks
```
""",
"""
```
``` this also is a paragraph
""",
        ]
        expected = [
            BlockType.PARAGRAPH,
            BlockType.PARAGRAPH,
            BlockType.PARAGRAPH,
            BlockType.PARAGRAPH,
            BlockType.PARAGRAPH,
            BlockType.PARAGRAPH,
            ]
        block_types = []
        for paragraph in paragraphs:
            block_type = block_to_block_type(paragraph)
            block_types.append(block_type)
        self.assertEqual(block_types, expected)

            


        


