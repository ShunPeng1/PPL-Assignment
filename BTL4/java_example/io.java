

import java.io.*;

//import bkool.codegeneration.IllegalRuntimeException;


public class io {
	//private static final DataInputStream input = new DataInputStream(System.in);
	public static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	public static Writer writer = new BufferedWriter(new OutputStreamWriter(System.out));
	
	//public io(String name) throws IOException {
		
	//}
            
          
	/** reads and returns an integer value from the standard input
	 *	@return int an integer number read from standard input
	 */
	public static int readInt()  {
        String tmp = ""; 
		try {
			tmp = input.readLine();
            return Integer.parseInt(tmp);
		} catch (IOException e) {
			e.printStackTrace();
		} catch (NumberFormatException e) {
            e.printStackTrace();
        }
		return 0;
	}
	
		
    /** print out the value of the integer i to the standard output
     *	@param i the value is printed out
     */
    public static void writeInt(int i) {
    	
        System.out.print(i+"");
    		
    }
   
    /** same as putInt except that it also prints a newline
     *	@param i the value is printed out
     */	
    public static void writeIntLn(int i)  {
    	System.out.println(i+"");
    }
    
    /** return a floating-point value read from the standard input
     *	@return float the floating-point value
     */
    public static float readFloat()  {   
    	String tmp ="";
        try {
            tmp = input.readLine();
			return Float.parseFloat(tmp);
		} 
    	catch (IOException e) {
			e.printStackTrace();;
		}
        catch (NumberFormatException e) {
            e.printStackTrace();;
        }
        return 0.0F;
	}

    /** print out the value of the float f to the standard output
     *	@param f the floating-point value is printed out
     */
    public static void writeFloat(float f)  {
    	System.out.print(f+"");
    }
    
    /** same as putFloat except that it also prints a newline
     *	@param f the floating-point value is printed out
     */
    public static void writeFloatLn(float f)  {
    	System.out.println(f+"");
    }
    
	/** reads and returns a boolean value from the standard input
	 *	@return int a boolean value read from standard input
	 */
	public static boolean readBoolean() {
        String tmp = "";
		try {
            tmp = input.readLine();
			if (tmp.equalsIgnoreCase("true"))
                return true;
            else //if (tmp.equalsIgnoreCase("false"))
                return false;
           // else throw new IllegalRuntimeException(tmp);
		} catch (IOException e) {
			e.printStackTrace();
		}
		return false;
	}

    /** print out the value of the boolean b to the standard output
     *	@param b the boolean value is printed out
     */
    public static void writeBoolean(boolean b)  {
    	System.out.print(b+"");
    }
    
    /** same as putBoolLn except that it also prints a new line
     *	@param b the boolean value is printed out
     */
    public static void writeBooleanLn(boolean b) {
    	System.out.println(b+"");
    }
    /** reads and returns a boolean value from the standard input
     *  @return int a boolean value read from standard input
     */
    /*public static String Str() {
        String tmp = "";
        try {
            tmp = input.readLine();
            return tmp;
        } catch (IOException e) {
        	e.printStackTrace();
        }
        return tmp;
    }*/

    /** prints the value of the string to the standard output
     *	@param a the string is printed out
     */
     public static String readStr() {
    	 String tmp ="";
        try {
            tmp = input.readLine();
            return tmp;
        } 
        catch (IOException e) {
            e.printStackTrace();;
        }
        catch (NumberFormatException e) {
            e.printStackTrace();;
        }
        return tmp;
    }
    
    /** same as putString except that it also prints a new line
     *	@param a the string is printed out
     */
    public static void writeStr(String a)  {
    	System.out.print(a);
    }
    /** print out an empty line
     **/
    public static void writeStrLn(String a)  {
    	System.out.println(a);
    }
    
    public static void close() {
    	try {
    		writer.close();
    	} catch (IOException e) {
			 e.printStackTrace();
		}
    }

    /** 
     * Thuan Code
     * 
    */

    public static boolean readBool() {
        return readBoolean();
    }

    public static void writeBool(boolean b) {
        writeBooleanLn(b);
    }
    
    public static float readNumber() {
        return readFloat();
    }

    public static void writeNumber(float f) {
        writeFloatLn(f);
    }
	
    public static String readString() {
        return readStr();
    }

    public static void writeString(String a) {
        writeStrLn(a);
    }

    
}

