import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Distance from start
        self.h = 0  # Heuristic (Estimate to goal)
        self.f = 0  # Total cost (g + h)

    def __lt__(self, other):
        return self.f < other.f

def get_heuristic(p1, p2):
    # Manhattan distance: |x1 - x2| + |y1 - y2|
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def a_star(maze, start, goal):
    start_node = Node(start)
    goal_node = Node(goal)
    
    open_list = []
    closed_set = set()
    
    heapq.heappush(open_list, start_node)
    
    while open_list:
        current_node = heapq.heappop(open_list)
        
        # Found the goal
        if current_node.position == goal_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1] # Return shortest path
        
        closed_set.add(current_node.position)
        
        # Neighbors: Up, Down, Left, Right
        for move in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            node_pos = (current_node.position[0] + move[0], current_node.position[1] + move[1])
            
            # Check boundaries and walls (1 = wall, 0 = path)
            if (0 <= node_pos[1] < len(maze)) and (0 <= node_pos[0] < len(maze[0])):
                if maze[node_pos[1]][node_pos[0]] == 1 or node_pos in closed_set:
                    continue
                
                neighbor = Node(node_pos, current_node)
                neighbor.g = current_node.g + 1
                neighbor.h = get_heuristic(neighbor.position, goal_node.position)
                neighbor.f = neighbor.g + neighbor.h
                
                # If neighbor is already in open_list with a better g, skip
                if any(open_node.position == neighbor.position and neighbor.g >= open_node.g for open_node in open_list):
                    continue
                    
                heapq.heappush(open_list, neighbor)
                
    return None # HANDLE UNREACHABLE CASE: Return None if no path found