def draw_maze(maze, path=None, start=None, goal=None):
    for y, row in enumerate(maze):
        line = ""
        for x, cell in enumerate(row):
            if (x, y) == start: line += "🏁 "
            elif (x, y) == goal: line += "🎯 "
            elif path and (x, y) in path: line += "🔹 "
            elif cell == 1: line += "██ "
            else: line += "░░ "
        print(line)