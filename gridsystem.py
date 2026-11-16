
from collections import deque

def bfs(grid, start, goal):

    rows = len(grid)
    cols = len(grid[0])

    queue = deque([start])
    parent = {start: None}

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        current = queue.popleft()

        if current == goal:
            break

        for dr, dc in directions:
            r = current[0] + dr
            c = current[1] + dc
            next_pos = (r, c)

            if (0 <= r < rows and 0 <= c < cols
                and grid[r][c] != '#'
                and next_pos not in parent):

                queue.append(next_pos)
                parent[next_pos] = current

    if goal not in parent:
        return None

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    return path[::-1]


# Grid environment
grid = [
    "S..#...",
    "#..#.#.",
    ".....#.",
    ".###...",
    "......G"
]

start = None
goal = None

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 'S':
            start = (r, c)
        elif grid[r][c] == 'G':
            goal = (r, c)

path = bfs(grid, start, goal)

if path is None:
    print("No path found.")

else:
    position = start
    visited = [start]

    print("Starting Position:", position)

    for next_pos in path[1:]:

        dr = next_pos[0] - position[0]
        dc = next_pos[1] - position[1]

        if dr == -1:
            action = "UP"
        elif dr == 1:
            action = "DOWN"
        elif dc == -1:
            action = "LEFT"
        else:
            action = "RIGHT"

        position = next_pos
        visited.append(position)

        print("Action:", action, "Position:", position)

    print("Goal Reached!")
    print("Total Moves:", len(path) - 1)
    print("Visited Positions:", visited)
