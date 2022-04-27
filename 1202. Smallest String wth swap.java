class UnionFind{
    private int[] id;

    public UnionFind(int number){
        id = new int[number];
        for(int i=0; i< number; ++i){
            id[i] = i;
        }
    }

    public void union(int u, int v){
        id[find(u)] = find(v);
    }

    public int find(int u){
        return id[u] == u? u: (id[u] = find(id[u]));
    }
}


class Solution {
    public String smallestStringWithSwaps(String s, List<List<Integer>> pairs) {
        StringBuilder ans = new StringBuilder();
        UnionFind uf = new UnionFind(s.length());
        Map<Integer, Queue<Character>> map = new HashMap<>();

        for(List<Integer> pair: pairs){
            uf.union(pair.get(0), pair.get(1));
        }

        for(int i=0; i<s.length(); ++i){
            map.computeIfAbsent(uf.find(i), k -> new PriorityQueue<>()).offer(s.charAt(i));
        }

        for(int i=0; i< s.length(); ++i){
            ans.append(map.get(uf.find(i)).poll());
        }

        return ans.toString();
    }
}