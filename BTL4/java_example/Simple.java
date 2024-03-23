public class Simple {
    public static int b = 1;
    public static void main(String[] args) {
        boolean a = true;
        if (a) {
            int c = 5;
            writeNumber(c);
        }
        else {
            writeNumber(b);
        }
        
    }
    
    public static void writeNumber(int number) {
        System.out.println(number);
    }
}
