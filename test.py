import tree
from tree import *
import pydot_graph_util
from pydot_graph_util import *

# bunch of tree models below and then test functions

# base tree
tree = load_tree("""{"k": 10, "l": {"k": 5, "l": null, "r": null}, "r": {"k": 15, "l": null, "r": null}}""")

# base tree
tree2 = load_tree("""{"k": 15, "l": null, "r": null}""")

# testing a full zigzig on left
tree3 = load_tree("""{"k": 15, "l": 
                                   {"k": 10, "l": 
                                                 {"k": 5, "l": null, 
                                                          "r": null}, 
                                             "r": null},
                                "r": null}""")
# testing a full zigzig on right
tree4 = load_tree("""{"k": 15, "l": null,
                               "r": 
                                    {"k": 30, "l": null, 
                                              "r": {"k": 45, "l": null, 
                                                             "r": null}}}""")
# Zig zag test with left right
tree5 = load_tree("""{"k": 30, 
                              "l": {"k": 15, "l": null, 
                                             "r": {"k": 20, 
                                                           "l": null, 
                                                           "r": null}}, 
                              "r": null}""")

tree6 = load_tree("""{"k": 30, 
                              "l": null, 
                              "r": {"k": 45, 
                                        "l": {"k": 40, "l": null, "r": null}, 
                                        "r": null}}""")

# bigger base tree
example_tree = load_tree("""{"k": 30, "l": {"k": 10, "l": null, "r": null}, 
                                      "r": {"k": 50, "l": null, 
                                                     "r": {"k": 60, 
                                                                   "l": {"k": 55, "l": null, "r": null},
                                                                   "r": null}}}""")

def testBuildTree():
    testEmptyTree = None
    modTree = insert(testEmptyTree,30)
    modTree = insert(modTree, 10)
    modTree = insert(modTree, 40)
    modTree = insert(modTree, 35)
    modTree = insert(modTree, 36)
    modTree = delete(modTree, 30)
    construct_graph(modTree).write_png('modTree.png')

def testTraversals():
    construct_graph(example_tree).write_png('modified_tree.png')
    lst = postorder(example_tree)
    lst2 = preorder(example_tree)
    ls3 = inorder(example_tree)
    
def testStringInstance():
    emptyTree = None
    emptyTree = insert(emptyTree, 'hello')
    construct_graph(emptyTree).write_png('stringtest.png')

# call function
testStringInstance()

