import pydot
from pydot import Dot
from pydot import Node as PydotNode
from pydot import Edge as PydotEdge

hinted = False

from TreeItems.SplayTree import Node

# Visualization helper -- honestly impressed I was able to repurpose this well
def construct_graph(root: Node) -> Dot:
    graph = Dot('my_graph', graph_type='digraph', bgcolor='black', dpi=300)
    counter = [0] # mutable int hack

    def _add_nodes(root: Node, graph: Dot, counter: list) -> None:
        if root is None:
            return graph

        label = f'{str(root.key)}'
        
        graph.add_node(PydotNode(str(root.key), shape='oval', color='white', fontcolor='white', label=label))
        if root.left is not None:
            graph.add_edge(PydotEdge(str(root.key), str(root.left.key), color='white'))
            _add_nodes(root.left, graph, counter)
        else: # add empty nodes in the empty child slots to spread out the tree
            counter[0] += 1
            none_key = f"None-{counter[0]}"
            graph.add_edge(PydotEdge(str(root.key), none_key, color='black'))
            graph.add_node(PydotNode(none_key, shape='oval', color='black', fontcolor='black'))
        if root.right is not None:
            graph.add_edge(PydotEdge(str(root.key), str(root.right.key), color='white'))
            _add_nodes(root.right, graph, counter)
        else: # add empty nodes in the empty child slots to spread out the tree
            counter[0] += 1
            none_key = f"None-{-counter[0]}"
            graph.add_edge(PydotEdge(str(root.key), none_key, color='black'))
            graph.add_node(PydotNode(none_key, shape='oval', color='black', fontcolor='black'))
        return graph

    return _add_nodes(root, graph, counter)