import java.util.Scanner;

import javax.print.attribute.PrintServiceAttributeSet;

public class boj1546 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        double[] arr = new double[n];

        double mx = 0;
        double total = 0;

        for(int i=0; i<n; i++){
            arr[i] = sc.nextDouble();
            if (arr[i] > mx){
                mx = arr[i];
            }
            total += arr[i];
        }
        
        System.out.println(total/n/mx*100);
    }
}
