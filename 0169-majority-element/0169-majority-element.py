class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        result=-1
        counter=0

        for n in nums:
            if counter==0:
                result=n
                counter=1
            elif n==result:
                counter+=1
            else:
                counter-=1

        return result
