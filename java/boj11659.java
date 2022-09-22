import java.util.Scanner;

public class boj11659 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] arr = new int[n+1];

        for(int i=1; i<=n; i++){
            arr[i] = sc.nextInt();
        }
        int start = 0;
        int end = 0;
        
        int[] sum = new int[n+1];
        int total = 0;
        for(int j=1; j<=n; j++){
            total+= arr[j];
            sum[j] = total;
        }
        
        for(int i=0; i<m; i++){
            start = sc.nextInt();
            end = sc.nextInt();
            
            System.out.println(sum[end]-sum[start-1]);
        }
        
    }
}
