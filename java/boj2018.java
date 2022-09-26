import java.util.Scanner;

public class boj2018 {
    
    public static void main(String[] args) {
        //천만
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        //05:10 ~ 05:35
        long i =0, j=1;
        long tot = 0;
        long ans = 0;

        while(i<=n && j<=n){
            tot = j*(j+1)/2 - i*(i+1)/2;
            if (tot==n){
                // System.out.println(String.valueOf(i)+" "+String.valueOf(j));
                i+=1;
                j+=1;
                ans+=1;
            }else if(tot<n){
                j+=1;
            }else if(tot>n){
                i+=1;
            }
            // System.out.println(String.valueOf(i)+" "+String.valueOf(j));
        }
        System.out.println(ans);
    }
}
