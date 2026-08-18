class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numberOfIslands=0

        rows= len(grid)
        cols= len(grid[0])

        visited= [[False] * cols for _ in range(rows)]

        def dfs(grid, x,y):
            nonlocal numberOfIslands
            if x< 0 or x>= rows or y<0 or y>=cols:
                return None

            if visited[x][y]== True:
                return None
            
        
            if grid[x][y]=='0':
                visited[x][y]= True
                return None
        
            #valid
            visited[x][y]= True
          
            dfs(grid,x+1,y) #down
            dfs(grid,x-1,y) #up
            dfs(grid,x,y+1) #right
            dfs(grid,x,y-1) #left

            
        for i in range(rows):
            for j in range (cols):
                if grid[i][j] == '1' and visited[i][j]==False:
                    numberOfIslands+=1
                dfs(grid,i,j)

        print(visited)

        return numberOfIslands
            