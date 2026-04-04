class Solution {
    public int longestValidParentheses(String s) {
        int n = s.length();
        if(n == 0) return 0;

        Stack<Integer> st = new Stack<>();
        st.push(-1);
        int maxLen = 0;

        for(int i=0;i<n;i++){
            char cur = s.charAt(i);
            if(cur == '('){
                st.push(i);
            }else{
                st.pop();
                if(st.isEmpty()){
                    st.push(i);
                }
                maxLen = Math.max(maxLen,i-st.peek());
            }
            
        }
        return maxLen;
    }
}