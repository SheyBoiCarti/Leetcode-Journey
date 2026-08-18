class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #loop through all the elements
        #if we encounter one, check its left,right, up, and down
        #if we encounter boundary, increase perimieter
        #if we encounter 0 increase perimeter

        rows = len(grid)
        cols= len(grid[0])

        perimeter=0
        #need to check bounds(means we hit a boundary) or if going in that direction gives us an zero
        for x in range(rows):
            for y in range(cols):
                if grid[x][y]==1:
                    #go left
                    if y-1 <0 or grid[x][y-1] ==0:
                        perimeter+=1
                    #right
                    if y+1 >=cols or grid[x][y+1] ==0:
                        perimeter+=1
                    #go up 
                    if x-1 <0 or grid[x-1][y] ==0:
                        perimeter+=1
                    #go down
                    if x+1 >=rows or grid[x+1][y] ==0:
                        perimeter+=1
        return perimeter


                    

        