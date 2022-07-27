class Solution {
    public String convert(String s, int numRows) {
        boolean down = true;
        int rowPos = 0;
        ArrayList<String> stringsVerRows = new ArrayList<String>();
        
        if(numRows==1){
            return s;
        }
        for(int i=0;i<numRows;i++){
            stringsVerRows.add("");
        }
        
        for(int i=0;i<s.length();i++){
            String target = stringsVerRows.get(rowPos);
            stringsVerRows.set(rowPos,target+s.charAt(i)); 
            if(i!=0 && i%(numRows-1)==0){
                down = !down;
            }
            if(down){
                rowPos+=1;
            }else{
                rowPos-=1;
            }
        }
        
        String answer = "";
        for(int i=0;i<numRows;i++){
            answer+= stringsVerRows.get(i);
        }
        return answer;
    }
}