public class Solution {
    public void Merge(int[] nums1, int m, int[] nums2, int n) {
        
        int nums1Length = nums1.Length;
        int counter=0;

        for(int i=m;i<nums1Length;i++){
            nums1[i]= nums2[counter];
            counter++;
        }

        Array.Sort(nums1);
    }
}