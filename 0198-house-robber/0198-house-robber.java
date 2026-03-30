class Solution {
    public int rob(int[] nums) {
        int max_val = 0;
        int prev1 = 0;
        int prev2 = 0;

        for(int cur: nums){
            max_val = Math.max(cur+prev2,max_val);

            prev2 = prev1;
            prev1 = max_val;
        }
        
        return prev1;
    }
}