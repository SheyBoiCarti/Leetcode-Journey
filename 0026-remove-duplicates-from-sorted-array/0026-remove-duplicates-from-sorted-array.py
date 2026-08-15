class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        validindex=0
        current=1

        #[1,2,2,3]
        while(current< len(nums)):
            if nums[validindex]!= nums[current]: 
                validindex+=1
                nums[validindex]= nums[current]
            
            current+=1
            
          #plus one because valid index returns to the array index
          #adding one gives the number of unique elements
        return validindex+1
       



        