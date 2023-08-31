from TreeItems.SplayTree import *
from pydot_graph_util import *
import copy

# Understand that I would use more unit testing here, but it would require me to paste and play with these json strings which are already annoying to write. They're not really here for me to actually type out.
# it's much easier for me to run these functions and then compare the images that are produced using the visualizer file to an online splay tree calculator or do it by hand. I'm sure if I really wanted to I could just make the trees and then
# dump them or load them as I go, but I just wanted to do it like this. I will write at least one unit test function.

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

# gpt helped make these trees because these json strings are annoying to type out
gpt_tree = SplayTree(load_tree("""{"k": 5, "l": {"k": 3, "l": {"k": 1, "l": null, "r": null}, "r": {"k": 4, "l": null, "r": null}}, "r": {"k": 7, "l": {"k": 6, "l": null, "r": null}, "r": {"k": 8, "l": null, "r": null}}}"""))
gpt_tree2 = SplayTree(load_tree("""{"k": 5, "l": {"k": 3, "l": {"k": 1, "l": {"k": 0, "l": null, "r": null}, "r": {"k": 2, "l": null, "r": null}}, "r": {"k": 4, "l": null, "r": null}}, "r": {"k": 7, "l": {"k": 6, "l": null, "r": null}, "r": {"k": 8, "l": {"k": 9, "l": null, "r": null}, "r": null}}}"""))
gpt_tree3 = SplayTree(load_tree("""{"k": 5, "l": {"k": 3, "l": {"k": 1, "l": {"k": 0, "l": {"k": -1, "l": null, "r": null}, "r": null}, "r": {"k": 2, "l": null, "r": {"k": 2.5, "l": null, "r": null}}}, "r": {"k": 4, "l": null, "r": null}}, "r": {"k": 7, "l": {"k": 6, "l": null, "r": null}, "r": {"k": 8, "l": {"k": 9, "l": null, "r": {"k": 10, "l": null, "r": null}}, "r": null}}}"""))

def printTrees():
    construct_graph(tree.root).write_png('Images/BaseTrees/tree.png')
    construct_graph(tree2.root).write_png('Images/BaseTrees/tree2.png')
    construct_graph(tree3.root).write_png('Images/BaseTrees/tree3.png')
    construct_graph(tree4.root).write_png('Images/BaseTrees/tree4.png')
    construct_graph(tree5.root).write_png('Images/BaseTrees/tree5.png')
    construct_graph(tree6.root).write_png('Images/BaseTrees/tree6.png')
    construct_graph(example_tree.root).write_png('Images/BaseTrees/example_tree.png')
    construct_graph(example_tree2.root).write_png('Images/BaseTrees/example_tree2.png')
    construct_graph(example_tree3.root).write_png('Images/BaseTrees/example_tree3.png')
    construct_graph(example_tree4.root).write_png('Images/BaseTrees/example_tree4.png')
    construct_graph(gpt_tree.root).write_png('Images/BaseTrees/gpt1.png')
    construct_graph(gpt_tree2.root).write_png('Images/BaseTrees/gpt2.png')
    construct_graph(gpt_tree3.root).write_png('Images/BaseTrees/gpt3.png')

def zigTest():
    # three nodes only
    dupRight = copy.deepcopy(tree)
    dupLeft = copy.deepcopy(tree)

    dupRight.zig(dupRight.root.left)
    dupLeft.zig(dupLeft.root.right)

    construct_graph(dupRight.root).write_png('Images/OneRotateTest/RightThreeOnly.png')
    construct_graph(dupLeft.root).write_png('Images/OneRotateTest/LeftThreeOnly.png')

    # full tree
    dupRight2 = copy.deepcopy(example_tree3)
    dupLeft2 = copy.deepcopy(example_tree3)

    dupRight2.zig(dupRight2.root.left)
    dupLeft2.zig(dupLeft2.root.right)

    construct_graph(dupRight2.root).write_png('Images/OneRotateTest/RightFullOneRot.png')
    construct_graph(dupLeft2.root).write_png('Images/OneRotateTest/LeftFullOneRot.png')

def zigZigTest():
    # Simple trees
    simpRight = copy.deepcopy(gpt_tree)
    simpLeft = copy.deepcopy(gpt_tree)

    simpRight.zigzig(simpRight.root.left.left)
    simpLeft.zigzig(simpLeft.root.right.right)

    construct_graph(simpRight.root).write_png('Images/ZigZigTest/simpRightZI.png')
    construct_graph(simpLeft.root).write_png('Images/ZigZigTest/simpLeftZI.png')

    # Complicated or "full" trees
    compRight = copy.deepcopy(gpt_tree2)
    compLeft = copy.deepcopy(gpt_tree2)

    compRight.zigzig(compRight.root.left.left)
    compLeft.zigzig(compLeft.root.right.right)

    construct_graph(compRight.root).write_png('Images/ZigZigTest/compRightZI.png')
    construct_graph(compLeft.root).write_png('Images/ZigZigTest/compLeftZI.png')

def zigZagTest():
    # simple test cases
    simpRight = copy.deepcopy(gpt_tree)
    simpLeft = copy.deepcopy(gpt_tree)

    simpRight.zigzag(simpRight.root.left.right)
    simpLeft.zigzag(simpLeft.root.right.left)

    construct_graph(simpRight.root).write_png('Images/ZigZagTest/simpRightZA.png')
    construct_graph(simpLeft.root).write_png('Images/ZigZagTest/simpLeftZA.png')

    # fuller tree test cases
    compRight = copy.deepcopy(gpt_tree3)
    compLeft = copy.deepcopy(gpt_tree3)

    compRight.zigzag(compRight.root.left.right) # this test will see if children move proper
    compLeft.zigzag(compLeft.root.left.left.right) # this test will see if it brings it up proper

    construct_graph(compRight.root).write_png('Images/ZigZagTest/compRightZA.png')
    construct_graph(compLeft.root).write_png('Images/ZigZagTest/compLeftZA.png')

def insertTest(): # am just going to insert a ton to the tree
    tree2.insert(10)
    tree2.insert(30)
    tree2.insert(60)
    tree2.insert(35)
    tree2.insert(16)
    tree2.insert(24)
    tree2.insert(31)
    construct_graph(tree2.root).write_png('Images/InsertTest/insertTest.png')
    # insert already existing node--looking to see it splay the node but not add another
    tree2.insert(16)
    construct_graph(tree2.root).write_png('Images/InsertTest/insertTest2.png')

def deleteTest(): # am going to delete some from the previous tree
    return None

def splayTest():
    # splay existing
    # splay nonexisting
    return None

# test will work essentially as a second splay test
def searchTest():
    # search existing
    # search nonexisting (inorder predecessor/successor)
    return None

def inorderTest():
    return None

def preorderTest():
    return None

def postorderTest():
    return None


# produces all the graphs from the visualizer in the images directory.
printTrees()
#zigTest()
#zigZigTest()
#zigZagTest()
insertTest()