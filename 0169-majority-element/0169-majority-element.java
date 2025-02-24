import java.util.*;

class Solution {
    public int majorityElement(int[] nums) {
        Hashtable<Integer, Integer> table = new Hashtable<>();
        int n = nums.length;

        for (int num : nums) {
            table.put(num, table.getOrDefault(num, 0) + 1);

            if (table.get(num) > n / 2) {
                return num;
            }
        }
        return -1;
    }  
}