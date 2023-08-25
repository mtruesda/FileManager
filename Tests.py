from TreeItems.SplayTree import *
from pydot_graph_util import *
import copy

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

example_tree2 = load_tree("""{"k": 30, "l": {"k": 10, "l": null, "r": null}, 
                                      "r": {"k": 50, "l": null, 
                                                     "r": {"k": 59, 
                                                                   "l": {"k": 57, "l": {"k": 55, "l": null, "r": null}, 
                                                                                  "r": null},
                                                                   "r": {"k": 60, "l": null, "r": null}}}}""")

example_tree3 = load_tree("""{"k": 59, 
                                    "l": {"k": 57, 
                                                "l": {"k": 50, 
                                                            "l": {"k": 30, 
                                                                        "l": {"k": 10, "l": null, "r": null}, 
                                                                        "r": null},
                                                            "r": {"k": 55, "l": null, "r": null}
                                                }, 
                                                "r": null},
                                    "r": {"k": 60, "l": null, "r": null}
                            }
                        """)

example_tree4 = load_tree("""{"k": 30, "l": {"k": 10, "l": null, "r": null}, 
                                "r": {"k": 59, 
                                   "l": {"k": 50, "l": null, "r": {"k": 57, "l": {"k": 55, "l": null, "r": null}, "r": null}},
                                   "r": {"k": 60, "l": null, "r": null}}
                          }""")


def printTrees():
    construct_graph(tree).write_png('Images/tree.png')
    construct_graph(tree2).write_png('Images/tree2.png')
    construct_graph(tree3).write_png('Images/tree3.png')
    construct_graph(tree4).write_png('Images/tree4.png')
    construct_graph(tree5).write_png('Images/tree5.png')
    construct_graph(tree6).write_png('Images/tree6.png')
    construct_graph(example_tree).write_png('Images/example_tree.png')
    construct_graph(example_tree2).write_png('Images/example_tree2.png')
    construct_graph(example_tree3).write_png('Images/example_tree3.png')
    construct_graph(example_tree4).write_png('Images/example_tree4.png')

def zigzig(tree):
    tree3 = right_zigzig(tree)
    construct_graph(tree3).write_png('Images/modified_tree3.png')
    tree3 = left_zigzig(tree3)
    construct_graph(tree3).write_png('Images/modified_tree3_2.png')

def zigzag(tree):
    new_tree = left_zigzag(tree)
    construct_graph(new_tree).write_png('Images/modified_tree5.png')

def zigzag2(tree):
    new_tree = right_zigzag(tree)
    construct_graph(new_tree).write_png('Images/modified_tree6.png')

def splayTest(tree):
    test_tree = splay(tree, 57)
    construct_graph(test_tree).write_png('Images/modified_example_tree.png')

def searchTestFound(tree):
    new_tree = search(tree, 60)
    construct_graph(tree).write_png('Images/modified_search.png')

def searchTestNotFound(tree):
    new_tree = search(tree, 59)
    print(new_tree.key)
    construct_graph(new_tree).write_png('Images/modified_search_nf.png')

def insertTreeTest(tree):
    new_tree = insertBST(tree, 30)
    new_tree = insertBST(new_tree, 45)
    new_tree = insertBST(new_tree, 10)
    new_tree = insertBST(new_tree, 60)
    new_tree = insertBST(new_tree, 16)
    new_tree = insertBST(new_tree, 40)
    new_tree = insertBST(new_tree, 35)

    construct_graph(new_tree).write_png('Images/modified_insert_tree.png')

def insertTreeTest2(tree):
    new_tree = insertAfter(tree, 30)
    new_tree = insertAfter(new_tree, 45)
    new_tree = insertAfter(new_tree, 10)
    new_tree = insertAfter(new_tree, 60)
    new_tree = insertAfter(new_tree, 16)
    construct_graph(new_tree).write_png('Images/old_insert_tree.png')

def insertTreeTest3():
    new_tree = copy.deepcopy(tree2)
    new_tree = insertAfter(new_tree, 30)
    new_tree = insertAfter(new_tree, 45)
    new_tree = insertAfter(new_tree, 10)
    new_tree = insertAfter(new_tree, 60)
    new_tree = insertAfter(new_tree, 16)
    construct_graph(new_tree).write_png('Images/insert_tree_3.png')

def insertTreeTest4():
    new_tree = copy.deepcopy(tree2)
    new_tree = insertBST(new_tree, 30)
    new_tree = insertBST(new_tree, 45)
    new_tree = insertBST(new_tree, 10)
    new_tree = insertBST(new_tree, 60)
    new_tree = insertBST(new_tree, 16)
    construct_graph(new_tree).write_png('Images/insert_tree_4.png')

def deleteTreeTest():
    modded_tree = copy.deepcopy(example_tree3)
    print_tree = copy.deepcopy(example_tree3)
    construct_graph(splay(print_tree, 30)).write_png('Images/checker.png')
    modded_tree = delete(modded_tree, 30)
    construct_graph(modded_tree).write_png('Images/delete_tree.png')

def newerSplayTest():
    tree1_ = copy.deepcopy(tree)
    tree2_ = copy.deepcopy(tree3)
    tree3_ = copy.deepcopy(tree6)

    tree1_ = splay(tree1_, 5)
    tree2_ = splay(tree2_, 5)
    tree3_ = splay(tree3_, 40)

    construct_graph(tree1_).write_png('Images/splayTree1.png')
    construct_graph(tree2_).write_png('Images/splayTree2.png')
    construct_graph(tree3_).write_png('Images/splayTree3.png')

printTrees()
#zigzig(tree3)
#zigzag(tree5)
#zigzag2(tree6)
#splayTest(example_tree)
#searchTestFound(example_tree)
#searchTestNotFound(example_tree)
insertTreeTest(tree2)
#insertTreeTest2(tree2)
#insertTreeTest3() # compare result with following line
#insertTreeTest4()
#deleteTreeTest()
#newerSplayTest()
