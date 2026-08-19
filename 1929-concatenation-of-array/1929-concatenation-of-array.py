class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        output= [0] * (2* len(nums))
        endindex=0
        n= len(nums)

        for i in range(n):
            output[i]= nums[i]
            endindex=i
    
        counter=0
        for j in range(endindex+1,endindex+n+1):
            output[j]= nums[counter]
            counter+=1

        return output



        