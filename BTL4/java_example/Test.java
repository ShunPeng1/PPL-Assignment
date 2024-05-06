
public class Test {
    
    public static void foo(boolean[] arr) {
        arr[0] = 1.38 < 2;
    }

    public static void main(String[] args) {
        boolean[] arr = {false, false};
        foo(arr);
        io.writeBool(arr[0]);
        io.writeBool(arr[1]);
    }
    
}
