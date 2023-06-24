import tree, pydot_graph_util, pydot_graph_viz
from tree import *

tree = load_tree("""{"k": 10, "l": {"k": 5, "l": null, "r": null}, "r": {"k": 15, "l": null, "r": null}}""")

example_tree = load_tree("""{"k": 30, "l": {"k": 10, "l": null, "r": null}, 
                                      "r": {"k": 50, "l": null, 
                                                     "r": {"k": 60, 
                                                                   "l": {"k": 55, "l": null, "r": null},
                                                                   "r": null}}}""")

print(dump_tree(example_tree))

print(dump_tree(tree))

tree = zig(tree, tree.right)

print(dump_tree(tree))

construct_tree(tree)