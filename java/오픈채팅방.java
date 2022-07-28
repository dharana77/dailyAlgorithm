//03:17~ 4:23 집중!
import java.util.*;

class Solution {
    public String[] solution(String[] record) {
        
        List<Map<String,String>> results = new ArrayList<>();
        Map<String, String> namesById = new HashMap<>();
        
        int count = 0;
        
        for(String re: record){
            String[] test = re.split(" ");
            String state = test[0];
            // System.out.println("state:" + state);
            if (state.equals("Enter")){
                String id = test[1];
                String name = test[2];
                namesById.put(id,name);
                count+=1;
            }else if (state.equals("Leave")){
                String id = test[1];
                count+=1;
            }else if (state.equals("Change")){
                String id = test[1];
                String name = test[2];
                namesById.put(id,name);
            }
        }
        String[] answer = new String[count];
        
        int ct=0;
        for(String re: record){
            String[] test = re.split(" ");
            String state = test[0];
            
            if (state.equals("Enter")){
                String id = test[1];
                String name = test[2];
                answer[ct++] = namesById.get(id) + "님이 들어왔습니다.";
            }else if (state.equals("Leave")){
                String id = test[1];
                answer[ct++] = namesById.get(id) + "님이 나갔습니다.";
            }
        }
        
        return answer;
    }
}