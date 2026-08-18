class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area=0
        current=0

        rows= len(grid)
        cols= len(grid[0])

        def dfs(grid,x,y):
            nonlocal current
            if x<0 or x>=rows or y<0 or y>=cols:
                return None
            
            if grid[x][y]== 0:
                return None
            
            #visited
            grid[x][y]=0
            dfs(grid,x,y-1)#left
            dfs(grid,x,y+1)#right
            dfs(grid,x-1,y)#up
            dfs(grid,x+1,y)#down
            current+=1
        
        for x in range(rows):
            for y in range(cols):
                if grid[x][y]==1:
                    dfs(grid,x,y)
                    max_area= max(max_area,current)
                    current=0
        
        return max_area