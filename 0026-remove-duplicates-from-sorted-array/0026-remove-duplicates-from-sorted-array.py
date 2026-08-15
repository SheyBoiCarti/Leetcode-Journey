class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        validindex=0
        current=0
        #[1,2,3]
        while(current< len(nums)):

            while(current+1 < len(nums) and nums[current]== nums[current+1]):
                current+=1
            
            nums[validindex]= nums[current]
            validindex+=1
            current+=1
            
        


        print(validindex)
        return validindex



        