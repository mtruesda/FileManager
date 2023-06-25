import pydot
from pydot import Dot
from pydot import Node as PydotNode
from pydot import Edge as PydotEdge

hinted = False

from tree import Node, LineOfText
import tree

# Visualization helper
def construct_graph(root: Node) -> Dot:
    """Construct a pydot graph object via a preorder traversal and return the graph.
       This is just some code cobbled together after browsing the pydot+GraphViz docs
       as well as some helpful stackoverflow posts. It's set up to lay things out 
       reasonably nicely for the small trees you might debug with."""
    graph = Dot('my_graph', graph_type='digraph', bgcolor='black', dpi=300)
    counter = [0] # mutable int hack

    def _add_nodes(root: Node, graph: Dot, counter: list) -> None:
        if root is None:
            return graph

        if not (isinstance(root.key, int) or isinstance(root.key, LineOfText)):
            raise TypeError(f"Unknown type {type(root.key)} for node keys.")

        if tree.balance(root) is not None:
            label = f'{str(root.key)} | {tree.height(root)} | {tree.balance(root)}'
        else:
            global hinted
            if not hinted:
                print("Hint: it will probably be helpful to define functions in tree.py for getting the height of a node and its balance factor!")
                hinted = True
            label = f'{str(root.key)}'
        
        graph.add_node(PydotNode(str(root.key), shape='oval', color='white', fontcolor='white', label=label))
        if root.leftchild is not None:
            graph.add_edge(PydotEdge(str(root.key), str(root.leftchild.key), color='white'))
            _add_nodes(root.leftchild, graph, counter)
        else: # add empty nodes in the empty child slots to spread out the tree
            counter[0] += 1
            none_key = f"None-{counter[0]}"
            graph.add_edge(PydotEdge(str(root.key), none_key, color='black'))
            graph.add_node(PydotNode(none_key, shape='oval', color='black', fontcolor='black'))
        if root.rightchild is not None:
            graph.add_edge(PydotEdge(str(root.key), str(root.rightchild.key), color='white'))
            _add_nodes(root.rightchild, graph, counter)
        else: # add empty nodes in the empty child slots to spread out the tree
            counter[0] += 1
            none_key = f"None-{-counter[0]}"
            graph.add_edge(PydotEdge(str(root.key), none_key, color='black'))
            graph.add_node(PydotNode(none_key, shape='oval', color='black', fontcolor='black'))
        return graph

    return _add_nodes(root, graph, counter)