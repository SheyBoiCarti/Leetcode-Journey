class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hashmap={}
        n = len(nums)/2

        for num in nums:
            if num not in hashmap:
                hashmap[num]=1
            else:
                hashmap[num]+=1

        for key,value in hashmap.items():
            print(value)
            if value > n:
                return key    