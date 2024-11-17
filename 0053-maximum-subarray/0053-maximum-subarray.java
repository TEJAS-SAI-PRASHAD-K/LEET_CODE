import java.util.Arrays;
import java.io.*;
class Solution {
   public int maxSubArray(int[] nums) {
       int i;
       int max = nums[0];
       int sum =0;
       for(i = 0; i < nums.length; i++) {
         sum = sum + nums[i];
         if(sum > max){
            max=sum;
         }
         if(sum<0){
            sum=0;
         }
       }
       return max;
   }
}