package Graph;

import java.util.ArrayList;

class Node{
    int idx;
    int cost;

    Node(int idx, int cost){
        this.idx = idx;
        this.cost = cost;
    }
}


public class Dijkstra{
    public static void main(String[] args){
        int V = sc.nextInt();
        int E = sc.nextInt();
        int start = sc.nextInt();

        ArrayList<ArrayList<Node>> graph = new ArrayList<ArrayList<Node>>();
        for(int i=0;i<V;i++){
            graph.add(new ArrayList<>());
        }

        for(int i=0;i<E;i++){
            int a = sc.nextInt();
            int b = sc.nextInt();
            int cost = sc.nextInt();

            graph.get(a).add(new Node(b, cost));
        }

        //
        boolean[] visited = new boolean[V+1];
        int[] dist = new int[V+1];

        for (int i=0; i<V+1; i++){
            dist[i] = Integer.MAX_VALUE;
        }

        dist[start] = 0;

        for(int i=0; i<V; i++){
            int nodeValue = Integer.MAX_VALUE;
            int nodeIdx = 0;
            for(int j=1; j<V; j++){
                if(!visited[j])
            }
        }
        for(int i=0; i<V; i++){
            int currentValue = Integer.MAX_VALUE;
            int nodeIdx = 0;
            for(int j=1; j<V; j++){
                if(!visited[j] && dist[j] < currentValue){
                    currentValue = dist[j];
                    nodeIdx = j;
                }
            }
            visited[nodeIdx] = true;
        }
        //nodeIdx = 이동하기로 한 노드
        for(int j=0; j<graph.get(nodeIdx).size(); j++){
            Node targetNode = graph.get(nodeIdx).get(j);
            //현재 탐색 노드
            int idx = targetNode.idx;
            int cost = targetNode.cost;
            int totalValue = currentValue + cost;
            if(totalValue < dist[idx]){
                dist[idx] = totalValue;
            }
        }
    }

    for(int i=1; i<V+1; i++){
        if(dist[i] == Integer.MAX_VALUE){
            System.out.println("INF");
        }else{
            System.out.println(dist[i]);
        }
    }
    sc.close();
}