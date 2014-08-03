public class Sicillian {

    public static void main(String[] args) {

        if (args.length == 0) System.out.println("S");
        else {
            //get and analyze history
            String[] history = args[0].split(",");
            Caveman vizzini = new Caveman(history[0].toCharArray());
            Caveman fool = new Caveman(history[1].toCharArray());
            Think divine = new Think(history[0].toCharArray(),history[1].toCharArray());

            //The Sicillian always thinks and makes a logical decision before acting...
            char onlyAFool = divine.clearly(vizzini.getSharpness(),fool.getSharpness());

            //Never go in against a Sicillian when death is on the line!
            if(onlyAFool == 'S') {
                if(!vizzini.weaponless()) poke();
                else sharpen();
            }
            else if(onlyAFool == 'P') {
                if(vizzini.hasSword()) poke();
                else block();
            }
            else if(onlyAFool == 'B') sharpen();

            else {          // Inconceivable!

                //if he's a sharpener, poke him where it hurts!
                if(fool.isSharpener()) {
                    if(vizzini.getSharpness() >= 2) poke();  //don't ever go weaponless, else you give him the advantage
                    else sharpen();
                }               
                //if he's a blocker, get sword and break through his defense
                else if(fool.isDefensive()) {
                    if(vizzini.hasSword()) poke();
                    else sharpen();
                }
                // fool doesn't have a disposition to do anything in particular
                else {
                    //he could be sharpening and blocking to get a sword in which case his sharpness will be higher
                    //or a random, which will average a lower sharpness
                    if (fool.getSharpness() <= 2) { //assume random
                        if(vizzini.hasSword()) poke();
                        else if(fool.weaponless()) sharpen();
                        else block();
                    }
                    else {
                        if(vizzini.hasSword()) poke();
                        else if(vizzini.getSharpness() > fool.getSharpness()) sharpen();    //we can win race to sword
                        else if(vizzini.getSharpness() >= 2 || (!vizzini.weaponless() && fool.onEdge())) poke();
                        else sharpen();
                    }
                }
            }           
        }
    }   //end of main

    private static void poke() {
        System.out.println("P");
    }
    private static void block() {
        System.out.println("B");
    }
    private static void sharpen() {
        System.out.println("S");
    }
}
class Think {
    private char[][] cleverman = new char[6][6];    //tracks what the enemy does in a particular situation 
    private int mySharpness;
    private int enemySharpness;
    public Think(char[] myAction, char[] enemyAction) {
        //init variables
        mySharpness = 0;
        enemySharpness = 0;

        for(int i = 0; i < myAction.length; i++) {
            //remember what enemy did last time
            cleverman[mySharpness][enemySharpness] = enemyAction[i];
            //System.out.println("When I was at ("+mySharpness+") and he was at ("+enemySharpness+") he did ("+enemyAction[i]+")");

            //calculate my sharpness
            if(myAction[i] == 'S') mySharpness++;
            else if(myAction[i] == 'P') mySharpness--;
            if(mySharpness < 0) mySharpness = 0; //ensure multiple pokes don't create a negative sharpness
            //calculate my enemy's sharpness
            if(enemyAction[i] == 'S') enemySharpness++;
            else if(enemyAction[i] == 'P') enemySharpness--;
            if(enemySharpness < 0) enemySharpness = 0; //ensure multiple pokes don't create a negative sharpness
        }   
    }
    public char clearly(int myAction, int enemyAction) {
        if(myAction > 5) myAction = 5;
        if(enemyAction > 5) enemyAction = 5;
        return cleverman[myAction][enemyAction];
    }
}
class Caveman {
    private int sharpness;
    private int disposition;    //Finite State Machine: how inclined the caveman is toward blocking (0) or sharpening (4)
    public Caveman(char[] action) {
        sharpness = 0;
        disposition = 1;        //assume a slightly defensive disposition
        for (int i = 0; i < action.length; i++) {
            if(action[i] == 'S') {
                sharpness++;
                disposition++;
            }
            else if(action[i] == 'P') sharpness--;
            else disposition--;                     //blocking
            if(sharpness < 0) sharpness = 0; //ensure multiple pokes don't create a negative sharpness
            if(disposition > 4) disposition = 4;
            else if(disposition < 0) disposition = 0;
        }
    }
    public int getSharpness() {
        return sharpness;
    }
    public boolean weaponless() {
        return sharpness == 0;
    }
    public boolean hasSword() {
        return sharpness >= 5;
    }
    public boolean onEdge() {
        return sharpness == 4;
    }
    public boolean isDefensive() {
        return disposition == 0;
    }
    public boolean isSharpener() {
        return disposition == 4;
    }
    public int getDisposition() {
        return disposition;
    }
}