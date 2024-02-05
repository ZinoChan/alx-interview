from typing import List


def islandPerimeter(grid: List[List[int]]) -> int:
    row, column = len(grid), len(grid[0])
    perimeter = 0
    for i in range(row):
        for j in range(column):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2
    return perimeter
