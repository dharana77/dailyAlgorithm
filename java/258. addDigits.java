class Solution {
    public int addDigits(int num) {
        String target = Integer.toString(num);
        int s = num;
        // System.out.println(target.length());
        while(target.length()!=1){
            s = 0;
            for(int i=0; i<target.length(); i++){
                s+= Character.getNumericValue(target.charAt(i));
            }
            target = Integer.toString(s);
        }
        return s;
    }
}