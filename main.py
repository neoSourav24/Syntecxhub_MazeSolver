import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.maze_logic import a_star
from src.utils import draw_maze

# Example Maze (0 = path, 1 = wall)
maze_grid = [
    [0, 0, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0]
]

def main():
    print("=== A* Maze Solver Project ===")
    draw_maze(maze_grid)
    
    try:
        start_x = int(input("\nEnter Start X (0-5): ") or 0)
        start_y = int(input("Enter Start Y (0-4): ") or 0)
        goal_x = int(input("Enter Goal X (0-5): ") or 5)
        goal_y = int(input("Enter Goal Y (0-4): ") or 4)
        
        start = (start_x, start_y)
        goal = (goal_x, goal_y)
        
        print("\nSearching for shortest path...")
        path = a_star(maze_grid, start, goal)
        
        if path:
            print(f"✅ Path Found! Length: {len(path)} steps.")
            draw_maze(maze_grid, path, start, goal)
        else:
            print("🚨 UNREACHABLE CASE: No path exists between those points.")
            draw_maze(maze_grid, start=start, goal=goal)
            
    except ValueError:
        print("Invalid input. Please enter numbers.")

if __name__ == "__main__":
    main()