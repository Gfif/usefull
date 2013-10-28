// Daily push-up calculator
import java.io.*;

public class pushup {
	public static void main(String[] args) {
		try {
			InputStream fs = new FileInputStream("pushup.txt");
			Integer n = fs.read();
			System.out.println((String)n);
			fs.close();
		}
		catch (Exception e) {
    		System.err.println("Error: " + e.getMessage());
    	}
	}
}