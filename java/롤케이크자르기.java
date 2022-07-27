import java.util.*;
//topping 100,000
//topping 원소 1<=  <=10,000
//시간초과

//왼쪽부터, 오른쪽 부터 종류 세기로 풀수 있을듯. 수정할 계획.
class Solution {
    
    public int solution(int[] topping) {
        //1,2,2,3,3,4,4,4

        int answer = 0;
        int ln = topping.length;
        int[] leftCount = new int[10001];
        int[] rightCount = new int[10001];
        int[] leftUniqueCount = new int[ln];
        int[] rightUniqueCount = new int[ln];

        //왼쪽
        int uniqueCount = 0;
        for(int i=0; i<ln; i++){
            int target = topping[i];
            if(leftCount[target]==0){
                uniqueCount+=1;
            }
            leftCount[target]+=1;
            leftUniqueCount[i] = uniqueCount;
        }

        //오른쪽
        uniqueCount = 0;
        for(int i=ln-1; i>=0; i--){
            int target = topping[i];
            if(rightCount[target]==0){
                uniqueCount+=1;
            }
            rightCount[target]+=1;
            rightUniqueCount[i] = uniqueCount;
        }

        for(int i=0; i<ln-1; i++){
            if(leftUniqueCount[i]==rightUniqueCount[i+1]){
                answer+=1;
            }
        }

        
        return answer;
    }

    
}