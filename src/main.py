from textnode import TextNode, TextType

from htmlnode import HTMLNode
def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

    prop = {
                "href": "https://www.google.com",
                "target": "_blank",
                }
    html_node = HTMLNode("p", "A normal text", None, prop)
    print(html_node)


main()