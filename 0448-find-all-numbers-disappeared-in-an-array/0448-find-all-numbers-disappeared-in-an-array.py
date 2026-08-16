class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
      
        result=[]

        for i in range(len(nums)):
            value= abs(nums[i])-1 #minus one because we want index
            nums[value]= abs(nums[value]) *-1
     
        for i in range(len(nums)):
            if nums[i] > 0 :
                result.append(i+1)
        print(nums)
        return result


        
           
        
        