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
    parent = node.left
    node.left = parent.right
    parent.right = node

    return right_rotate(parent)

def left_zigzig(node):
    parent = node.right
    node.right = parent.right
    parent.right = node

    return left_rotate(parent)

def right_zigzag(node):
    parent = node.left
    node.left = parent.right
    parent.right = node

    return right_rotate(parent)

def left_zigzag(node):
    parent = node.right
    node.right = parent.left
    parent.left = node

    return left_rotate(parent)

def splay(root, key):
    print('s(p)laying')
    # if we have none we return none
    if not root:
        return None
    # if we found the key return the root
    if key == root.key:
        return root
    
    if key < root.key:
        if not root.left:
            return root

        if key == root.left.key:
            return right_rotate(root)

        if key < root.left.key:
            root.left.left = splay(root.left.left, key)
            return right_zigzig(root)
        else:
            root.left.right = splay(root.left.right, key)
            if not root.left.right:
                return right_zigzig(root)
            return left_zigzag(root)

    else:
        if not root.right:
            return root

        if key == root.right.key:
            return left_rotate(root)

        if key > root.right.key:
            root.right.right = splay(root.right.right, key)
            return left_zigzig(root)
        else:
            root.right.left = splay(root.right.left, key)
            if not root.right.left:
                return left_zigzig(root)
            return right_zigzag(root)
        
def insert(root, key):
    print("inserting")
    root = splay(root, key)
    if root.key == key:
        raise RuntimeError('Duplicate values') # we will handle this later
    new_root = Node(key, None, None)
    if root.key < key:
        new_root.left = root
        new_root.right = root.right
        root.right = None
    elif root.key > key:
        new_root.right = root
        new_root.left = root.left
        root.left = None
    return new_root

def delete(root, key):
    print("deleting")

# returns the key at the top after splaying the seeked key. That key will either be the seeked key or the nearest key
def search(root, key):
    root = splay(root, key)
    return root.key
    

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
