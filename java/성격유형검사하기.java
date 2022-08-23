import java.util.HashMap;

class Solution {
    private HashMap<String, Integer> scores = 
        new HashMap<>(){{
            put("R", 0);
            put("T", 0);
            put("C", 0);
            put("F", 0);
            put("J", 0);
            put("M", 0);
            put("A", 0);
            put("N", 0);
        }};
    
    public String solution(String[] survey, int[] choices) {
        String answer = "";
        for(int i=0; i<survey.length; i++){
            String currentSurvey = survey[i];
            getValue(currentSurvey, choices[i]);
        }
        // System.out.println(scores);
        
        if(scores.get("R") >= scores.get("T")){
            answer += "R";
        }else{
            answer += "T";
        }
        
        if(scores.get("C") >= scores.get("F")){
            answer += "C";
        }else{
            answer += "F";
        }
        
        if(scores.get("J") >= scores.get("M")){
            answer += "J";
        }else{
            answer += "M";
        }
        
        if(scores.get("A") >= scores.get("N")){
            answer += "A";
        }else{
            answer += "N";
        }
        return answer;
    }
    
    private void getValue(String survey, int choice){
        if (choice==1){
            String target = String.valueOf(survey.charAt(0));
            int currentScore = scores.get(target);
            scores.put(target, currentScore + 3);
        }
        else if(choice == 2){
            String target = String.valueOf(survey.charAt(0));
            int currentScore = scores.get(target);
            scores.put(target, currentScore + 2);
        }else if(choice == 3){
            String target = String.valueOf(survey.charAt(0));
            int currentScore = scores.get(target);
            scores.put(target, currentScore + 1);
        }else if(choice ==5){
            String target = String.valueOf(survey.charAt(1));
            int currentScore = scores.get(target);
            scores.put(target, currentScore + 1);
        }else if(choice == 6){
            String target = String.valueOf(survey.charAt(1));
            int currentScore = scores.get(target);
            scores.put(target, currentScore + 2);
        }else if(choice == 7){
            String target = String.valueOf(survey.charAt(1));
            int currentScore = scores.get(target);
            scores.put(target, currentScore + 3);
        }
    }
}