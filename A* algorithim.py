import heapq

goal = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)

initial = (
    (5, 1, 3),
    (4, 2, 6),
    (7, 8, 0)
)

def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)

    moves = [(-1,0), (1,0), (0,-1), (0,1)]

    for dx, dy in moves:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            temp = [list(row) for row in state]
            temp[x][y], temp[nx][ny] = temp[nx][ny], temp[x][y]
            neighbors.append(tuple(tuple(row) for row in temp))

    return neighbors

def a_star(start):
    visited = set()
    pq = []

    heapq.heappush(pq, (heuristic(start), 0, start, []))

    while pq:
        f, g, current, path = heapq.heappop(pq)

        if current == goal:
            return path + [current]

        if current in visited:
            continue

        visited.add(current)

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(neighbor)

                heapq.heappush(
                    pq,
                    (new_f, new_g, neighbor, path + [current])
                )

    return None

solution = a_star(initial)

if solution:
    print("Solution Found!\n")
    for state in solution:
        for row in state:
            print(row)
        print()
    print("Moves:", len(solution) - 1)
else:
    print("No solution found.")
