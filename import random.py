import random
import copy

def karger_min_cut(graph):
    min_cut = float('inf')
    num_iterations = 200  # Increase this for higher probability of finding the minimum cut
    
    for _ in range(num_iterations):
        local_graph = copy.deepcopy(graph)
        cut_value = karger_contraction(local_graph)
        min_cut = min(min_cut, cut_value)
    
    return min_cut

def karger_contraction(graph):
    while len(graph) > 2:
        u = random.choice(list(graph.keys()))
        v = random.choice(graph[u])
        
        # Merge v into u and remove v from the graph
        graph[u].extend(graph[v])
        for vertex in graph[v]:
            graph[vertex].remove(v)
            if vertex != u:
                graph[vertex].append(u)
        while u in graph[u]:
            graph[u].remove(u)
        
        del graph[v]
    
    # The remaining graph has two nodes, return the cut size
    remaining_nodes = list(graph.keys())
    return len(graph[remaining_nodes[0]])

# Load the graph from the file
def load_graph(file_path):
    graph = {}
    with open(file_path, 'r') as f:
        for line in f:
            parts = list(map(int, line.strip().split()))
            graph[parts[0]] = parts[1:]
    return graph

# File path to the adjacency list
file_path = '/Users/yiningqu/Desktop/_f370cd8b4d3482c940e4a57f489a200b_kargerMinCut.txt'

# Load the graph
graph = load_graph(file_path)

# Compute the min cut
min_cut = karger_min_cut(graph)
print(f"The minimum cut is: {min_cut}")
