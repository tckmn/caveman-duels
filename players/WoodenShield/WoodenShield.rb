def getSharpness (history)
    sharpness = 0
    for i in 0..history.length - 1
        case history[i]
        when 'S', 's'
          sharpness += 1
        when 'P', 'p'
          sharpness -= 1
        end
    end
    return sharpness
end

if ARGV.length == 0
    puts 'S' # At the first run, sharpen.
else
    inputParts = ARGV[0].split(',')
    myHistory = inputParts[0]
    opponentHistory = inputParts[1]
    mySharpness = getSharpness(myHistory)
    opponentSharpness = getSharpness(opponentHistory)
    if mySharpness == 0 && opponentSharpness == 0
        puts 'S' # It's safe to sharpen now, the opponent cannot poke.
    elsif mySharpness > 0 && opponentSharpness == 0
        puts 'P' # Poke, the chance that the opponent sharps now is higher than when he has more sharpness.
    elsif mySharpness > 0 && opponentSharpness == 4
        puts 'P' # It is likely that the opponent sharpens now, because he wants a sword.
    elsif mySharpness > 4
        puts 'P' # Me win! (hopefully...)
    elsif mySharpness == 0 && opponentSharpness == 4
        puts 'S' # Uh oh... sharpen anyway, it is unlikely, but there *is* still a small chance that the opponent will sharpen once more after he got a sword.
    elsif mySharpness > 0 && opponentSharpness > 4
        puts 'P' # Poke, just in case the opponent sharpens.
    elsif mySharpness == 0 && opponentSharpness > 4
        puts 'S' # Sharpen anyway, for the same reasons as above. 
    else
        puts 'B' # In all other cases, block!
    end       
end