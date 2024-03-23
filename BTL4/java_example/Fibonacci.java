public class Fibonacci {
    // Recursive approach
    public static int fibonacciRecursive(int n) {
        if (n <= 1)
            return n;
        return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
    }

    // Dynamic programming approach using array
    public static int fibonacciDynamic(int n) {
        int[] fibArray = new int[n + 1];
        fibArray[0] = 0;
        fibArray[1] = 1;

        for (int i = 2; i <= n; i++) {
            fibArray[i] = fibArray[i - 1] + fibArray[i - 2];
        }

        return fibArray[n];
    }

    public static void main(String[] args) {
        int n = 10; // Change n to whatever Fibonacci number you want to calculate
        System.out.println(fibonacciRecursive(n));
        System.out.println(fibonacciDynamic(n));
    }
}
