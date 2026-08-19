from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap={}
        result=[]

        counter=0
        for i in range(len(strs)):
            sortedvalue= "".join(sorted(strs[i]))
            if sortedvalue in hashmap:
                result[hashmap[sortedvalue]].append(strs[i])
            else:
                hashmap[sortedvalue] =counter
                counter+=1
                result.append([strs[i]])

        return result
     