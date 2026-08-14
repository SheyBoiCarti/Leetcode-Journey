/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        
        ListNode tempList1= l1;
        ListNode tempList2= l2;

        int list1Value=0;
        int list2Value=0;

        int carry=0;
        int final=0;
        ListNode output = new ListNode(-1,null);
        ListNode currOutput = output;

        //[9,9,9,9,9,9,9]
        //[9,9,9,9,0,0,0]
        //8,9,9,9
        while(tempList1!= null || tempList2!= null){

            list1Value = (tempList1 == null ? 0 : tempList1.val);//9
            list2Value = (tempList2 == null ? 0 : tempList2.val);//0

            final = list1Value + list2Value+ carry; //10

            if(final >= 10){
                currOutput.next = new ListNode(final%10, null);//0
                carry = 1;
            }
            else{
                carry =0;
                currOutput.next = new ListNode(final,null);
            }
            currOutput = currOutput.next;

            if(tempList1 != null){
              tempList1= tempList1.next;
            }
            if(tempList2 != null){
              tempList2= tempList2.next;
            }

        }

        if(carry >0){
          currOutput.next = new ListNode(carry, null);
        }   

        return output.next;
    }
}