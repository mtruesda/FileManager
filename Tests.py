from TreeItems.SplayTree import *
from Utility.pydot_graph_util import *

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
                                                                   "l": {"k": 55, "l": null, 
                                                                                  "r": {"k": 57, "l": null, "r": null}},
                                                                   "r": null}}}""")
def printTrees():
    construct_graph(tree).write_png('Images/tree.png')
    construct_graph(tree2).write_png('Images/tree2.png')
    construct_graph(tree3).write_png('Images/tree3.png')
    construct_graph(tree4).write_png('Images/tree4.png')
    construct_graph(tree5).write_png('Images/tree5.png')
    construct_graph(tree6).write_png('Images/tree6.png')
    construct_graph(example_tree).write_png('Images/example_tree.png')

def zigzig(tree):
    tree3 = right_zigzig(tree)
    construct_graph(tree3).write_png('Images/modified_tree3.png')
    tree3 = left_zigzig(tree3)
    construct_graph(tree3).write_png('Images/modified_tree3_2.png')

def zigzag(tree):
    tree5 = left_zigzag(tree)
    construct_graph(tree5).write_png('Images/modified_tree5.png')

def zigzag2(tree):
    tree6 = right_zigzag(tree)
    construct_graph(tree6).write_png('Images/modified_tree6.png')

def splayTest(tree):
    test_tree = splay(tree, 57)
    construct_graph(test_tree).write_png('Images/modified_example_tree.png')

def searchTestFound(tree):
    new_tree = search(tree, 60)
    construct_graph(tree).write_png('Images/modified_search.png')

def searchTestNotFound(tree):
    new_tree = search(tree, 65)
    construct_graph(tree).write_png('Images/modified_search_nf.png')

def insertTreeTest(tree):
    new_tree = insert(tree, 30)
    construct_graph(new_tree).write_png('Images/modified_insert_tree.png')
    new_tree = insert(new_tree, 45)
    construct_graph(new_tree).write_png('Images/modified_insert_tree.png')
    new_tree = insert(new_tree, 10)
    construct_graph(new_tree).write_png('Images/modified_insert_tree.png')
    new_tree = insert(new_tree, 60)
    construct_graph(new_tree).write_png('Images/modified_insert_tree.png')
    new_tree = insert(new_tree, 16)
    construct_graph(new_tree).write_png('Images/modified_insert_tree.png')

#printTrees()
#zigzig(tree3)
#zigzag(tree5)
#splayTest(example_tree)
#searchTestFound(example_tree)
#searchTestNotFound(example_tree)
insertTreeTest(tree2)

