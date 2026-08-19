class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        town_judge =-1
        counterForPeopleTrustingTownJudge=0
        
        hashset= set()

        for i in range(len(trust)):
            Person_that_trusts,Person_trust_on= trust[i]
            hashset.add(Person_that_trusts)

        #The town judge trusts nobody.
        for i in range(1,n+1):
            if i not in hashset:
                town_judge= i

        if town_judge ==-1:
            return -1

        #Everybody (except for the town judge) trusts the town judge.
        #if thats the case then there should be n-1 people trusting the judge since the judge itself is not included 

        for i in range(len(trust)):
            Person_that_trusts,Person_trust_on= trust[i]

            if Person_trust_on == town_judge:
                counterForPeopleTrustingTownJudge+=1
        
        if counterForPeopleTrustingTownJudge!= n-1:
            return -1
        
        return town_judge      