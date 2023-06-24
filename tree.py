# Author: @MyronTruesdale
# Date: 2023-03-16
#
# file for the splay tree


import json
import math

from typing import List, Text, Union

# Node class
class Node():
    def __init__(self, key, left, right):
        self.key = key      # should be a string
        self.left = left    # node left
        self.right = right  # node right

def insert(root, key):
    edgeNode = splay(root, key)
    return None

def delete(root, key):
    edgeNode = splay(root, key, None)
    return None

def splay(root, key, parent):
    if root.key > key and root.right != None:
        splay(root.right, key, root)
    elif root.key < key and root.left != None:
        splay(root.right, key, root)
    else:
        values = (root, parent)

# Movement Operations Below
def zig(root, node):
    if node == root.left:
        temp = node.right
        node.right = root
        root.left = temp
    elif node == root.right:
        temp = node.left
        node.left = root
        root.right = temp
    else:
        return None
    return node

# will possibly work to zig zag as well because of how zig works?
def zigzig(root, node):
    root = zig(root, node)
    root = zig(root, node)
    return root

# trying to get better with JSON
def load_tree(json_str: str) -> Node:
    def _from_dict(dict_repr) -> Node:
        if dict_repr == None or dict_repr == {}:
            return None
        return Node(key=dict_repr["k"],
                    left=_from_dict(dict_repr["l"]),
                    right=_from_dict(dict_repr["r"]))
    try: 
        dict_repr = json.loads(json_str)
    except Exception as e:
        print(f"Exception encountered parsing the json string: {json_str}")
        raise e
    root = _from_dict(dict_repr)
    return root

# changing a tree to a JSON string
def dump_tree(root: Node) -> str:
    def _to_dict(node) -> dict:
        return {
            "k": node.key,
            "l": (_to_dict(node.left) if node.left is not None else None),
            "r": (_to_dict(node.right) if node.right is not None else None),
        }
    if root == None:
        dict_repr = {}
    else:
        dict_repr = _to_dict(root)
    return json.dumps(dict_repr)