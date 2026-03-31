//recursion and backtracking
class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> dist = new ArrayList<>();
        int n = nums.length;
        backtrack(nums,dist, new ArrayList<>(), new boolean[nums.length]);
        return dist;
    }

    static void backtrack(int nums[], List<List<Integer>> dist, List<Integer> tempList, boolean arr[]){
        if(tempList.size() == nums.length){
            dist.add(new ArrayList<>(tempList));
            return;
        }
        for(int i = 0;i<nums.length;i++){
            if(arr[i]) continue;
            arr[i]=true;
            tempList.add(nums[i]);
            backtrack(nums,dist, tempList, arr);
            arr[i] = false;
            tempList.remove(tempList.size() -1);
        }
    }
}