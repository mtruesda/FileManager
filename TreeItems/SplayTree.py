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

def right_zigzig(node):
    node.left = right_rotate(node.right)
    return right_rotate(node)

def left_zigzig(node):
    node.right = left_rotate(node.right)
    return left_rotate(node)

def left_zigzag(node):
    node.left = left_rotate(node.left)
    return right_rotate(node)

def right_zigzag(node):
    node.right = right_rotate(node.right)
    return left_rotate(node)

# I have spent an unholy amount of time trying to figure out this function.
# this should not have taken *nearly* as long as it has and I am honestly contemplating three terrible options
# The first choice--which I'll add in here--is to make the function so that it finds the point where it drops out and then
# reruns splay in its entirety. This function will be inefficient for the reason that it will run through the tree multiple times
# The second option is to somehow make the function such that it will go until it reaches an endpoint and then splay that last known node.
# The third and final option is to scratch the idea of splaying an unknown node altogether and implement search using a BST approach.
# The first and third are the laziest options.

def splay(root, key):
    # Base case: if the root is None or the root contains the key, return the root
    if root is None or root.key == key:
        return root

    # Zig: key is in the left subtree of the root
    if key < root.key:
        if root.left is None:
            return root
        # Zig-Zig: key is in the left-left subtree
        if key < root.left.key:
            root.left.left = splay(root.left.left, key)
            root = right_zigzig(root)
        # Zig-Zag: key is in the left-right subtree
        elif key > root.left.key:
            root.left.right = splay(root.left.right, key)
            root = left_zigzag(root)
        return right_rotate(root)

    # Zig: key is in the right subtree of the root
    elif key > root.key:
        if root.right is None:
            return root
        # Zig-Zig: key is in the right-right subtree
        if key > root.right.key:
            root.right.right = splay(root.right.right, key)
            root = left_zigzig(root)
        # Zig-Zag: key is in the right-left subtree
        elif key < root.right.key:
            root.right.left = splay(root.right.left, key)
            root = right_zigzag(root)
        return left_rotate(root)

    return root  # If the key is found at the root, no need to splay


# returns the key at the top after splaying the seeked key. That key will either be the seeked key or the nearest key
# the question will be if I want the search function to modify the tree. I'm leaning no but I'll leave the following commented here
# def search(root, key):
#     root = splay(root, key)
#     return root.key
    
# other search function -- returns nearest key without modification
def search(root, key):
    return splay(root, key).key


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
