class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap={}

        for n in nums:
            if n not in hashmap:
                hashmap[n]=1
            else: 
                hashmap[n]+=1

        for key,value in hashmap.items():
            if value ==1:
                return key
        