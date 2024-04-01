
public class Test {
    
    static int[] x = {1,2,3,4,5};
    public static void main(String[] args) {
      
        int[] a = {1, 2, 3, 4, 5};
        
        int c = 4;
        a[c] = c;

        c = a[3];
    }
    

    public static void main2(){
        int [][] b = {{1, 2}, {3, 4}};
        
        b[0][1] = b[2][3];
        b[1] = b[0];

        int [] c = {1,2};
        b[0] = c;
        b[0][1] = 2;
    }

    public static void main3(){
        x[0] = 6;
        
    }
}
