import java.util.Scanner;
import java.util.ArrayList; 

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> n_list = new ArrayList<>(); 

        while(true) {
            int n = sc.nextInt();
            if (n == 0) break;
            n_list.add(n); 
        }

        for (int n : n_list) {
            ArrayList<Integer> number = new ArrayList<>();
        
            while (n != 0) {
                number.add(n % 10);
                n = n / 10;
            }
    
            int a = 0;
            int b = number.size() - 1;
            int is_same = 1;

            while (a < b) {
                if (number.get(a) != number.get(b)) {
                    is_same = 0;
                    break;
                }
                a ++;
                b --; 
            }

            if (is_same == 1) System.out.println("yes");
            else System.out.println("no");
        }

        sc.close();
    }
}