class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
  
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp= nums.copy()
        temp.sort()
        hashmap= {}
        result= [0] * len(nums) #result = [0,0,0,0,0]


        for i in range(len(temp)):
            if temp[i] in hashmap:
                hashmap[temp[i]]= min(hashmap[temp[i]],i)
            else:
                hashmap[temp[i]]=i
                # hashmap {1:0, 2:1, 3:3, 8:4}
        print(temp)
        print(nums)

        for i in range(len(nums)):
            result[i]= hashmap[nums[i]]

        return result

                

