    public class CaveMonkey {

    public static void main(String[] args) {
        System.out.println(new CaveMonkey().fight(args));;
    }

    private int[] used;
    private int[][] dna;

    public CaveMonkey() {
        this.dna = new int[][] { //dna is found by evolutionary algorithm and mating with neanderthalers
            {1, 1, 2, 0, 2, 2, 0, 1, 1, 2, 0, 0, 0, 1, 2, 0, 2, 2, 0, 2, 2, 1, 1, 2, 1, 0, 1, 2, 0, 0, 0, 2, 2, 1, 2, 0},
            {0, 1, 2, 2, 0, 2, 0, 1, 2, 1, 0, 2, 2, 1, 2, 1, 1, 0, 0, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 2, 0, 0, 0, 2, 1, 2},
            {1, 0, 2, 0, 2, 2, 0, 1, 1, 0, 1, 2, 0, 2, 1, 2, 0, 2, 1, 1, 1, 0, 1, 0, 2, 2, 0, 0, 0, 0, 2, 1, 2, 0, 1, 0},
        };
        this.used = new int[dna[0].length];
    }

    private static final String[] I_DO = new String[] { "S", "B", "P" };
    private static final int[][] LOOKUP_TABLE = {
            { -1, -1, 0, 0, 0, 0, 0, 1, 1 }, // me
            { -1, 0, 0, -1, 0, 1, 0, 0, 1 }, // ugly you
    };

    public String fight(String[] input) {
        if (input.length == 0) {
            return "S";
        }
        String[] s = input[0].split(",");
        char[] me = s[0].toCharArray();
        char[] bleh = s[1].toCharArray();

        int stickMe = 0;
        int stickStupid = 0;
        for (int i = 0; i < me.length; i++) {
            // i can math!
            int code = ((((me[i] % 4) + (me[i] % 2)) / 2) * 3)
                    + (((bleh[i] % 4) + (bleh[i] % 2)) / 2);
            stickMe += LOOKUP_TABLE[0][code];
            stickStupid += LOOKUP_TABLE[1][code];
            int played = Math.min(5, stickMe) * 6 + Math.min(5, stickStupid);
            used[played]++;
        }

        stickMe = Math.max(0, stickMe);
        stickStupid = Math.max(0, stickStupid);

        int dnaLookup = Math.min(5, stickMe) * 6 + Math.min(5, stickStupid);
        String move = I_DO[dna[used[dnaLookup]%3][dnaLookup]];
        if(stickMe == 0 && move.equals("P")) {
            return "B";
        }
        return move;
    }
}