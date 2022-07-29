// you can also use imports, for example:
// import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public static boolean[] visited = new boolean[100001];

    public int solution(int[] T, int[] A) {
        // write your code in Java SE 8
        int answer = 0;
        for(int a: A){
            find(a, T);
        }
        for(boolean v: visited){
            if(v){
                answer+=1;
            }
        }
        return answer;
        //
    }

    private int find(int x, int[] parents){
        if(x==parents[x]){
            visited[x] = true;
            return x;
        }else{
            visited[x] = true;
            return parents[x] = find(parents[x], parents);
        }
    }    
}
