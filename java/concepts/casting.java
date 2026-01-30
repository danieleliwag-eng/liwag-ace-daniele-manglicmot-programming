public class casting {
    public static void main(String[] args) {
        // casting : it can use the data type to another
        // example
        float d = 8.99f;
        double g  = 4.55d;
        System.out.println(d);
        System.out.println(g);
       

        long j = 8;
        System.out.print(j);
         
        // narrowing casting
        // example : double myDouble = 9.78d;
//  int myInt = (int) myDouble; // Manual casting: double to int

// System.out.println(myDouble); // Outputs 9.78
// System.out.println(myInt);    // Outputs 9
        // float f = 5.55f;
        // double d = f;
        // System.out.println(f);
        float f = 5.55f;
        int h = (int) f;
        System.out.println(f);
        System.out.println(h);
        // another example
        int y = 100;
        int u = 200;
        float final_answer = (float) u / y * 100f;
        // arguement_list
        System.out.println(final_answer); 

        // example
        int a =100;
        int v = 56;
        double finding_my_answer = (int) a / v * 200d;
        System.out.println(finding_my_answer);

    }
    
}
