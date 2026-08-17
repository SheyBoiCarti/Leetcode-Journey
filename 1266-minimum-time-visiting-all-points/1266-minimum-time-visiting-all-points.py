class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        distance=0
        start=0
        current=1

        while(current < len(points)):
            point1= points[start]
            point2= points[current]

            x1, y1 = point1
            x2, y2 = point2
            distance+= max(abs(x1-x2), abs(y1-y2))
            current+=1
            start+=1
        
        return distance



