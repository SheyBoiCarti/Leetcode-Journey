class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        hashmap = {}

        start=0
        end = 0
        length = len(s)
        maxcounter=0

        while(end< length):
     
            if s[end] in hashmap:
                hashmap[s[end]] +=1
            else:
                hashmap[s[end]] = 1
            
            while(hashmap[s[end]] >2):
                hashmap[s[start]] -= 1
                if hashmap[s[start]]==0:
                    del hashmap[s[start]]
                start+=1

            maxcounter= max(maxcounter, end-start+1)
            end+=1
        
        return maxcounter
            

        