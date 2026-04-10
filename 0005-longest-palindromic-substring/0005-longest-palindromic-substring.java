class Solution {

    static String Expansion_middle(String s,int n,int l,int r){

        while(l>=0 && r<n && s.charAt(l) == s.charAt(r)){
            l--;
            r++;
        }  
        return s.substring(l+1,r);
    }
    public String longestPalindrome(String s) {
        int n =s.length();
        if(n == 0) return "";
        String max = "";
        int l,r;

        for(int i=0;i<n;i++){
            String odd = Expansion_middle(s,n,i,i);
            String even = Expansion_middle(s,n,i,i+1);

            if(max.length()<odd.length()) max = odd;
            if(max.length()<even.length()) max = even;
        }

        return max;
    }

}