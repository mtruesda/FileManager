import tree
from tree import *

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

#print(dump_tree(example_tree))

#print(dump_tree(tree))

#modified_tree = zigzag(tree5.left, tree5.left.right, tree5)
#modified_tree = zigzag(tree6.right, tree6.right.left, tree6)
#print(dump_tree(modified_tree))

#print(search(example_tree, 62))
#modified_tree = splay(tree3, 10)

testEmptyTree = None

modTree = insert(testEmptyTree,30)
modTree = insert(modTree, 10)
modTree = insert(modTree, 40)
modTree = insert(modTree, 35)
modTree = insert(modTree, 36)

print(dump_tree(modTree))