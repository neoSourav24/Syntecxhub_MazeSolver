# Syntecxhub_MazeSolver
Maze Solver using A* Search

# 🧩 Maze Solver AI (A* Search Algorithm)

This project is a Python-based implementation of the **A* Search Algorithm** to solve a grid-based maze. It models the environment as nodes, utilizes heuristics for efficiency, and handles unreachable scenarios gracefully.


## 📋 Project Requirements 
As per the project guidelines:
* **Node Modeling**: Represents a maze/grid consisting of a start point, a goal, and walls modeled as searchable nodes.
* **A* Implementation**: Utilizes the A* search algorithm combined with a heuristic.
* **Heuristic Functions**: Supports **Manhattan Distance** ($|x1 - x2| + |y1 - y2|$) for grid-based movement.
* **Shortest Path**: Guaranteed to return the most efficient route from start to goal.
* **Unreachable Cases**: Built-in logic to detect and report when a goal is inaccessible due to wall placement.
* **Visualization**: Provides a clear console-based visual representation of the search results and the final path.



## 🧠 How it Works
The A* algorithm evaluates nodes using the following formula:
$$f(n) = g(n) + h(n)$$

* **$g(n)$**: The actual cost from the start node to the current node $n$.
* **$h(n)$**: The estimated cost (heuristic) from node $n$ to the goal.
* **$f(n)$**: The total estimated cost of the path through node $n$.

## 🚀 Setup and Execution
1. Ensure the `src/` folder containing `maze_logic.py` and `utils.py` is in the same directory as `main.py`.
2. Run the program using:
   ```bash
   python main.py
