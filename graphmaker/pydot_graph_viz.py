import pydot
from pydot import Dot
from pydot import Node as PydotNode
from pydot import Edge as PydotEdge

from tree import Node

# Visualization helper
def construct_graph(root: Node) -> Dot:
    """Construct a pydot graph object via a preorder traversal and return the graph.
       This is just some code cobbled together after browsing the pydot+GraphViz docs
       as well as some helpful stackoverflow posts. It's set up to lay things out 
       reasonably nicely for the small trees you might debug with."""
    graph = Dot('my_graph', graph_type='digraph', bgcolor='black', dpi=300)

    def _add_nodes(root: Node, graph: Dot) -> None:
        if root is None:
            return graph

        raise NotImplementedError
        label = f"" # FIXME Need a description of the node's contents
        node_id = f"" # FIXME unique and hashable, maybe str(keys and vals)?

        graph.add_node(PydotNode(node_id, shape='oval', color='white', fontcolor='white', label=label))

        for child in root.children:
            if child is not None:
                child_id = f"" # FIXME unique and hashable, maybe str(keys and vals)?
                graph.add_edge(PydotEdge(node_id, child_id, color='white'))
                _add_nodes(child, graph)

        return graph

    return _add_nodes(root, graph)