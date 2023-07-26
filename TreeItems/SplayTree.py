import json, math, re
from typing import List, Text, Union

class Node():
    def __init__(self, key, left, right):
        self.key = key # should be a string
        self.left = left
        self.right = right
    def __str__(self):
        return self.key
    
# takes in the root node to the rotated right and returns the new tree
# zig
def right_rotate(node):
    root = node.left
    node.left = root.right
    root.right = node
    return root

# takes in the root node to be rotated left and returns the new tree
# zig
def left_rotate(node):
    root = node.right
    node.right = root.left
    root.left = node
    return root

# uses rotate functions to rotate right right. Returns the new tree. Given the original root
def left_zigzig(node):
    node.left = right_rotate(node.left.left)
    root = right_rotate(node.left)
    return root

# uses the rotate functions to rotate left left. Returns the new tree. Given the original root
def right_zigzig(node):
    node.right = right_rotate(node.right.right)
    root = right_rotate(node.right)
    return root

def splay(root, key):
    if not root:
        return None
    if root.left and root.left.key == key:
        return right_rotate(root.left)
    elif root.right and root.right.key == key:
        return left_rotate(root.right)
    

# these three functions will return a list of nodes and I'll determine later how I want to parse that list
# may consider adding balance to the tree to see more accurate distance results
# using balance may allow me to see what is furthest or closest in the tree allowing for both a recents and a least recents section
def inorder(root):
    lst = []
    if root.left != None:
        lst += inorder(root.left)
    lst.append(root)
    if root.right != None:
        lst += inorder(root.right)
    return lst

def preorder(root):
    lst = [root]
    if root.left != None:
        lst += preorder(root.left)
    if root.right != None:
        lst += preorder(root.right)
    return lst
    
def postorder(root):
    lst = []
    if root.left != None:
        lst += postorder(root.left)
    if root.right != None:
        lst += postorder(root.right)
    lst.append(root)
    return lst

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
            "r": (_to_dict(node.right) if node.right is not None else None)
        }
    if root == None:
        dict_repr = {}
    else:
        dict_repr = _to_dict(root)
    return json.dumps(dict_repr)
