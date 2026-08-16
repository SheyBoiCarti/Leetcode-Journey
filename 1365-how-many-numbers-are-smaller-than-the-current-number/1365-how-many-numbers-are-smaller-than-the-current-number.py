class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #index=0
        #2 for loops
        #i=0, counter=0
        #[8,1,2,2,3]

        result=[0] * len(nums)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    continue
                elif nums[j] < nums[i]:
                    result[i]= result[i]+1
        return result
                

