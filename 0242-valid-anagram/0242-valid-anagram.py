class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashmap={}

        for c in s:
            if c in hashmap:
                hashmap[c]= hashmap[c]+1
            else: hashmap[c]=1
        
        for c2 in t:
            if c2 in hashmap:
                if hashmap[c2] >0:
                    hashmap[c2]= hashmap[c2]-1
                    if hashmap[c2] ==0 :
                        del hashmap[c2]
            else:return False
        
        print(len(hashmap))
        return len(hashmap) ==0

        