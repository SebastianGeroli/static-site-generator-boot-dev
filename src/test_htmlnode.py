import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_raise_not_NotImplementedError(self):
       with self.assertRaises(NotImplementedError):
           node = HTMLNode()
           node.to_html()

    def test_props(self):
        node = HTMLNode(props={"target":"some_target"})
        self.assertEqual(node.props_to_html(), ' target="some_target"')

    def test_tag(self):
            node = HTMLNode(tag="<a>")
            self.assertEqual(node.tag,"<a>")
            

if __name__ == "__main__":
    unittest.main()