from flask import Flask, render_template, request, send_file
import os

from algorithms.graph import Graph
from algorithms.dijkstra import shortest_path
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.visualize import create_graph_image

app = Flask(__name__)

# =====================================
# CITY GRAPH DATASET
# =====================================

city = Graph()

city.add_edge("Mumbai", "Pune", 150)
city.add_edge("Mumbai", "Nashik", 165)

city.add_edge("Pune", "Satara", 110)
city.add_edge("Pune", "Aurangabad", 230)

city.add_edge("Satara", "Kolhapur", 120)

city.add_edge("Nashik", "Aurangabad", 180)
city.add_edge("Nashik", "Jalgaon", 160)

city.add_edge("Aurangabad", "Nagpur", 400)

city.add_edge("Jalgaon", "Amravati", 280)

city.add_edge("Amravati", "Nagpur", 150)

locations = sorted(city.graph.keys())


# =====================================
# HOME PAGE
# =====================================

@app.route("/")
def home():

    return render_template(
        "index.html",
        locations=locations
    )


# =====================================
# ROUTE CALCULATION
# =====================================

@app.route("/route", methods=["POST"])
def route():

    source = request.form["source"]
    destination = request.form["destination"]

    # Shortest Path
    path, distance = shortest_path(
        city.graph,
        source,
        destination
    )

    # BFS Traversal
    bfs_result = bfs(
        city.graph,
        source
    )

    # DFS Traversal
    dfs_result = dfs(
        city.graph,
        source
    )

    # Analytics
    node_count = len(path)

    # Graph Visualization
    create_graph_image(
        city.graph
    )

    # Create Output Folder
    os.makedirs(
        "outputs",
        exist_ok=True
    )

    # Route Report
    with open(
        "outputs/route_report.txt",
        "w",
        encoding="utf-8"
    ) as report:

        report.write(
            "INTELLIGENT ROUTE PLANNER REPORT\n"
        )

        report.write(
            "=" * 50 + "\n\n"
        )

        report.write(
            f"Source: {source}\n"
        )

        report.write(
            f"Destination: {destination}\n\n"
        )

        report.write(
            "Shortest Route:\n"
        )

        report.write(
            " -> ".join(path)
        )

        report.write(
            f"\n\nTotal Distance: {distance} km\n\n"
        )

        report.write(
            "BFS Traversal:\n"
        )

        report.write(
            " -> ".join(bfs_result)
        )

        report.write(
            "\n\nDFS Traversal:\n"
        )

        report.write(
            " -> ".join(dfs_result)
        )

    return render_template(
        "result.html",
        path=path,
        distance=distance,
        bfs_result=bfs_result,
        dfs_result=dfs_result,
        node_count=node_count
    )

@app.route("/download-report")
def download_report():

    return send_file(
        "outputs/route_report.txt",
        as_attachment=True
    )


# =====================================
# RUN APPLICATION
# =====================================

if __name__ == "__main__":
    app.run(
        debug=True
    )

