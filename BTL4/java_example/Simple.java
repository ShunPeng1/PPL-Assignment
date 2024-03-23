public class Simple {
    public static float b = 3;
    public static void main(String[] args) {
        boolean a = true;
        if (a) {
            int c = 5;
            writeNumber(c);
        }
        else {
            int c = 6;
            writeNumber(c);
        }
        
    }
    
    public static void writeNumber(int number) {
        System.out.println(number);
    }
}
