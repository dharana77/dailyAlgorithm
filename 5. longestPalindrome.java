class Solution {
    private int mx = 0;
    private String answer = "";

    public String longestPalindrome(String s) {
        answer = Character.toString(s.charAt(0));
        for(int i=0; i<s.length(); i++){
            for(int j=i+1; j<=s.length(); j++){
                String t = s.substring(i,j);
                // System.out.println(t);
                if(isPalindrome(t)){
                    if(mx<t.length()){
                        mx = t.length();
                        answer = t;
                    }
                }
            }
        }
        return answer;
    }

    public boolean isPalindrome(String s){
        for(int i=0; i<=s.length()/2; i++){
            if(s.charAt(i)!= s.charAt(s.length()-1-i)){
                return false;
            }
        }
        return true;
    }
}