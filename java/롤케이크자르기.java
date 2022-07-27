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

        for(int i=0;i<ln;i++){
            Map<String, List<Integer>> sliced = slice(i, topping);
            
            int firstUniqueCount = getUniqueCount(sliced.get("first"));
            int secondUniqueCount = getUniqueCount(sliced.get("second"));
            
            if (firstUniqueCount == secondUniqueCount){
                answer+=1;
            }
        }
        return answer;
    }

    private Map<String, List<Integer>> slice(int idx, int[] target){
        List<Integer> array1 = new ArrayList<Integer>();
        List<Integer> array2 = new ArrayList<Integer>();
        for(int i=0;i<=idx;i++){
            array1.add(target[i]);
        }
        int ln = target.length;
        for(int i=idx+1; i<ln; i++){
            array2.add(target[i]);
        }

        Map<String, List<Integer>> map = new HashMap<String, List<Integer>>();
        map.put("first", array1);
        map.put("second", array2);
        return map;
    }

    private int getUniqueCount(List<Integer> piece){
        Set<Integer> pieceSet = new HashSet<>(piece);
        return pieceSet.size();
    }
}