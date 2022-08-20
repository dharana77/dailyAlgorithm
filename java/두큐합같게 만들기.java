import java.util.Queue;
import java.util.LinkedList;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int answer = 0;
        Queue<Integer> q1 = new LinkedList<Integer>();
        Queue<Integer> q2 = new LinkedList<>();
        int size1 = queue1.length;
        int size2 = queue2.length;
        long q1Sum = 0;
        long q2Sum = 0;
        
        // System.out.println(Math.max(size1, size2) *2 +2);
        for (int i=0; i<size1; i++){
            q1.add(queue1[i]);
            q1Sum += queue1[i];
        }
        
        for (int i=0; i<size2; i++){
            q2.add(queue2[i]);
            q2Sum += queue2[i];
        }
        
    
        while(q1.size()!=0 && q2.size()!=0){
            // System.out.println(q1Sum +" "+ q2Sum);
            if(q1Sum == q2Sum){
                return answer;
            }
            if(q1Sum < q2Sum){
                int target = q2.poll();
                q1.add(target);
                q2Sum -= target;
                q1Sum += target;
            }else if(q2Sum < q1Sum){
                int target = q1.poll();
                q2.add(target);
                q1Sum -= target;
                q2Sum += target;
            }
            if(answer > ((size1 + size2) * 2 + 2) ){
                return -1;
            }
            answer+=1;
        }
        return -1;
    }
}