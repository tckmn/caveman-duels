import System.Environment


-- Tell caveman next move

next move
    | end with sharp stick  = poke with (what have)
    | they no poky          = sharpen stick
    | me have sword         = poke with sword
    | soon them have sword  = try poke or sharpen
    | soon have own sword   = fear pokes
    | think them want sword = sharpen stick
    | getting bored now     = sharpen stick
    | otherwise             = block poky stick


-- How fancy techno computer program know?

    where
        end with sharp stick = pokiness my stick >= moves before fight boring
        they no poky  = pokiness their stick == 0
        me have sword = pokiness my stick >= 5
        soon "them" have sword = pokiness their stick == 4
        soon have "own" sword  = pokiness my stick == 4
        try poke or sharpen = if pokiness my stick > 0
                              then poke with stick
                              else sharpen stick
        fear pokes = count 2 (block poky stick) and (sharpen stick)
        think them want sword = pokiness their stick == 3
        getting bored now = those last 2 mine same

        what have
            | me have sword = sword
            | otherwise     = stick



-- Rest not for caveman - only techno computer

        moves before time up = time - (length . fst $ move)

        and   = my
        mine  = my
        my    = fst move
        their = snd move

        before = "before"
        bored  = "bored"
        boring = "boring"
        have   = "have"
        no     = "no"
        now    = "now"
        own    = "own"
        pokes  = "pokes"
        same   = "same"
        sharp  = "sharp"
        them   = "them"
        want   = "want"


fight = 100


main = do
    movesHistoryEtc <- getArgs
    putStrLn . next . basedOn $ movesHistoryEtc


basedOn = movesOfEachCaveman . history

history []    = ""
history (h:_) = h

movesOfEachCaveman "" = ("", "")
movesOfEachCaveman h  = (\(a, b) -> (a, tail b)) . span (/= ',') $ h


sharpened = 'S'
poked     = 'P'
blocked   = 'B'

times m = length . filter (== m)


with  = "WITH"
poky  = "POKY"
sword = "SWORD"
stick = "STICK"

sharpen stick    = "SHARPEN " ++ stick
block poky stick = "BLOCK " ++ poky ++ " " ++ stick
poke with stick  = "POKE " ++ with ++ " " ++ stick


pokiness stick is = foldl countPokiness 0 stick

countPokiness pokyPoints 'P'
    | pokyPoints > 0         = pokyPoints - 1
    | otherwise              = 0
countPokiness pokyPoints 'S' = pokyPoints + 1
countPokiness pokyPoints  _  = pokyPoints


allLast n x xs = all (== x) $ take n . reverse $ xs

those previous n moves same = ((length moves) >= n)
                           && (allLast n (last moves) moves)

count n firstMoves moveHistory lastMove = if allLast n fm moveHistory
                                          then lastMove
                                          else firstMoves
    where fm = head firstMoves