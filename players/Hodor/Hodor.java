public class Hodor {
    public static void main(String[] args){

        String previousMoves = null;

        //account for no input
        if(args.length == 0){
            System.out.print('S');
            System.exit(0);
        }else{
            previousMoves = args[0];
        }

        //declare variables
        char action = 'S';
        int enemySharpens = 0, enemyPokes = 0, myPokes = 0, mySharpens = 0;
        String[] movesArray = previousMoves.split(",");
        char[] enemyMoves = movesArray[1].toCharArray(), myMoves = movesArray[0].toCharArray();

        //determine enemy sharpness
        for(int i=0; i<enemyMoves.length; i++){
            if(enemyMoves[i] == 'S'){
                enemySharpens++;
            }else if(enemyMoves[i] == 'P'){
                enemyPokes++;
            }
        }

        //block if opponent can poke, else sharpen
        if(enemySharpens - enemyPokes > 0){
            action = 'B';
        }else{
            action = 'S';
        }

        //determine my sharpness
        for(int i=0; i<movesArray[0].length(); i++){
            if(myMoves[i] == 'P'){
                myPokes++;
            }else if(myMoves[i] == 'S'){
                mySharpens++;
            }
        }

        //poke as much as possible if the game is about to end
        if((mySharpens-myPokes) > (100-enemyMoves.length)){
            action = 'P';
        }

        try{
            //sharpen if opponent blocks 2 times in a row and I didn't just sharpen
            if((enemyMoves[enemyMoves.length-1] == 'B') && (enemyMoves[enemyMoves.length-2] == 'B') && (myMoves[myMoves.length-1] != 'S')){
                action = 'S';
            }
            //poke if opponent sharpens twice in a row
            if((enemyMoves[enemyMoves.length-1] == 'S') && (enemyMoves[enemyMoves.length-2] == 'S')){
                action = 'P';
            }
            //poke if the opponent just sharpened/blocked then poked, has a blunt stick, and my stick isn't blunt
            if((enemyMoves[enemyMoves.length-2] != 'P') && (enemyMoves[enemyMoves.length-1] == 'P') && (enemySharpens-enemyPokes == 0) && (mySharpens - myPokes > 0)){
                action = 'P';
            }
        }catch (ArrayIndexOutOfBoundsException e){
            //not enough info
        }

        //poke if we have a sword
        if(mySharpens-myPokes > 4){
            action = 'P';
        }

        System.out.print(action);
    }
}