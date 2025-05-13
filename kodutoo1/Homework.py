import time
from queue import Queue, PriorityQueue


# Heuristic function (Manhattan Distance)
def h(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


# BFS Algorithm
def bfs(map_data, start, goal):
    frontier = Queue()
    frontier.put(start)
    came_from = {start: None}
    iterations = 0

    while not frontier.empty():
        current = frontier.get()
        iterations += 1

        if current == goal:
            break

        for next in neighbors(map_data, current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current

    path = reconstruct_path(came_from, start, goal)
    return path, iterations


# Greedy Search Algorithm
def greedy(map_data, start, goal):
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {start: None}
    iterations = 0

    while not frontier.empty():
        _, current = frontier.get()
        iterations += 1

        if current == goal:
            break

        for next in neighbors(map_data, current):
            if next not in came_from:
                priority = h(next, goal)
                frontier.put((priority, next))
                came_from[next] = current

    path = reconstruct_path(came_from, start, goal)
    return path, iterations


# A* Algorithm
def astar(map_data, start, goal):
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}
    iterations = 0

    while not frontier.empty():
        _, current = frontier.get()
        iterations += 1

        if current == goal:
            break

        for next in neighbors(map_data, current):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + h(next, goal)
                frontier.put((priority, next))
                came_from[next] = current

    path = reconstruct_path(came_from, start, goal)
    return path, iterations


# Neighbors function to get valid neighboring cells
def neighbors(map_data, current):
    rows = len(map_data)
    cols = len(map_data[0])
    row, col = current
    candidates = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    result = []

    for r, c in candidates:
        if 0 <= r < rows and 0 <= c < cols and map_data[r][c] != '*':
            result.append((r, c))

    return result


# Reconstruct the path from start to goal
def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path


# Main function to test the algorithms
def run_experiments(map_data, start, goal):
    # BFS
    start_time = time.time()
    path, iterations = bfs(map_data, start, goal)
    bfs_time = time.time() - start_time
    print(f"BFS - Iterations: {iterations}, Time: {bfs_time:.4f}s, Path length: {len(path)}")

    # Greedy Search
    start_time = time.time()
    path, iterations = greedy(map_data, start, goal)
    greedy_time = time.time() - start_time
    print(f"Greedy - Iterations: {iterations}, Time: {greedy_time:.4f}s, Path length: {len(path)}")

    # A*
    start_time = time.time()
    path, iterations = astar(map_data, start, goal)
    astar_time = time.time() - start_time
    print(f"A* - Iterations: {iterations}, Time: {astar_time:.4f}s, Path length: {len(path)}")


lava_map1 = [
    "      **               **      ",
    "     ***     D        ***      ",
    "     ***                       ",
    "                      *****    ",
    "           ****      ********  ",
    "           ***          *******",
    " **                      ******",
    "*****             ****     *** ",
    "*****              **          ",
    "***                            ",
    "              **         ******",
    "**            ***       *******",
    "***                      ***** ",
    "                               ",
    "                s              ",
]

lava_map2 = [
    "     **********************    ",
    "   *******   D    **********   ",
    "   *******                     ",
    " ****************    **********",
    "***********          ********  ",
    "            *******************",
    " ********    ******************",
    "********                   ****",
    "*****       ************       ",
    "***               *********    ",
    "*      ******      ************",
    "*****************       *******",
    "***      ****            ***** ",
    "                               ",
    "                s              ",
]
with open("cave300x300") as f:
    map_data1 = [l.strip() for l in f.readlines() if len(l)>1]

with open("cave600x600") as f:
    map_data2 = [l.strip() for l in f.readlines() if len(l)>1]

with open("cave900x900") as f:
    map_data3 = [l.strip() for l in f.readlines() if len(l)>1]

start_row, start_col = 14, 16
goal_row1, goal_col1 = 1, 18
goal_row2, goal_col2 = 1, 12

run_experiments(lava_map1, (start_row, start_col), (goal_row1, goal_col1))
run_experiments(lava_map2, (start_row, start_col), (goal_row2, goal_col2))

start_row1, start_col1 = 2, 2
goal_rows, goal_cols = 295, 257
goal_rows1, goal_cols1 = 598, 595
goal_rows2, goal_cols2 = 898, 895

print("Testing on cave300x300")
run_experiments(map_data1, (start_row1, start_col1), (goal_rows, goal_cols))
print("Testing on cave600x600")
run_experiments(map_data2, (start_row1, start_col1), (goal_rows1, goal_cols1))
print("Testing on cave900x900")
run_experiments(map_data3,(start_row1, start_col1), (goal_rows2, goal_cols2))