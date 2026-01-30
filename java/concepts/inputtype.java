// Input type : to create a user input to find the finalanswer
import java.util.Scanner;
public class inputtype {
    public static void main(String[] args) {
        //sanner : to get the user input of import.java
        Scanner scanner = new Scanner(System.in);
        System.out.println("what is ur name");
        String name = scanner.nextLine();
        System.out.println("hello" +  ""+ name);

        // self-test
        Scanner liwagScanner = new Scanner(System.in);
        System.out.println("hello");
        String a = liwagScanner.nextLine();
        System.out.print("hi" + a );

        // another example
        Scanner danieleScanner = new Scanner(System.in);
        System.out.println("name");
        String b = danieleScanner.nextLine();
        System.out.println(b);
        

                
    }
    
}


