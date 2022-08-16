class Solution {
    public boolean isUgly(int n) {
        boolean ans = true;
        while(n!=1){
            if(!isDivided(n)){
                ans = false;
                break;
            }
            n = divide(n);
        }
        return ans;
    }
    
    private boolean isDivided(int n){
        if(n%2 == 0 || n%3 == 0 || n%5 == 0){
            return true;
        }
        return false;
    }
    
    private int divide(int n){
        if(n%2 ==0){
            n = n/2;
        }
        if(n%3 ==0){
            n = n/3;
        }
        if(n%5 == 0){
            n = n/5;
        }
        return n;
    }
}