class Solution {
    public int maxArea(int[] height) {
        int ln = height.length;
        int ans = 0;
        int i=0, j=ln-1;
        while(i<ln && j>=0){
            int h = Math.min(height[i], height[j]);
            ans = Math.max(ans, Math.abs(j-i) * h);
            if(height[i]>=height[j]){
                j-=1;
            }else{
                i+=1;
            }
        }
        return ans;
    }
}