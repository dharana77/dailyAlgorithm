// you can also use imports, for example:
import java.util.*;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public String solution(String S, String C) {
        // write your code in Java SE 8
        String domain = C.toLowerCase() +".com";
        String[] s = S.split(",");
        int sln = S.split(",").length;
        Map<String, Integer> idCount = new HashMap<>();

        String ans = "";
        for(int i=0;i<s.length;i++){
            String test = s[i];
            String[] target =  test.split(" ");
            int ln = target.length;
            int start = 0;
            if(target[0].equals("")){
                start = 1;
            }

            // System.out.println(target[start]);
            // char a = Character.toLowerCase(target[start].charAt(0));
            // System.out.println("test"+a);
            if((i==0 && ln!=3) || (i!=0 && ln == 3)){
                
                char a = Character.toLowerCase(target[start].charAt(0));
                String b = target[start+1].toLowerCase();
                String temp = a + b;
                
                int ct;
                if (idCount.get(temp)==null){
                    idCount.put(temp,1);
                    ct = 1;
                }else{
                    idCount.put(temp,idCount.get(temp)+1);
                    ct = idCount.get(temp);
                }
                String t;
                if(ct==1){
                    t = test + " <" + temp + "@" + domain +">";    
                }else{
                    String count = Integer.toString(ct);
                    t = test + " <" + temp + count + "@" + domain +">";
                }
                // System.out.println(t);
                ans+=t;

            }else {
                
                char a = Character.toLowerCase(target[start].charAt(0));
                char b = Character.toLowerCase(target[start+1].charAt(0));
                String c = target[start+2].toLowerCase().replaceAll("-", "");
                if(c.length() >=8){
                    c = c.substring(0,8);
                }
                String temp = ""+a+b+c;
                // System.out.println(temp);
                int ct;
                if (idCount.get(temp)==null){
                    idCount.put(temp,1);
                    ct=1;
                }else{
                    idCount.put(temp,idCount.get(temp)+1);
                    ct = idCount.get(temp);
                }

                String t;
                if(ct==1){
                    t = test + " <" + temp + "@" + domain +">";    
                }else{
                    String count = Integer.toString(ct);
                    t = test + " <" + temp + count + "@" + domain +">";
                }
                // System.out.println(t);
                ans+=t;
            }
            if(i!=s.length-1){
                ans+=",";
            }
        }
        // System.out.println(ans);
        return ans;
    }
}