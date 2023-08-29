from TreeItems.SplayTree import *
from pydot_graph_util import *
import copy

# base tree
tree = SplayTree(load_tree("""{"k": 10, "l": {"k": 5, "l": null, "r": null}, "r": {"k": 15, "l": null, "r": null}}"""))
# base tree
tree2 = SplayTree(load_tree("""{"k": 15, "l": null, "r": null}"""))
# testing a full zigzig on left
tree3 = SplayTree(load_tree("""{"k": 15, "l": {"k": 10, "l": {"k": 5, "l": null, "r": null}, "r": null},"r": null}"""))
# testing a full zigzig on right
tree4 = SplayTree(load_tree("""{"k": 15, "l": null,"r": {"k": 30, "l": null, "r": {"k": 45, "l": null, "r": null}}}"""))
# Zig zag test with left right
tree5 = SplayTree(load_tree("""{"k": 30, "l": {"k": 15, "l": null, "r": {"k": 20, "l": null, "r": null}}, "r": null}"""))
tree6 = SplayTree(load_tree("""{"k": 30, "l": null, "r": {"k": 45, "l": {"k": 40, "l": null, "r": null}, "r": null}}"""))

# bigger base tree
example_tree = SplayTree(load_tree("""{"k": 30, "l": {"k": 10, "l": null, "r": null}, "r": {"k": 50, "l": null, "r": {"k": 60, "l": {"k": 55, "l": null, "r": {"k": 57, "l": null, "r": null}},"r": null}}}"""))
example_tree2 = SplayTree(load_tree("""{"k": 30, "l": {"k": 10, "l": null, "r": null}, "r": {"k": 50, "l": null, "r": {"k": 59, "l": {"k": 57, "l": {"k": 55, "l": null, "r": null}, "r": null},"r": {"k": 60, "l": null, "r": null}}}}"""))
example_tree3 = SplayTree(load_tree("""{"k": 59, "l": {"k": 57, "l": {"k": 50, "l": {"k": 30, "l": {"k": 10, "l": null, "r": null}, "r": null},"r": {"k": 55, "l": null, "r": null}}, "r": null},"r": {"k": 60, "l": null, "r": null}}"""))
example_tree4 = SplayTree(load_tree("""{"k": 30, "l": {"k": 10, "l": null, "r": null}, "r": {"k": 59, "l": {"k": 50, "l": null, "r": {"k": 57, "l": {"k": 55, "l": null, "r": null}, "r": null}},"r": {"k": 60, "l": null, "r": null}}}"""))

def printTrees():
    construct_graph(tree.root).write_png('Images/tree.png')
    construct_graph(tree2.root).write_png('Images/tree2.png')
    construct_graph(tree3.root).write_png('Images/tree3.png')
    construct_graph(tree4.root).write_png('Images/tree4.png')
    construct_graph(tree5.root).write_png('Images/tree5.png')
    construct_graph(tree6.root).write_png('Images/tree6.png')
    construct_graph(example_tree.root).write_png('Images/example_tree.png')
    construct_graph(example_tree2.root).write_png('Images/example_tree2.png')
    construct_graph(example_tree3.root).write_png('Images/example_tree3.png')
    construct_graph(example_tree4.root).write_png('Images/example_tree4.png')

def OneRotateTest():
    # three nodes only
    dupRight = copy.deepcopy(tree)
    dupLeft = copy.deepcopy(tree)

    dupRight.zig(tree.root.left)
    dupLeft.zig(tree.root.right)

    # full tree
    dupRight2 = copy.deepcopy(example_tree3)
    dupLeft2 = copy.deepcopy(example_tree3)

    dupRight2.zig(tree.root.left)
    dupLeft2.zig(tree.root.right)

printTrees()
OneRotateTest()