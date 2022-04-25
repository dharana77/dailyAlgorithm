import java.util.*;

//시간 초과 경우
// https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
class Solution {
    private int MAX_CHAR = 256;
    
    public int lengthOfLongestSubstring(String s) {
        int answer = 0 ;
        for(int i=0; i<s.length(); i++){
            for(int j=i+1; j<= s.length(); j++){
                String target = s.substring(i, j);
                
                if(isUnique(target)){
                    if(answer<target.length()){
                        answer = target.length();
                    }
                }
                
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