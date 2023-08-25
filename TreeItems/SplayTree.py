import json, math, re
from typing import List, Text, Union

class Node():
    def __init__(self, key, left, right):
        self.key = key # should be a string
        self.left = left
        self.right = right
    def __str__(self):
        return self.key

# ----------------------------------------------------------------

def left_rotate(node):
    new_root = node.right
    node.right = new_root.left
    new_root.left = node
    return new_root

def right_rotate(node):
    new_root = node.left
    node.left = new_root.right
    new_root.right = node
    return new_root

def right_zigzig(node):
    root = right_rotate(node)
    return right_rotate(root)

def left_zigzig(node):
    root = left_rotate(node)
    return left_rotate(root)

# Zig-Zag: left_zigzag
def left_zigzag(node):
    child = node.left
    node.left = left_rotate(child)
    return right_rotate(node)

# Zig-Zag: right_zigzag
def right_zigzag(node):
    child = node.right
    node.right = right_rotate(child)
    return left_rotate(node)

# ----------------------------------------------------------------

def splay(root, key):
    if not root:
        return None
    if key < root.key:
        if not root.left:
            return root
        if key < root.left.key and root.left.left and root.left.left.key == key:
            root.left.left = splay(root.left.left, key)
            if root.left.left:
                root = right_zigzig(root)
        elif key > root.left.key: # and root.left.right and root.left.right.key == key:
            root.left.right = splay(root.left.right, key)
            if root.left.right:
                 root = left_zigzag(root)
        else:
            root.left = splay(root.left, key)
            root = right_rotate(root)
    elif key > root.key:
        if not root.right:
            return root
        if key > root.right.key and root.right.right and root.right.right.key == key:
            root.right.right = splay(root.right.right, key)
            if root.right.right:
                root = left_zigzig(root)
        elif key < root.right.key: #and root.right.left and root.right.left.key == key:
            root.right.left = splay(root.right.left, key)
            if root.right.left:
                root = right_zigzag(root)
        else:
            root.left = splay(root.left, key)
            root = left_rotate(root)
    return root

# ----------------------------------------------------------------

# this is the way the professor showed us, however I think it doesn't do a great job of maintaining the recent
# items at the top of the tree, defeating the purpose of the splay.
def insertAfter(tree, key):
    new_tree = splay(tree, key)
    new_node = Node(key, None, None)
    if new_tree.key == key:
        raise ValueError("Key already exists") # may need to be changed to more agreeable code
        # return new_tree
    elif new_tree.key < key:
        new_node.right = new_tree.right
        new_tree.right = None
        new_node.left = new_tree
    elif new_tree.key > key:
        new_node.left = new_tree.left
        new_tree.left = None
        new_node.right = new_tree
    return new_node

# performs the insertion for the BST insertion function
def performInsert(tree, key):
    if tree == None or tree.key == key:          # remove the == piece to fix below *** fix
        raise ValueError("Something went wrong") # adjust such that it just splays this item
    elif key < tree.key:
        if tree.left:
            tree.left = performInsert(tree.left, key)
        else:
            tree.left = Node(key, None, None)
    elif key > tree.key:
        if tree.right:
            tree.right = performInsert(tree.right, key)
        else:
            tree.right = Node(key, None, None)
    return tree

# BST version. Probably a little slower than the version above but I think it actually does a better job of maintaining the most recent items
# at the top of the tree 🤔
def insertBST(tree, key):
    tree = performInsert(tree, key) # performs the actual insertion of the new node
    return splay(tree, key)         # returns the splayed tree with the new node at the root

# uses deletion method put together by Justin
# splays right tree and uses it
def delete(tree, key):
    mod_tree = splay(tree, key)
    if not mod_tree.left:
        return mod_tree.right
    elif not mod_tree.right:
        return mod_tree.left
    else:
        child_tree = splay(tree.right, key)
        child_tree.left = tree.left
        return child_tree

def search(tree, key):
    new_tree = splay(tree, key)
    return new_tree

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
