class Solution {
    public boolean isValid(String s) {
        
        Stack<Character> st = new Stack<Character> ();
        for(int i=0;i < s.length();i++){
            if (s.charAt(i) == '(' | s.charAt(i) == '{' | s.charAt(i) == '['){
                st.push(s.charAt(i));
            }
            else if(s.charAt(i) == ')' | s.charAt(i) == '}' | s.charAt(i) == ']'){
                if (st.empty()){
                    return false;
                }
                else if(st.peek() == '(' & s.charAt(i) == ')' | st.peek() == '{' & s.charAt(i) == 
                '}' | st.peek() == '[' & s.charAt(i) == ']'){
                st.pop();
                }
                else{return false;}
            }
                            
        }
        if (st.empty()){
            return true;
        }else{return false;}
    }
}