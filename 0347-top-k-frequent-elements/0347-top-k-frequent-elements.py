class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap={}

        result=[]

        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]]+=1
            else: 
                hashmap[nums[i]]=1

        hashmap = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))

        for key,value in hashmap.items():
            if k!=0:
                result.append(key)
                k-=1
        return result