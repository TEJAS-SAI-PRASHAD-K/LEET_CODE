class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hash_table1 = {}
        hash_table2 = {}
        
        for i in s:
            hash_table1[i] = hash_table1.get(i, 0) + 1
        for j in t:
            hash_table2[j] = hash_table2.get(j, 0) + 1
        
        return hash_table1 == hash_table2
