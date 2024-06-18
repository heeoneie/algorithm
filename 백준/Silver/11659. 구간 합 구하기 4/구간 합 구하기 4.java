import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int n, m;
        int[] A;
        int i, j;

        n = scanner.nextInt();
        m = scanner.nextInt();

        A = new int[n + 1];
        for (int k = 1; k <= n; k++) {
            A[k] = scanner.nextInt();
        }

        int[] S = new int[n + 1];
        for (int k = 1; k <= n; k++) {
            S[k] = S[k - 1] + A[k];
        }

        for (int k = 0; k < m; k++) {
            i = scanner.nextInt();
            j = scanner.nextInt();
            System.out.println(S[j] - S[i - 1]);
        }
    }
}
