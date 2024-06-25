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
    nx.draw(G, pos, with_labels=True)
    plt.savefig(f"./nt/graph_img/{m}.png")
    plt.clf()
    plt.close()


for i in primes:
   division_graph(i)

