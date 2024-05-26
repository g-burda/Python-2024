





import networkx as nx
import matplotlib.pyplot as plt
import random

num_nodes = 7
G = nx.Graph()

G.add_nodes_from(range(num_nodes))

for u in G.nodes():
    for v in G.nodes():
        if u != v:
            probability = 0.3
            if random.random() < probability:
                G.add_edge(u, v)
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='orange', edge_color='red', node_size=300, font_size=15)
plt.title("Random Undirected Graph")
plt.show()
