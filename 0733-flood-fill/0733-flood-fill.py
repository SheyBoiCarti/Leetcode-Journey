class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        rows = len(image)
        cols = len(image[0])

        old_color = image[sr][sc]

        if old_color == color:
            return image

        def floodFill(x, y):

            # out of bounds
            if x < 0 or x >= rows or y < 0 or y >= cols:
                return

            # wrong color or already changed
            if image[x][y] != old_color:
                return

            image[x][y] = color

            floodFill(x - 1, y)  # up
            floodFill(x + 1, y)  # down
            floodFill(x, y - 1)  # left
            floodFill(x, y + 1)  # right

        floodFill(sr, sc)

        return image