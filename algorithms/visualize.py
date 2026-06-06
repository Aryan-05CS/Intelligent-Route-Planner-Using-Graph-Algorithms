import networkx as nx
import matplotlib

# Prevent GUI thread issues in Flask
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import os


def create_graph_image(graph):

    G = nx.Graph()

    for node in graph:

        for neighbor, weight in graph[node]:

            G.add_edge(
                node,
                neighbor,
                weight=weight
            )

    plt.figure(figsize=(8, 6))

    pos = nx.spring_layout(
        G,
        seed=42
    )

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=2500
    )

    labels = nx.get_edge_attributes(
        G,
        "weight"
    )

    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=labels
    )

    image_dir = os.path.join(
        "static",
        "images"
    )

    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    plt.savefig(
        os.path.join(
            image_dir,
            "route_graph.png"
        )
    )

    plt.close()