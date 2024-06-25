import networkx as nx
import matplotlib.pyplot as plt

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def division_graph(m,p):
    direction = []
    G = nx.DiGraph()  # Create a directed graph
    G.add_nodes_from(range(m))
    pos = nx.circular_layout(G)
    for i in range(m):
        direction.append((i * p) % m)
        G.add_edge(i, direction[i])
    
    plt.figure(figsize=(10, 10))  # Adjust figure size
    
    # Draw nodes, edges, and labels separately
    nx.draw_networkx_nodes(
        G, pos, 
        node_size=500, 
        node_color='lightblue', 
        edgecolors='black', 
        linewidths=1
    )
    nx.draw_networkx_edges(
        G, pos, 
        edge_color='gray', 
        arrows=True, 
        arrowstyle='-|>', 
        arrowsize=20
    )
    nx.draw_networkx_labels(
        G, pos, 
        font_size=10, 
        font_color='black', 
        font_weight='bold'
    )
    
    plt.savefig(f"./nt/index/{p}.png")
    plt.clf()
    plt.close()

division_graph(7,7)