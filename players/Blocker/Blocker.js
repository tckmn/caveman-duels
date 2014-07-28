function sharpenStick()
{
    meDoesWhat = 'S';
}

function block()
{
    meDoesWhat = 'B';
}

function poke()
{
    meDoesWhat = 'P';
}

if(process.argv.length > 2)
{
    cavemenDidWhat = process.argv[2].split(',');

    meMoves = cavemenDidWhat[0];
    mePokes = meMoves.split('P').length - 1;
    meSharpens = meMoves.split('S').length - 1;
    meHasSword = meSharpens - mePokes >= 5;

    opponentMoves = cavemenDidWhat[1];
    opponentPokes = opponentMoves.split('P').length - 1;
    opponentSharpens = opponentMoves.split('S').length - 1;
    opponentHasSword = opponentSharpens - opponentPokes >= 5;

    chooseMove();
}else
{
    sharpenStick();
}

function chooseMove()
{
    if(opponentSharpens - opponentPokes > 0 && meMoves < 50)
    {
        block();
    }else
    {
         var attackChance =  Math.random() * (opponentSharpens - 5);
         var isDoingFirst = Math.random() < .42;

         if(opponentHasSword)
         {
             attackChance -= 2;
         }

         if(attackChance > 2)
         {
             block();
         }else
         {
             if(meHasSword)
             {
                 poke();
             }else
             {
                 if(meSharpens > 0)
                 {
                     if(isDoingFirst)
                     {
                         poke();
                     }else
                     {
                         sharpenStick();
                     }
                 }else
                 {
                     if(isDoingFirst || meSharpens === 0)
                     {
                         block();
                     }else
                     {
                         sharpenStick();
                     }
                 }
             }
         }
     }
}

console.log(meDoesWhat);