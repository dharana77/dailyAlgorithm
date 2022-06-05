import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        
        HashMap<String, List<String>> reportedListById = new HashMap<String, List<String>>();
        
        for(int i=0; i<id_list.length; i++){
            List<String>emptyList = new ArrayList<String>();
            reportedListById.put(id_list[i], emptyList);
        }
        
        for(int j=0; j<report.length; j++){
            String reporter = report[j].split(" ")[0];
            String reported = report[j].split(" ")[1];
            List<String> value = reportedListById.get(reporter);
            value.add(reported);
            reportedListById.put(reporter, value);
        }
        Set<String>reportSet = reportedListById.keySet();
        for(String reporter: reportSet){
            Set<String> reported = new HashSet<String>(reportedListById.get(reporter));
            List<String> set_reported = new ArrayList<String>(reported);
            reportedListById.put(reporter, set_reported);
        }
    
        
        // Set<String> keySet = reportedListById.keySet();
        // for(String key: keySet){
        //     System.out.println(key);
        //     System.out.println(reportedListById.get(key));
        // }
        HashMap<String, Integer> reportedCountById = new HashMap<String, Integer>();
        for(int i=0; i<id_list.length; i++){
            reportedCountById.put(id_list[i], 0);
        }
        for(int i=0; i<id_list.length; i++){
            List<String>reportedList = reportedListById.get(id_list[i]);
            for(int j=0; j<reportedList.size(); j++){
                Integer targetValue = reportedCountById.get(reportedList.get(j));
                reportedCountById.put(reportedList.get(j), targetValue+1);
            }
        }
        ArrayList<Integer> answerList = new ArrayList<Integer>();
        for(int i=0; i<id_list.length; i++){
            int ct = 0;
            List<String> localReportedList = reportedListById.get(id_list[i]);
            for(int j=0; j<localReportedList.size(); j++){
                if(reportedCountById.get(localReportedList.get(j))>=k){
                    ct+=1;
                }
            }
            answerList.add(ct);
        }
        int[] answer = new int[answerList.size()];
        for(int i=0; i<answerList.size(); i++){
            answer[i] = answerList.get(i);
        }
        
        return answer;
    }
}