    import java.util.*;

    class Solution {
        private int MAX_CHAR = 256;

        public int lengthOfLongestSubstring(String s) {
            int answer = 0 ;
            String target = "";
            for(int i=0; i<s.length(); i++){
                target += s.charAt(i);
                if(isUnique(target)){
                    // System.out.println(target);
                    if(answer<target.length()){
                        
                        answer = target.length();
                    }
                }else{
                    target = target.substring( target.indexOf(s.charAt(i)) + 1);  
                    // System.out.println(target);
                }
            
            }
            return answer;
        }

        public boolean isUnique(String target){
            // System.out.println(target);
            boolean[] chars = new boolean[MAX_CHAR];
            Arrays.fill(chars, false);

            if(target.length() > MAX_CHAR){
                return false;
            }

            for(int i=0; i<target.length(); i++){
                int index = (int)target.charAt(i);

                if(chars[index]==true){
                    return false;
                }
                if(chars[index]==false){
                    chars[index]=true;
                }

            }
            return true;
        }
    }