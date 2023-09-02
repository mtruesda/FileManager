import json

class Node:                     # reimplemented to include parent local variable
    def __init__(self, key):
        self.key = key          # key is value
        self.left = None        # left node option
        self.right = None       # right node option
        self.parent = None      # parent node option -- necessary for splay to work as intended.
    def __str__(self):
        return str(self.key)         # not sure why this doesn't work :/

class SplayTree:                # with this rewrite I decided to make the tree an object
    def __init__(self, tree):
        if tree:
            self.root = tree
        else:
            self.root = None

    def zig(self, x):
        parent = x.parent
        if parent.left == x: # right rotation
            parent.left = x.right
            x.right = parent
            x.parent = parent.parent
            parent.parent = x
        else:           # left rotation
            parent.right = x.left
            x.left = parent
            x.parent = parent.parent
            parent.parent = x

        if not x.parent:         # updates root when necessary
            self.root = x        # if x doesn't have a parent then it becomes the new root
        elif x.parent.left == parent: # replace parent of parents child with x -- fucking confusing shit
            x.parent.left = x
        else:
            x.parent.right = x   # does the same

        if parent.left:               # updates the parent pointers to the left and right children of p after p has replaced x
            parent.left.parent = parent
        if parent.right:
            parent.right.parent = parent

    def zigzig(self, x):   # abstracted properly this time thank god
        self.zig(x.parent)
        self.zig(x)

    def zigzag(self, x):   # same here. For whatever reason I ran into the issue of thinking I could just run the same as zigzig. Sorted itself with the debugger
        self.zig(x)
        self.zig(x)

    def splay(self, x):    # once I added parents to the node this became a joke. This was horrifying to write without parents on the nodes
        while x.parent:
            # check for each case and done
            if x.parent.parent is None:
                self.zig(x)
            elif x.parent.left == x and x.parent.parent.left == x.parent or \
                 x.parent.right == x and x.parent.parent.right == x.parent:
                self.zigzig(x)
            else:
                self.zigzag(x)

    # originally I wanted this function to work in the order of splaying and then inserting as with the class notes, but I found that it's far more accurate when you do it in the opposite order.
    def insert(self, key):
        # base case. Create tree
        if self.root is None:
            self.root = Node(key)
            return

        node = self.root
        while True:
            if key < node.key:
                if node.left is None:
                    node.left = Node(key)
                    node.left.parent = node
                    self.splay(node.left)
                    return
                node = node.left
            elif key > node.key:
                if node.right is None:
                    node.right = Node(key)
                    node.right.parent = node
                    self.splay(node.right)
                    return
                node = node.right
            else:
                self.splay(node)
                return

    # There was a lot of debate over whether to splay when inserting or to just determine if a key exists. I settled with splaying when inserting.
    # This does also make sure that if the key doesn't exist, it splays anyways with an inorder successor/predecessor
    def search(self, key):
        node = self.root
        last_left, last_right = None, None
        
        # searches for node
        while node:
            if key < node.key:
                last_left = node
                node = node.left
            elif key > node.key:
                last_right = node
                node = node.right
            else:
                self.splay(node)
                return node
        
        # if the node didn't exist it takes the last item that did and splays that instead. may modify this such that it looks for the closer of the two.
        if last_left:
            self.splay(last_left)
            return None
        elif last_right:
            self.splay(last_right)
            return None
        return None

    # it uses search.
    def delete(self, key):
        node_to_delete = self.search(key) # returns node if it exists, otherwise just splays the tree
        if node_to_delete is None:
             return                       # key didn't exist

        if node_to_delete.left and node_to_delete.right: # if both exist, we need to do weird stuff
            min_node = node_to_delete.left               # looks for the highest node in the left subtree (inorder successor)
            while min_node.right:
                min_node = min_node.right
            node_to_delete.key = min_node.key
            if min_node.parent.right == min_node:
                min_node.parent.right = min_node.left
            else:
                min_node.parent.left = min_node.left
            if min_node.left:
                min_node.left.parent = min_node.parent
        else:                                            # if only one exists, we only need that subtree
            if node_to_delete.left:
                self.root = node_to_delete.left
            else:
                self.root = node_to_delete.right

            if self.root:
                self.root.parent = None
    
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

# new load_tree function that plays with json strings... *yay*
# this actually wasn't that bad to put together with the parent portion
def load_tree(json_str: str) -> Node:
    def _from_dict(dict_repr) -> Node:
        if dict_repr == None or dict_repr == {}:
            return None
        node = Node(key=dict_repr["k"])
        node.left = _from_dict(dict_repr["l"])
        if node.left:
            node.left.parent = node
        node.right = _from_dict(dict_repr["r"])
        if node.right:
            node.right.parent = node
        return node

    try: 
        dict_repr = json.loads(json_str)
    except Exception as e:
        print(f"Exception encountered parsing the json string: {json_str}")
        raise e

    root = _from_dict(dict_repr)
    return root

# same with the dump_tree function
def dump_tree(root: Node) -> str:
    def _to_dict(node) -> dict:
        return {
            "k": node.key,
            "l": (_to_dict(node.left) if node.left is not None else None),
            "r": (_to_dict(node.right) if node.right is not None else None)
        }

    if root is None:
        dict_repr = {}
    else:
        dict_repr = _to_dict(root)

    return json.dumps(dict_repr)
