# Author: @MyronTruesdale
# Date: 2023-03-16
#
# file for the splay tree

import json, math, re
from typing import List, Text, Union

# Node class
class Node():
    def __init__(self, key, left, right):
        self.key = key      # should be a string
        self.left = left    # node left
        self.right = right  # node right
        
# I believe this is gucci. Gonna have to test it.
def insert(root, key):
    if root is None:
        return Node(key, None, None)
    node = None
    moddedTree = splay(root, search(root, key, "insert"))
    if key > moddedTree.key:
        node = Node(key, moddedTree, moddedTree.right)
        node.left.right = None
    elif key < moddedTree.key:
        node = Node(key, moddedTree.left, moddedTree)
        node.right.left = None
    else:
        raise RuntimeError("Not sure what's going on")
    return node

# this function needs to be tested
# search function may not need stri specification.
def delete(root, key):
    if root == None:
        return None
    root = splay(root, search(root, key, "delete"))
    if root.key == key:
        if root.left is None:
            root = root.right
        elif root.right is None:
            root = root.left
        else:
            root.right = splay(root.right, search(root.right, key, "delete"))
            root.right.left = root.left
            root = root.right
    return root

# works. Finds the nearest ancestor to the given key and returns its key
def search(root, key, stri):
    if root is None:
        return None
    elif root.key == key and stri == "insert":
        raise ValueError("Already exists within the tree") # can be written to avoid error -- come back to this
    elif root.left != None and key < root.key:
        return search(root.left, key, stri)
    elif root.right != None and key > root.key:
        return search(root.right, key, stri)
    else:
        return root.key

# made a more cleaned up version I guess. Hopefully more efficient than before.
def splay(root, key):
    if root == None or root.key == key:
        return root
    if root.left is not None:
        # zig case
        if root.left.key == key:
            return zig(root, root.left)
        # zigzag case
        elif root.left.right is not None and root.left.right.key == key:
            return zigzag(root.left, root.left.right, root)
        # zigzig case
        elif root.left.left is not None and root.left.left.key == key:
            return zigzig(root.left, root.left.left, root)
    if root.right is not None:
        # zig case
        if root.right.key == key:
            return zig(root, root.right)
        # zigzag case
        elif root.right.left is not None and root.right.left.key == key:
            return zigzag(root.right, root.left.right, root)
        # zigzig case
        elif root.right.right is not None and root.right.right.key == key:
            return zigzig(root.right, root.right.right, root)
    # otherwise go deeper
    if key > root.key:
        root.right = splay(root.right, key)
    elif key < root.key:
        root.left = splay(root.left, key)
    else:
        raise ValueError("Something weird happened")

# Movement Operations Below

# basically automatically performs a rotation based on the node location
def zig(root, node):
    if root.left is not None and node.key == root.left.key:
        temp = node.right
        node.right = root
        root.left = temp
    elif root.right is not None and node.key == root.right.key:
        temp = node.left
        node.left = root
        root.right = temp
    else:
        return None
    return node

# performs zigzig algorithm. A little jank
# "A temporary solution is often a permanent one"
def zigzig(root, node, grandParent):
    root = zig(grandParent, root)
    node = zig(root, node)
    return node

def zigzag(root, node, grandParent):
    if grandParent.right == root:
        grandParent.right = zig(root, node)
        grandParent = zig(grandParent, grandParent.right)
    elif grandParent.left == root:
        grandParent.left = zig(root, node)
        grandParent = zig(grandParent, grandParent.left)
    else:
        raise ValueError
    return grandParent


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

