public class Gruntt {

public static void main(String[] args) {
    System.out.println(whatToDo(args));
}

private static String whatToDo(String[] args){
    int mySharpness = 0;
    int otherSharpness = 0;

    if (args.length > 0) {
        String[] ss = args[0].split(",");
        mySharpness = howSpiky(ss[0]);
        otherSharpness = howSpiky(ss[1]);
    } else {
        return "S";
    }

    if (mySharpness >= 5){
        return "P";
    }

    String res = wowoo(args[0].split(",")[1]);
    if ("P".equals(res) && mySharpness > 0) {
        return "P";
    } else if ("P".equals(res) && mySharpness == 0) {
        return "S";
    } else if ("S".equals(res) && !args[0].split(",")[0].endsWith("S")) {
        return "S";
    }

    if (otherSharpness == 4 && !args[0].split(",")[0].endsWith("P")){
        return "P";
    }

    if (otherSharpness == 0){
        return "S";
    }

    return "B";

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

private static String wowoo(String s){
    String s1 = "";
    String s2 = "";

    if (s.length() >= 4){
        s1 = s.substring(s.length() - 4);
    }

    if (s.length() >= 3){
        s2 = s.substring(s.length() - 3);
    }

    if ("SPSP".equals(s1)){
        return "P";
    } else if ("SSS".equals(s2)){
        return "P";
    } else if ("BBBB".equals(s1)){
        return "S";
    } else if ("SBSB".equals(s1)){
        return "P";
    }

    return null;
}

}