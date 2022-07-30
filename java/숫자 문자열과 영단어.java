class Solution {
    public int solution(String s) {
        int answer = 0;
        String temp = "";
        
        for(int i=0; i<s.length(); i++){
            char target = s.charAt(i);
            if(Character.isDigit(target)){
                temp+=target;
                continue;
            }
            if(target=='z'){
                temp+="0";
            }
            if(target=='o'){
                if(i+1<s.length() && i+2<s.length()){
                    if(s.charAt(i+1)=='n' && s.charAt(i+2)=='e'){
                        temp+="1";
                    }
                }
            }
            if(target=='t'){
                if(i+1<s.length() && i+2<s.length()){
                    if(s.charAt(i+1)=='w' && s.charAt(i+2)=='o'){
                        temp+="2";
                    }
                }
                if(i+1<s.length() && i+2<s.length() && i+3<s.length()){
                    if(s.charAt(i+1)=='h' && s.charAt(i+2)=='r' && s.charAt(i+3)=='e'){
                        temp+="3";
                    }
                }
            }
            if(target == 'f'){
                if(i+1<s.length() && i+2<s.length()){
                    if(s.charAt(i+1)=='o' && s.charAt(i+2)=='u'){
                        temp+="4";
                    }
                }
                if(i+1<s.length() && i+2<s.length()){
                    if(s.charAt(i+1)=='i' && s.charAt(i+2)=='v'){
                        temp+="5";
                    }
                }
            }
            
            if(target == 's'){
                if(i+1<s.length() && i+2<s.length()){
                    if(s.charAt(i+1)=='i' && s.charAt(i+2)=='x'){
                        temp+="6";
                    }
                }
                
                if(i+1<s.length() && i+2<s.length()){
                    if(s.charAt(i+1)=='e' && s.charAt(i+2)=='v'){
                        temp+="7";
                    }
                }
            }
            
            if(target == 'e'){
                if(i+1<s.length() && i+2<s.length()){
                    if(s.charAt(i+1)=='i' && s.charAt(i+2)=='g'){
                        temp+="8";
                    }
                }
            }
            
            if(target == 'n'){
                if(i+1<s.length() && i+2<s.length()){
                    if(s.charAt(i+1)=='i' && s.charAt(i+2)=='n'){
                        temp+="9";
                    }
                }
            }
            
            
        }
        answer = Integer.parseInt(temp);
        return answer;
    }
}