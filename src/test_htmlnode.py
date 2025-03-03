import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TextHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        prop = {
                "href": "https://www.google.com",
                "target": "_blank",
                }
        
        node = HTMLNode("p", "A normal text", None, prop)
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_values(self):
        node = HTMLNode(
            "div",
            "Hello, World!",
            None,
            {"class": "greeting", "href": "https://boot.dev"}
        )

        self.assertEqual(
            node.tag,
            "div"
        )

        self.assertEqual(
            node.value,
            "Hello, World!"
        )

        self.assertEqual(
            node.children,
            None
        )

        self.assertEqual(
            node.props,
            {"class": "greeting", "href": "https://boot.dev"}
        )


    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>'
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()

