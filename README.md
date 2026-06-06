# 🚗 Intelligent Route Planner Using Graph Algorithms

## 📌 Project Overview

The Intelligent Route Planner is a Flask-based web application that uses Graph Algorithms to find the shortest and most efficient route between locations.

The project simulates how navigation systems such as Google Maps, Uber, Ola, Swiggy, Zomato, and logistics companies optimize routes using graph-based pathfinding algorithms.

This project demonstrates practical applications of Data Structures and Algorithms including Graphs, BFS, DFS, Dijkstra's Algorithm, Adjacency Lists, and Priority Queues.

---

## 🎯 Problem Statement

Finding the shortest path between two locations is a common problem in transportation, logistics, delivery services, and navigation systems.

This project solves that problem by:

* Representing locations as graph nodes
* Representing roads as weighted edges
* Applying graph traversal algorithms
* Using Dijkstra's Algorithm to find the shortest route
* Visualizing the transportation network

---

## ✨ Features

### Route Optimization

* Find shortest path between two locations
* Calculate total travel distance
* Route reconstruction from source to destination

### Graph Algorithms

* Breadth First Search (BFS)
* Depth First Search (DFS)
* Dijkstra's Shortest Path Algorithm

### Visualization

* Graph visualization using NetworkX
* Weighted edge display
* Transportation network simulation

### Report Generation

* Route summary generation
* Downloadable route report
* Analytics dashboard

### User Interface

* Flask Web Application
* Bootstrap Dashboard
* Interactive route selection

---

## 🧠 DSA Concepts Used

| Concept             | Usage                  |
| ------------------- | ---------------------- |
| Graph               | City Road Network      |
| Adjacency List      | Graph Storage          |
| BFS                 | Graph Traversal        |
| DFS                 | Graph Exploration      |
| Dijkstra Algorithm  | Shortest Path          |
| Priority Queue      | Efficient Route Search |
| Min Heap            | Distance Optimization  |
| Path Reconstruction | Route Generation       |

---

## ⚙️ Algorithms Used

### 1. Breadth First Search (BFS)

Used for graph traversal level by level.

Time Complexity:

```text
O(V + E)
```

---

### 2. Depth First Search (DFS)

Used for graph exploration.

Time Complexity:

```text
O(V + E)
```

---

### 3. Dijkstra's Algorithm

Used to find the shortest path between source and destination.

Time Complexity:

```text
O((V + E) log V)
```

---

## 🏗️ System Architecture

```text
User Input
     │
     ▼
Flask Web Interface
     │
     ▼
Graph Creation
     │
     ▼
Adjacency List Storage
     │
     ▼
BFS / DFS Traversal
     │
     ▼
Dijkstra Algorithm
     │
     ▼
Route Reconstruction
     │
     ▼
Route Analytics
     │
     ▼
Graph Visualization
```

---

## 📂 Project Structure

```text
Intelligent-Route-Planner-Using-Graph-Algorithms/
│
├── algorithms/
│   ├── bfs.py
│   ├── dfs.py
│   ├── dijkstra.py
│   ├── graph.py
│   └── visualize.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── images/
│       └── route_graph.png
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── outputs/
│   └── route_report.txt
│
├── images/
│   ├── homepage.png
│   ├── dashboard.png
│   ├── graph_visualization.png
│   └── route_report.png
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/Aryan-05CS/Intelligent-Route-Planner-Using-Graph-Algorithms.git
```

### Move into Project Folder

```bash
cd Intelligent-Route-Planner-Using-Graph-Algorithms
```

### Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

## 📊 Sample Output

### Input

```text
Source: Mumbai
Destination: Nagpur
```

### Shortest Route

```text
Mumbai → Pune → Aurangabad → Nagpur
```

### Distance

```text
780 km
```

---

## 📸 Screenshots

### Home Page

Add Screenshot Here

```markdown
![Home Page](images/homepage.png)
```

### Dashboard

```markdown
![Dashboard](images/dashboard.png)
```

### Graph Visualization

```markdown
![Graph](images/graph_visualization.png)
```

### Route Report

```markdown
![Report](images/route_report.png)
```

---

## 🎓 Learning Outcomes

Through this project I learned:

* Graph Data Structures
* Adjacency List Representation
* BFS Traversal
* DFS Traversal
* Dijkstra's Algorithm
* Priority Queues and Min Heaps
* Route Optimization Techniques
* Flask Web Development
* NetworkX Visualization
* Git & GitHub Workflow

---

## 🔮 Future Enhancements

* Traffic-Based Route Optimization
* A* Search Algorithm
* Multiple Route Suggestions
* Interactive Maps using Leaflet
* SQLite Search History
* Real-Time GPS Integration
* Distance and Fuel Cost Estimation

---

## 👨‍💻 Author

**Aryan Choughule**

Engineering Student | DSA Enthusiast | Python Developer | Cybersecurity Aspirant

GitHub:
https://github.com/Aryan-05CS

---

## ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the repository

📢 Share it with others

Happy Coding 🚀
