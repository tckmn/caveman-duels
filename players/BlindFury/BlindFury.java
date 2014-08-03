public class BlindFury {

    public static void main(String[] args) {
            if(args.length == 0 || !args[0].contains(",")) {
                System.out.print("S");
                return;
            }

            String[] moves = args[0].split(",");
            int sharp = getSharp(moves[0]);
            int rageMeter = getRage(moves[0], moves[1]);


            if(rageMeter >= 0){
                //Urge to kill rising
                if(sharp > 0) {
                    System.out.println('P');
                    return;
                }
                else {
                    System.out.println('S');
                    return;
                }
            }
            else{
                //Not enough rage, lame it out.
                System.out.print('B');
                return;
            }
        }

       private static int getSharp(String mine) {
        int sharp = 0;

        for(char c : mine.toCharArray()) {
            if(c == 'S') {
                sharp++;
            }

            if(c == 'P') {
                sharp--;
            }
        }

        return sharp;
    }

 private static int getRage(String mine, String theirs) {
        int rage = 0;

        for(char c : mine.toCharArray()) {
            if(c == 'S') {
                rage++;
            }

            if(c == 'P') {
                rage--;
            }
        }

        for(char c : theirs.toCharArray()) {
            if(c == 'S') {
                rage--;
            }

            if(c == 'P') {
                rage++;
            }

            if(c == 'B') {
                rage+=2;
            }
        }

        return rage;
    }
}