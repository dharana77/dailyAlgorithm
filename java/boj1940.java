import java.util.Arrays;
import java.util.Scanner;

public class boj1940 {
    //17:44 ~
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] items = new int[n];

        for(int a=0; a<n; a++){
            items[a] = sc.nextInt();
        }

        int i=0, j=n-1;
        int ans = 0 ;

        Arrays.sort(items);
        
        // for(int k=0; k< items.length; k++){
        //     System.out.println(items[k]);
        // }

        while(i<j){
            int target = items[i] + items[j];
            
            if( target == m){
                j-=1;
                ans+=1;
            }
            else if(target < m){
                i+=1;
            }
            else if(target > m){
                j-=1;
            }
        }
        // 1,2,3,4,5,7
        System.out.println(ans);
    }
}
