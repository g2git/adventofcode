from collections import defaultdict
from itertools import combinations
import networkx as nx

# Function to find all groups of 3
def connect_tuples_to_triples(tuples):
    # Dictionary to store connections
    connections = defaultdict(set)

    # Fill the dictionary with pairs of connected elements
    for a, b in tuples:
        connections[a].add(b)
        connections[b].add(a)

    # Set to store the result triples (avoid duplicates)
    triples = set()

    # Iterate through all the elements and find possible triples
    for a in connections:
        for b in connections[a]:
            if b > a:  # to avoid revisiting the same pairs
                for c in connections[b]:
                    if c > b and c in connections[a]:  # Check if a, b, c are all connected
                        triples.add(tuple(sorted([a, b, c])))

    return list(triples)

def count_elements_that_start_with(triples, char):
    count = 0

    # Loop through each triple
    for triple in triples:
        # Check if the element starts with 't' (case-insensitive)
        if any(element.lower().startswith(char) for element in triple):
            count += 1
    
    return count


# Function to find all connected components using DFS
def find_connected_groups(tuples):
    # Create a dictionary to store connections between elements
    connections = defaultdict(set)

    # Populate the connections dictionary with each tuple
    for a, b in tuples:
        connections[a].add(b)
        connections[b].add(a)

    # Set to store the result groups (to avoid duplicates)
    groups = []
    visited = set()  # To keep track of already processed elements

    # Function to perform DFS and gather all connected elements in a group
    def dfs(element, group):
        if element not in visited:
            visited.add(element)
            group.append(element)
            for neighbor in connections[element]:
                dfs(neighbor, group)

    # Iterate through each element and apply DFS if it has not been visited
    for element in connections:
        if element not in visited:
            group = []
            dfs(element, group)
            groups.append(tuple(sorted(group)))  # Sort to handle order-free results

    return groups


# Function to build an adjacency graph from the list of tuples
def build_graph(tuples):
    graph = defaultdict(set)
    for a, b in tuples:
        graph[a].add(b)
        graph[b].add(a)
    return graph

# Function to check if all pairs in a list of elements are connected
def all_connected(graph, component):
    for i in range(len(component)):
        for j in range(i + 1, len(component)):
            if component[j] not in graph[component[i]]:
                return False
    return True

# Function to connect tuples and expand groups
def connect_elements(tuples):
    graph = build_graph(tuples)  # Build the graph from tuples
    elements = set([item for pair in tuples for item in pair])  # Get all unique elements

    result = []  # To store the connected groups (tuples)
    
    # Try expanding groups from size 2 up to the size of the largest group
    for size in range(2, len(elements) + 1):
        for component in combinations(elements, size):
            # If the current component is fully connected, add it to the result
            if all_connected(graph, component):
                result.append(tuple(sorted(component)))  # Sorting for consistency
    
    return result


with open('23-LANparty.txt') as file:
    triples = []
    tuples = []
    for line in file:
        tuples.append((tuple(line.strip().split('-'))))
    triples = connect_tuples_to_triples(tuples)
    # print(count_elements_that_start_with(triples, "t"))
    
    # Create a graph
    G = nx.Graph()
    # Add edges (which implicitly adds nodes)
    G.add_edges_from(tuples)

    # Get the list of all cliques
    cliques = list(nx.find_cliques(G))
    print(cliques)
    
    # Find the row with the largest length
    largest_row = ','.join(sorted(max(cliques, key=lambda row: len(row))))
    print(f"The largest row is: {largest_row}")