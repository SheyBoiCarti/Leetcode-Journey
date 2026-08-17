class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        rows = len(matrix)
        cols = len(matrix[0])

        boundaryx = rows - 1
        boundaryy = cols - 1

        result = [0] * (rows * cols)
        index = 0
        result[index] = matrix[0][0]

        visited = [[False] * cols for j in range(rows)]
        visited[0][0] = True

        direction = "right"

        def movearound(matrix, x, y):
            nonlocal index, direction

            if index == rows * cols - 1:
                return None

            # right
            if direction == "right":
                if y + 1 <= boundaryy and visited[x][y + 1] == False:
                    visited[x][y + 1] = True
                    index += 1
                    result[index] = matrix[x][y + 1]
                    movearound(matrix, x, y + 1)
                else:
                    direction = "down"
                    movearound(matrix, x, y)

            # down
            elif direction == "down":
                if x + 1 <= boundaryx and visited[x + 1][y] == False:
                    visited[x + 1][y] = True
                    index += 1
                    result[index] = matrix[x + 1][y]
                    movearound(matrix, x + 1, y)
                else:
                    direction = "left"
                    movearound(matrix, x, y)

            # left
            elif direction == "left":
                if y - 1 >= 0 and visited[x][y - 1] == False:
                    visited[x][y - 1] = True
                    index += 1
                    result[index] = matrix[x][y - 1]
                    movearound(matrix, x, y - 1)
                else:
                    direction = "up"
                    movearound(matrix, x, y)

            # up
            elif direction == "up":
                if x - 1 >= 0 and visited[x - 1][y] == False:
                    visited[x - 1][y] = True
                    index += 1
                    result[index] = matrix[x - 1][y]
                    movearound(matrix, x - 1, y)
                else:
                    direction = "right"
                    movearound(matrix, x, y)

            return None

        movearound(matrix, 0, 0)

        return result