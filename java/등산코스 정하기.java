import java.util.*;

class Solution {
    public int[] solution(int n, int[][] paths, int[] gates, int[] summits) {
        int[] answer = {0,0};
        
        ArrayList<ArrayList<Map<Integer, Integer>>> board = new ArrayList<ArrayList<Map<Integer, Integer>>>();
        Arrays.sort(summits);
        
        for(int i=0; i<n+1; i++){
            ArrayList<Map<Integer, Integer>> temp = new ArrayList<Map<Integer, Integer>>();
            board.add(temp);
        }
        
        for(int i=0; i<paths.length; i++){
            int from = paths[i][0];
            int to = paths[i][1];
            int w = paths[i][2];
            HashMap<Integer, Integer> map = new HashMap<>();
            map.put(to, w);
            board.get(from).add(map);
            HashMap<Integer, Integer> map2 = new HashMap<>();
            map2.put(from,w);
            board.get(to).add(map2);
        }
        
        int [] dist = new int[n+1];
        for(int i=1; i<=n; i++){
            dist[i] = Integer.MAX_VALUE;
        }
        
        for(int i=0; i<gates.length; i++){
            int node = gates[i];
            dist[node] = 0;
        }
        
        Queue<Integer> q = new LinkedList<>();
        
        for(int i=0; i<gates.length; i++){
            q.add(gates[i]);
        }
        
        while(q.size() != 0){
            int node = q.poll();
            // System.out.println("qnode:" + node);
            boolean isSummit = false;
            
            for(int i=0; i<summits.length; i++){
                if(summits[i] == node){
                    isSummit = true;
                    break;
                }
            }
            
            if(isSummit) continue;
            
            for(int i=0; i<board.get(node).size(); i++){
                Map<Integer, Integer> map = board.get(node).get(i);
                Iterator<Integer> it = map.keySet().iterator();
                int nextNode = it.next();
                int w = map.get(nextNode);
                int currentMaxW = Math.max(w, dist[node]);
                
                if(dist[nextNode] > currentMaxW ){
                    // System.out.println("addqueNode:" + nextNode);
                    // System.out.println("maxw:" + currentMaxW);
                    
                    q.add(nextNode);
                    dist[nextNode] = currentMaxW;
                }
            }
        }
        
        // for(int i=0; i<dist.length; i++){
        //     System.out.println(i +":" + dist[i]);    
        // }
        
        int mx = dist[summits[0]];
        int s = summits[0];
        // System.out.println("mx, s"+ mx +" "+ s);
        for(int i=0; i<summits.length; i++){
            int node = summits[i];
            // System.out.println("node:"+node);
            // System.out.println("dist:"+dist[node]);
            if(dist[node] != 0 && dist[node] < mx){
                mx = dist[node];
                s = node;
            }
        }
        answer[0] = s;
        answer[1] = mx;
        return answer;
    }
}