import networkx as nx
import matplotlib.pyplot as plt

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def division_graph(m):
    direction = []
    G = nx.empty_graph(m)
    pos = nx.circular_layout(G)
    for i in range(m):
        direction.append((i*10)%m)
        G.add_edge(i,direction[i])
    plt.figure(figsize=(30, 30))
    nx.draw(G, pos, with_labels=True,node_size=2000)
    #plt.savefig(f"./nt/graph_img/{m}.png")
    plt.savefig(f"circular_graph.png")
    plt.clf()
    plt.close()


division_graph(6)