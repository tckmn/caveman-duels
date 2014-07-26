public class ViceLeader {

    public static void main(String[] args) {
        if (args.length == 0 || !args[0].contains(",")) {
            System.out.print("S");
            return;
        }
        String[] history = args[0].split(",");
        int mySharpness = getSharpness(history[0]);
        int enemySharpness = getSharpness(history[1]);

        // enough sharpness to strike until end of game
        if (100 - history[0].length() <= mySharpness) {
            System.out.print("P");
            return;
        }

        // sharpen while secure
        if (enemySharpness == 0) {
            System.out.print("S");
            return;
        }

        // enemy blocks the whole time and I didn't use this tactic on last turn
        if (isBlocker(history[1]) && history[0].charAt(history[0].length() - 1) != 'S') {
            System.out.print("S");
            return;
        }

        // TAKE HIM OUT!
        if (enemySharpness == 4 || mySharpness >= 5) {            
            System.out.print("P");
            return;
        }

        // enemy sharpens the whole time => sharpen to strike on next turn
        if (isSharpener(history[1])) {
            System.out.print("S");
            return;
        }

        System.out.print("B");
    }

    private static int getSharpness(String history) {
        int sharpness = 0;
        for (char move : history.toCharArray()) {
            if (move == 'S') {
                sharpness++;
            } else if ((move == 'P' && sharpness > 0) || move == '^') {
                sharpness--;
            }
        }
        return sharpness;
    }

    private static boolean isBlocker(String history) {
        if (history.length() < 3) {
            return false;
        }
        for (int i = history.length() - 1; i > history.length() - 3; i--) {
            if (history.charAt(i) != 'B') {
                return false;
            }
        }
        return true;
    }

    private static boolean isSharpener(String history) {
        if (history.length() < 3) {
            return false;
        }
        for (int i = history.length() - 1; i > history.length() - 3; i--) {
            if (history.charAt(i) != 'S') {
                return false;
            }
        }
        return true;
    }
}