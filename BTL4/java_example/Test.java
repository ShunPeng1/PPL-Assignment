
public class Test {
    
    public static int foo(int[] a, String b) {
        for (int i = 0; i < 5; i++) {
            a[i] = i * i + 5;
        }
        return -1;
    }
    public static int[] arr = new int[5];
    public static void main(String[] args) {
        
        String b = "mommy";
        int t = foo(arr, b);
        System.out.println(t < 0);
        for (int i = 0; i < 5; i++) {
            System.out.println(arr[i]);
        }
    }
    
}
