import java.util.Random;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class SharpMan {
    public static void main(String[] args) {
        String arg = args != null && args.length > 0 ? args[0] : null;
        char action = action(arg);
        System.out.print(action);
    }

    protected static char action(String arg) {
        if (arg != null) {
            String[] split = arg.split(",");
            final int me = sharpness(split[0]);
            final int notMe = sharpness(split[1]);
            if (me > 4) {
                return 'P';
            } else if (me > 3) {
                return Math.random() >= 0.75 ? 'S' : 'P';
            } else if (notMe == 0 || notMe > 4) {
                return 'S';
            } else if (notMe == 1) {
                Matcher matcher = Pattern.compile("B+$").matcher(split[1]);
                if (matcher.find() && matcher.group().length() > new Random().nextInt(42) + 5) {
                    return 'S';
                }
                return 'B';
            } else if (notMe == 2) {
                return Math.random() >= 0.75 ? 'S' : 'B';
            } else if (notMe == 3) {
                return Math.random() >= 0.5 ? 'S' : (me < 3) ? 'P' : 'B';
            } else {
                return Math.random() >= 0.75 ? 'S' : 'P';
            }
        } else {
            return 'S';
        }
    }

    protected static int sharpness(String s) {
        int sharp = 0;
        for (char c : s.toCharArray()) {
            switch (c) {
                case 'P':
                    sharp = Math.max(0, sharp - 1);
                    break;
                case 'B':
                    break;
                case 'S':
                    sharp++;
                    break;
            }
        }
        return sharp;
    }
}