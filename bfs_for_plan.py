from collections import deque

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

queue = deque([start])
visited = {start}

while queue:
    state = queue.popleft()

    if state == goal:
        print("Goal Reached!")
        print(state)
        break

    pos = state.index(0)

    for move in [-3, 3, -1, 1]:
        new = pos + move

        if 0 <= new < 9 and not (
            (move == -1 and pos % 3 == 0) or
            (move == 1 and pos % 3 == 2)
        ):
            new_state = list(state)

            new_state[pos], new_state[new] = new_state[new], new_state[pos]

            new_state = tuple(new_state)

            if new_state not in visited:
                visited.add(new_state)
                queue.append(new_state)

