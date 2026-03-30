class Solution {
    public int findNumberOfLIS(int[] nums) {
        int n = nums.length;
        int[] len = new int[n];
        int[] count = new int[n];
        Arrays.fill(len,1);
        Arrays.fill(count,1);

        int maxlen = 0;
        int cnt = 0;

        for(int i=0;i<n;i++){
            for(int j=0;j<i;j++){
                if(nums[i] > nums[j]){
                    if(len[j]+1 > len[i]){
                        len[i] = len[j] + 1;
                        count[i] = count[j];
                    }
                    else if(len[j]+1 == len[i]){
                        count[i] += count[j];
                    }
                }
            }
            maxlen = Math.max(maxlen, len[i]);
        }
        


        for(int i=0;i<n;i++){
            if(len[i] == maxlen){
                cnt += count[i];
            }
        }
        return cnt;
    }
}