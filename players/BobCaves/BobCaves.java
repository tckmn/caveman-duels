import java.util.Random;

public class BobCaves {

    public static void main(String[] args) {
        int mySharpness = 0;
    int otherSharpness = 0;

    //Boc counts
    if (args.length > 0) {
        String[] ss = args[0].split(",");
        mySharpness = howSpiky(ss[0]);
        otherSharpness = howSpiky(ss[1]);
    }
    // Bob thinks!
    Random rn = new Random();
    if (mySharpness == 0 && otherSharpness == 0){
        System.out.println( "S");
    }
    if (otherSharpness == 0 && mySharpness < 5 && mySharpness > 0){
        if (rn.nextBoolean()){
            System.out.println("P");
        } else {
            System.out.println("S");
        }
    } 

    if (mySharpness >= 5 || (otherSharpness >= 2 && mySharpness > 0)) {
        System.out.println("P");
    }

    if (rn.nextInt(5) > 3) {
        System.out.println("S");
    } 

    System.out.println("B");
    }

    private static int howSpiky(String s1) {
        int count = 0;
        char[] c1 = s1.toCharArray();
        for (int i = 0; i < c1.length; i++) {
        if (c1[i] == 'S') {
                count++;
            } else if (c1[i] == 'P'){
                count --;
            }
        }
        return count;
    }

}