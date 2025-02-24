import java.util.*;
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Hashtable<Integer, Integer> table = new Hashtable<>();
        int n = nums.length;

        for (int num : nums) {
            table.put(num, table.getOrDefault(num, 0) + 1);

            if (table.get(num) >= 2) {
                return true;
            }
        }
        return false;
    }
}