# Trees and Graphs - Beginner Example

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
    print(node, end=" ")
    for child in tree[node]:
        dfs_tree(child)

print("Tree Traversal (DFS):")
dfs_tree("A")

print("\n")

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
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_graph(neighbor, visited)

print("Graph Traversal (DFS):")
dfs_graph("A", set())

print("\n")

print("Practical Uses:")
print("Tree -> File System, Organization Chart")
print("Graph -> Social Networks, Google Maps Navigation")