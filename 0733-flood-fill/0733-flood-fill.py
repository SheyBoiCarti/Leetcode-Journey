class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        #start flood fill at image[sr][sc]

        rows= len(image) 
        cols= len(image[0])

        boundary_x= rows-1
        boundary_y= cols-1

        old_color= image[sr][sc]

        visited= [[False] * cols for _ in range(rows)]
        print(visited)

        def floodFill(image, x,y, boundary_x, boundary_y, color):
            """
            #check if we can go up
            if x<0:
                #cant go up anymore
            if x > boundary_x:
                #cant go down anymore
            if y <0: 
                #cant go left
            if y> boundary_y: 
                #cant go right
            """
            # out of boundary for current cell
            if x<0 or x> boundary_x or y<0 or y > boundary_y:
                return None

            #already visited cell
            if visited[x][y]== True :
                return None
            
            # color doesnt match
            if old_color != image[x][y]:
                return None

            #now we at a valid cell

            image[x][y]= color
            visited[x][y]= True

            floodFill(image, x-1,y, boundary_x, boundary_y, color) #go up
            floodFill(image, x+1,y, boundary_x, boundary_y, color) #go down
            floodFill(image, x,y-1, boundary_x, boundary_y, color) #go left
            floodFill(image, x,y+1, boundary_x, boundary_y, color) #go right
        
        floodFill(image, sr, sc, boundary_x, boundary_y, color)
        print(visited)
        return image
     