public class Solution {
    public int MissingInteger(int[] nums) {
        
        int n = nums.Length;
        int[] prefixSum= new int[n];
        HashSet<int> set = new HashSet<int>();
        int current=0;
        bool condition=false;
        int valueToCheck=-1;

        prefixSum[0]= nums[0];
        set.Add(nums[0]);
        


        for(int i=1;i<n;i++){
         prefixSum[i]= prefixSum[i-1] + nums[i];
         set.Add(nums[i]);
        }

        /*
        nums = [1,2,3,2,5]
        prefixSum = [1,3,6,8,13]

        current=0;
        */

        while(condition ==false){
            if(current +1 <n && nums[current]+1 == nums[current+1]){
                current++;
            }
            else{

                valueToCheck = prefixSum[current]; //returns 6

                while (set.Contains(valueToCheck))
                {
                valueToCheck++;
                }
                condition =true;
            }
        }

        return valueToCheck;



    }
}