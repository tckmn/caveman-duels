import System.Environment
import Data.Maybe
import Data.List

main :: IO ()
main = do
  args <- getArgs
  writeFile attackFile "F"
  let (me, he) = if not (null args) then processInput (head args) else ("", "")
      meSharpness = sharpness me
      heSharpness = sharpness he
  determineMove heSharpness meSharpness

attackFile :: FilePath
attackFile = "players/CarefulBot/attack.txt"

processInput :: String -> (String, String)
processInput input = splitAt (fromJust $ elemIndex ',' input) input 

sharpness :: String -> Int
sharpness moves = length (elemIndices 'S' moves) - length (elemIndices 'P' moves)

determineMove :: Int -> Int -> IO ()
determineMove heSharpness meSharpness =
  case (heSharpness, meSharpness) of (0, 5) -> attack
                                     (0, 0) -> unAttack
                                     (0, _) -> checkAttack
                                     (4, x) -> if x > 0 && x < 4 then attack else putChar 'S'
                                     (_, _) -> putChar 'B'

attack :: IO ()
attack = do
  writeFile attackFile "T"
  putChar 'P'

checkAttack :: IO ()
checkAttack = do
  file <- readFile attackFile
  putChar $ case file of "T" -> 'P'
                         "F" -> 'S'
                         _   -> 'B'

unAttack :: IO ()
unAttack = do
  writeFile attackFile "F"
  putChar 'S'