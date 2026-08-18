class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Loop through all the elements
        # If we encounter a 1, check its left, right, up, and down
        # If we encounter a boundary, increase the perimeter
        # If we encounter a 0, increase the perimeter

        rows = len(grid)
        cols = len(grid[0])

        perimeter = 0

        # Check if we hit a boundary or if moving in that direction gives us a 0
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1:
                    # Go left
                    if y - 1 < 0 or grid[x][y - 1] == 0:
                        perimeter += 1

                    # Go right
                    if y + 1 >= cols or grid[x][y + 1] == 0:
                        perimeter += 1

                    # Go up
                    if x - 1 < 0 or grid[x - 1][y] == 0:
                        perimeter += 1

                    # Go down
                    if x + 1 >= rows or grid[x + 1][y] == 0:
                        perimeter += 1

        return perimeter