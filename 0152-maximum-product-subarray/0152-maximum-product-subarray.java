import java.util.Arrays;
import java.io.*;
class Solution {
   public int maxProduct(int[] nums) {
       int pref=1,suff=1;
       int n = nums.length;
       int max_sum=Integer.MIN_VALUE;
       for(int i = 0; i < n; i++) {
        if(pref==0){
            pref=1;
        }
        if(suff==0){
            suff=1;
        }
        pref = pref*nums[i];
        suff = suff*nums[n-1-i];
        max_sum = Math.max(max_sum,Math.max(pref,suff));
       }

       return max_sum;
    }
}