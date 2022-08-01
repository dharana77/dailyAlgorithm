class Solution {
    public int solution(String s) {
        int answer = s.length();
        
        for(int i=1; i<=s.length()/2+1; i++){
            //반복할 문자개수
            StringBuilder sb = new StringBuilder();
            String target = s.substring(0,i);
            String temp = "";
            int count = 1;
            int tempIndex = -1;
            
            for(int j=i; j<=s.length(); j+=i){
                String toCompare = s.substring(j, (j+i) < s.length() ? j+i : s.length());
                tempIndex = j;
                if(target.equals(toCompare)){
                    count+=1;
                }else{
                    temp += (target + (count == 1 ? "" :Integer.toString(count)));
                    count = 1;
                    target = toCompare;
                }
            }
            // System.out.println(tempIndex);
            temp += s.substring(tempIndex, s.length());
            // System.out.println(temp);
            answer = answer > temp.length() ? temp.length() : answer;
        }
        
        return answer;
    }
}