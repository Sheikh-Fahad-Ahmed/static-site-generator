from textnode import TextNode, TextType

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











