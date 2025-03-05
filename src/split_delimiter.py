from textnode import TextNode, TextType

from extract_md_img_and_links import (
    extract_markdown_links,
    extract_markdown_images
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        split_node_list = []
        if node.text_type == TextType.TEXT:
            text_list = node.text.split(delimiter)
            if len(text_list) % 2 == 0:
                raise ValueError("invalid markdown, formatted section not closed")
            for i in range(len(text_list)):
                if text_list[i] == "":
                    continue
                if i % 2 == 0:
                    split_node_list.append(TextNode(text_list[i], TextType.TEXT))
                else:
                    split_node_list.append(TextNode(text_list[i], text_type))
            new_nodes.extend(split_node_list)
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        split_node_list = []
        if node.text_type == TextType.TEXT:
            new_text = node.text
            image_list = extract_markdown_images(node.text)
            text_list = []
            for image in image_list:
                text_list = new_text.split(f"![{image[0]}]({image[1]})", 1)
                split_node_list.append(TextNode(text_list[0], TextType.TEXT))
                split_node_list.append(TextNode(image[0], TextType.IMAGE, image[1]))
                new_text = text_list[1]
            if new_text:
                split_node_list.append(TextNode(new_text, TextType.TEXT))
            new_nodes.extend(split_node_list)
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        split_nodes_list = []
        if node.text_type == TextType.TEXT:
            new_text = node.text
            link_list = extract_markdown_links(node.text)
            text_list = []
            for link in link_list:
                text_list = new_text.split(f"[{link[0]}]({link[1]})", 1)
                split_nodes_list.append(TextNode(text_list[0], TextType.TEXT))
                split_nodes_list.append(TextNode(link[0], TextType.LINK, link[1]))
                new_text = text_list[1]
            if new_text:
                split_nodes_list.append(TextNode(new_text, TextType.TEXT))
            new_nodes.extend(split_nodes_list)
        else:
            new_nodes.append(node)
    return new_nodes




node = TextNode(
    "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png) is the last",
    TextType.TEXT,
)








