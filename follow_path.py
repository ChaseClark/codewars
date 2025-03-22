# trying dfs version of FollowPath

height = 10
width = 15
target = []
grid = []
directions = []

directions.append((1, 0))  # right
directions.append((-1, 0))  # left
directions.append((0, -1))  # up
directions.append((0, 1))  # down

grid.append(["*", "*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "])
grid.append([" ", "h", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "])
grid.append([" ", "e", "*", "l", "*", "*", "r", "l", "d", "*", " ", " ", " ", " ", " "])
grid.append([" ", " ", " ", "*", "*", " ", " ", " ", " ", "*", " ", " ", " ", " ", " "])
grid.append([" ", " ", " ", "l", "*", " ", " ", " ", " ", "!", " ", " ", " ", " ", " "])
grid.append([" ", " ", " ", "o", "o", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "])
grid.append([" ", " ", " ", "*", "w", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "])
grid.append([" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "])
grid.append([" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "])


def dfs_util(position, visited):
    visited.add(f"x:{position[0]} y:{position[1]}")
    print(f"visiting: {position}")

    for dir in directions:
        # see if next position has possible value and has not been processed
        next = list(position)
        next[0] += dir[0]  # x
        next[1] += dir[1]  # y
        if f"x:{next[0]} y:{next[1]}" not in visited:
            # check bounds
            if (next[0] >= 0 and next[0] < width) and (
                next[1] >= 0 and next[1] < height
            ):
                # see if next is not a blank string
                char = grid[next[0]][next[1]]
                if char is not " ":
                    if char is not "*":
                        target.append(char)
                    dfs_util(next, visited)


def dfs(position):
    visited = set()
    dfs_util(position, visited)


dfs([0, 0])
print(f"ans: {''.join(target)}")
