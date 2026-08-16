class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        hashset= set()

        for n in nums:
            hashset.add(n)

        for i in range(0,len(nums)+1):
            if i not in hashset:
                return i


        