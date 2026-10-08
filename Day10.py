import logging

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(name)s:%(message)s"
)

logger = logging.getLogger(__name__)

# -------- TREE --------

tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

def dfs_tree(node):
    logger.info(f"Visited Tree Node: {node}")

    for child in tree[node]:
        dfs_tree(child)

logger.info("Tree Traversal (DFS)")
dfs_tree("A")

# -------- GRAPH --------

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

def dfs_graph(node, visited):
    visited.add(node)
    logger.info(f"Visited Graph Node: {node}")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_graph(neighbor, visited)

logger.info("Graph Traversal (DFS)")
dfs_graph("A", set())

logger.info("Practical Uses")
logger.info("Tree -> File System, Organization Chart")
logger.info("Graph -> Social Networks, Google Maps Navigation")