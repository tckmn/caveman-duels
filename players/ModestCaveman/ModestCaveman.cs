using System;
using System.Collections.Generic;

namespace ModestCaveman
{
    class Program
    {
        static char DecideNextMove(char[] playerHistory, char[] opponentHistory)
        {
            int playerSharpness = 0, opponentSharpness = 0;

            for (int i = 0; i < playerHistory.Length; i++)
            {
                switch (opponentHistory[i])
                {
                    case 'P': if (playerHistory[i] == 'P') playerSharpness--; break;
                    case 'B': if (playerHistory[i] == 'P') playerSharpness--; break;
                    case 'S': opponentSharpness++; break;
                    default: throw new ArgumentException(string.Format("Invalid input symbol provided: symbol {0}", opponentHistory[i]));
                }
                switch (playerHistory[i])
                {
                    case 'P': if (opponentHistory[i] == 'P') opponentSharpness--; break;
                    case 'B': if (opponentHistory[i] == 'P') opponentSharpness--; break;
                    case 'S': playerSharpness++; break;
                    default: throw new ArgumentException(string.Format("Invalid input symbol provided: symbol {0}", playerHistory[i]));
                }
            }

            if (opponentSharpness < playerSharpness) return 'P';
            if (opponentSharpness > playerSharpness) return 'B';
            if (opponentSharpness == 0) return 'S';
            if (opponentSharpness == playerSharpness) return 'P';
            return ((new Random().Next() & 1) == 1) ? 'B' : 'S';
        }

        static void Main(string[] args)
        {
            if (args.Length < 1) { Console.Write('S'); return; }

            string[] input = args[0].Split(',');

            if (input.Length < 2)
                throw new ArgumentException("Malformatted arugment. Argument expected to be in form \"(S|P|B),(S|P|B)\"");

            char[]
                playerHistory = input[0].ToCharArray(),
                opponentHistory = input[1].ToCharArray();

            if (playerHistory.Length != opponentHistory.Length)
                throw new ArgumentException("Number of player moves and number of opponent moves are not equal");

            Console.Write(DecideNextMove(playerHistory, opponentHistory));
        }
    }
}