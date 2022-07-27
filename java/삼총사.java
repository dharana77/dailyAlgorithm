class Solution {
    private int answer = 0;

    public int solution(int[] number) {
        boolean[] visited = new boolean[number.length];
        dfs(0, 0, 0, number, visited);
        return answer;
    }

    private void dfs(int start, int count, int sum, int[] target, boolean[] visited){
        int ln = target.length;
        if(count==3){
            if(sum==0){
                answer+=1;
            }
            return;
        }
        for(int i=start; i<ln; i++){
            int next = i;
            if(visited[next]){
                continue;
            }
            int totalSum = sum + target[i];
            // System.out.println("start: "+start + " next: "+next + " total: " +totalSum);
            visited[next] = true;
            dfs(next,count+1,totalSum,target, visited);
            visited[next] = false;

        }
    }
}