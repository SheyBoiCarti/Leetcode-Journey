class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        hashset= set()
        result=[]
        

        for n in nums:
            hashset.add(n)
        
        for i in range(1,len(nums)+1):
            if i not in hashset:
                result.append(i)
        
        return result
        


        