from collections import defaultdict

def perform_dfs(edges, start_point, is_directed=True):
    # Create an adjacency map from the edges
    adjacency_map = defaultdict(list)
    for origin, destination in edges:
        adjacency_map[origin].append(destination)
        if not is_directed:
            adjacency_map[destination].append(origin)  # Add reverse edge for undirected graphs

    seen = set()  # Tracks visited nodes
    traversal_order = []  # Stores the order of traversal
    cycle_detected = False  # Flag to check for cycles

    def traverse(node, ancestors):
        """Recursive DFS traversal."""
        nonlocal cycle_detected
        if node not in seen:
            seen.add(node)
            traversal_order.append(node)
            ancestors.add(node)  # Add current node to recursion stack
            for adjacent in adjacency_map[node]:
                if adjacent not in seen:
                    traverse(adjacent, ancestors)
                elif adjacent in ancestors:
                    cycle_detected = True  # Cycle detected (back edge in directed graph)
            ancestors.remove(node)  # Remove node from recursion stack
        return

    if start_point not in adjacency_map:
        print(f"Error: Start point '{start_point}' not found in the graph.")
        return

    # Start DFS from the given start point
    traverse(start_point, set())

    # Check for disconnected nodes
    all_nodes = set(adjacency_map.keys())
    unvisited_nodes = all_nodes - seen

    # Output the traversal
    print(f"DFS Traversal Order from '{start_point}': {' -> '.join(traversal_order)}")
    if cycle_detected:
        print("Cycle detected in the graph.")
    else:
        print("No cycles detected in the graph.")

    # Warn if there are disconnected components
    if unvisited_nodes:
        print(f"Warning: The graph has disconnected nodes: {', '.join(unvisited_nodes)}")

# Example Usage
example_edges = [
    ("u", "v"),
    ("u", "x"),
    ("v", "y"),
    ("y", "x"),
    ("x", "v"),
    ("w", "z"),
    ("w", "y"),
    ("z", "z")  # self-loop
]

print("Depth-First Search from 'u':")
perform_dfs(example_edges, 'u', is_directed=True)  # Specify if the graph is directed or undirected
