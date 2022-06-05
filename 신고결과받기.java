import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        
        HashMap<String, List<String>> reportedListById = new HashMap<String, List<String>>();
        
        for(int i=0; i<id_list.length; i++){
            // System.out.println(id_list[i]);
            List<String> reported_list = new ArrayList<String>();
            
            for(int j=0; j<report.length; j++){
                String reporter = report[j].split(" ")[0];
                String reported = report[j].split(" ")[1];
                // System.out.println(id_list[i]);
                if(reporter.equals(id_list[i])){
                    reported_list.add(reported);
                    
                }
            }
            Set<String> reported = new HashSet<String>(reported_list);
            List<String> set_reported = new ArrayList<String>(reported);
            reportedListById.put(id_list[i], set_reported);
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