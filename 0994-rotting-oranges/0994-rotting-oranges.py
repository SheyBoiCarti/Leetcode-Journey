class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Basic idea is to:
        # Find all rotten oranges and store their positions in the queue
        # Count the number of fresh oranges
        # Run BFS starting from all rotten oranges at the same time
        # Each BFS level represents one minute
        # When a fresh orange becomes rotten, decrease the fresh orange counter
        # After BFS, if fresh oranges remain, return -1; otherwise return the minutes
        
        rows= len(grid)
        cols= len(grid[0])

        fresh=0
        minute=0

        q= deque()

        for i in range(rows):
            for j in range(cols):
                value = grid[i][j]
                if value==1:
                    fresh+=1
                if value==2:
                    q.append((i,j))

        def bfs(grid):
            nonlocal fresh
            nonlocal minute

            while q:
                numberofvalues= len(q)

                for i in range(numberofvalues):
                    x,y = q.popleft()

                    if x-1>=0 and grid[x-1][y]==1:
                        grid[x - 1][y] = 2
                        fresh-=1
                        q.append((x-1,y))
                
                    if x+1<rows and grid[x+1][y]==1:
                        grid[x + 1][y] = 2
                        fresh-=1
                        q.append((x+1,y))
                    
                    if y-1>=0 and grid[x][y-1]==1:
                        grid[x][y-1] = 2
                        fresh-=1
                        q.append((x,y-1))

                    if y+1 < cols and grid[x][y+1]==1:
                        grid[x][y+1] = 2
                        fresh-=1
                        q.append((x,y+1))
                if q:
                    #if there is still elements in queue, increase minutes
                    minute += 1
        
        bfs(grid)

        if fresh > 0: return -1

        return minute
            


        

                








        