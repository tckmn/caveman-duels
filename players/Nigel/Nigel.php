<?php
// Seed the random number generator
srand(time());

// Simple function output chosen move
function move($m)
{
    echo $m;
    echo "\n";
    exit;
}

// Make stick sharp if first move
if (sizeof($argv) == 1)
    move("S");

// Grab the list of moves
$moves = explode(",", $argv[1]);    
$mySharpness = 0;
$opSharpness = 0;

// Loop through all previous moves and calculate sharpness
for ($i=0; $i<strlen($moves[0]); $i++)
{
    $myMove = substr ($moves[0], $i, 1);
    $opMove = substr ($moves[1], $i, 1);
    if ($myMove == "S")     $mySharpness++;
    if ($opMove == "S")     $opSharpness++; 
    if ($myMove == "P" && $mySharpness > 0)     $mySharpness--;
    if ($opMove == "P" && $opSharpness > 0)     $opSharpness--;     
}

// We somehow have a sword.. ATTACK!
if ($mySharpness > 4)
    move("P");

// Opponent is blunt, guarenteed upgrade!
if ($opSharpness < 1)
    move("S");          

// If we're sharp, either block or poke, unless OP is near a sword
if ($mySharpness > 0)
{
    // Oppenent is halfway to a sword.. ATTACK!
    if ($opSharpness > 2)
        move("P");  

    if (rand(0,1) == 0)     move("P");
    else                    move("B");
}

// If we're blunt, either sharpen or block
else
{
    if (rand(0,1) == 0)     move("S");
    else                    move("B");  
}

?>