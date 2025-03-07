from enum import Enum
import re

from htmlnode import HTMLNode, LeafNode, ParentNode
from text_to_text_node import text_to_text_node
from textnode import TextNode, TextType, text_node_to_html_node

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_block(markdown):
    block_list = markdown.strip().split("\n\n")
    clean_block_list = []
    for block in block_list:
        if block == "":
            continue
        clean_block_list.append(block.strip())
    return clean_block_list

def block_to_block_type(block):
    headings = [
        "# ", "## ", "### ", "#### ", "##### ", "###### "
    ]

    for head in headings:
        if head in block:
            return BlockType.HEADING
        
    if block[:3] == "```" and block[-3: ] == "```":
        return BlockType.CODE
    
    string_list = block.split("\n")
    if all(item.startswith(">") for item in string_list):
        return BlockType.QUOTE
    
    if all(item.startswith("- ") for item in string_list):
        return BlockType.UNORDERED_LIST
    
    flag = True
    i = 1
    for item in string_list:
        if item.startswith(f"{i}. "):
            i += 1
            continue
        else:
            flag = False
            break
    if flag == True:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    block_list = markdown_to_block(markdown)
    parent_node = ParentNode("div", [])
    for block in block_list:
        block_type = block_to_block_type(block)
        if block_type == BlockType.ORDERED_LIST or block_type == BlockType.UNORDERED_LIST:
            list_nodes = get_html_node_from_list(block, block_type)
            parent_node.children.append(list_nodes)
        else:
            tag, value = extract_tag_value_from_block(block, block_type)
            if tag == 'code':
                code_node = ParentNode(tag, [LeafNode(None, value)])
                pre_node = ParentNode("pre",[code_node])
                parent_node.children.append(pre_node)
            else:
                children = text_to_children(value)
                block_node = ParentNode(tag, children)
                parent_node.children.append(block_node)
    return parent_node

def get_html_node_from_list(block, block_type):
    block_list = block.split("\n")

    if block_type == BlockType.UNORDERED_LIST:
        parent_list = ParentNode("ul", [])
        block_list = [line[2:] for line in block_list if line.startswith("- ") and line.strip() ]
        for line in block_list:
            children = text_to_children(line)
            li_node = ParentNode("li", children)
            parent_list.children.append(li_node)
        return parent_list
    
    if block_type == BlockType.ORDERED_LIST:
        parent_list = ParentNode("ol", [])
        block_list = [line[line.find(".")+2:] for line in block_list if re.match(r"^\d+\.\s", line)]
        for line in block_list:
            children = text_to_children(line)
            li_node = ParentNode("li", children)
            parent_list.children.append(li_node)
        return parent_list




def extract_tag_value_from_block(block, block_type):
    if block_type == BlockType.HEADING:
        if block.startswith("# "):
            return "h1", block[2:].strip()
        if block.startswith("## "):
            return "h2", block[3:].strip()
        if block.startswith("### "):
            return "h3", block[4:].strip()
        if block.startswith("#### "):
            return "h4", block[5:].strip()
        if block.startswith("##### "):
            return "h5", block[6:].strip()
        if block.startswith("###### "):
            return "h6", block[7:].strip()
    if block_type == BlockType.CODE:
        lines = block.split("\n")
        code_text = "\n".join(lines[1:-1]) +"\n"
        return "code", code_text
    if block_type == BlockType.PARAGRAPH:
        content = " ".join(line.strip() for line in block.split("\n"))
        return "p", content
    if block_type == BlockType.QUOTE:
        lines = block.split("\n")
        lines = [line[2:] if line.startswith("> ") else line[1:] if line.startswith(">") else line for line in lines]
        quote_text = " ".join(lines)
        return "blockquote", quote_text
    
def text_to_children(text):
    text_nodes = text_to_text_node(text)
    html_nodes = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        html_nodes.append(html_node)
    return html_nodes

    



