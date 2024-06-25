import networkx as nx
import matplotlib.pyplot as plt

def division_graph(m):
    direction = []
    G = nx.cycle_graph(m)
    pos = nx.circular_layout(G)
    for i in range(m):
        direction.append((i*10)%m)
        G.add_edge(i,direction[i])
    nx.draw(G, pos, with_labels=True)
    plt.savefig("circular_graph.png")


# Add edges between specific nodes
#G.add_edge(1, 1)
#G.add_edge(4, 1)

# Draw the graph

# Save the figure as an image file


division_graph(10)