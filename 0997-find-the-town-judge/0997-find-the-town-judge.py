class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        town_judge =-1
        counter=0
        print(len(trust))
        if n==len(trust):
            return -1

        hashset= set()

        hashmap={}

        for i in range(len(trust)):
            Person_that_trusts,Person_trust_on= trust[i]
            hashset.add(Person_that_trusts)
   
        for i in range(1,n+1):
            if i not in hashset:
                town_judge= i

        if town_judge ==-1:
            return -1

        for i in range(len(trust)):
            Person_that_trusts,Person_trust_on= trust[i]

            if Person_trust_on == town_judge:
                counter+=1
        
        if counter!= n-1:
            return -1
        
        return town_judge

        print(town_judge)
        print(hashset)

    

        