from textnode import TextNode, TextType

def main():
    node = TextNode("hello", TextType.LINK, "www.google.com")
    print(node)

main()