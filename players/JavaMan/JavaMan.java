public class JavaMan
{
    public static void main(String[] args)
    {
        // input: SPB,SBB
        // me, enemy
        // S: sharpen, P: poke, B: block

        if (args.length == 0)
        {
            System.out.println("S");
        }
        else
        {
            String[] states = args[0].split(",");
            Player me = new Player(states[0].toCharArray());
            Player enemy = new Player(states[1].toCharArray());  //fixed thanks to Roy van Rijn

            if (me.hasSword())
            {
                System.out.println("P");
            }
            else if (!enemy.canPoke())
            {
                if (me.canPoke() && (Math.random() * 95) < states[0].length())
                {
                    System.out.println("P");
                }
                else
                {
                    System.out.println("S");
                }
            }
            else if (enemy.hasSword())
            {
                if (me.canPoke())
                {
                    System.out.println("P");
                }
                else
                {
                    System.out.println("S");
                }

            }
            else if (enemy.canPoke())
            {
                if (me.canPoke())
                {
                    if ((Math.random() * 95) < states[0].length())
                    {
                        System.out.println("P");
                    }
                    else
                    {
                        System.out.println("B");
                    }
                }
                else
                {
                    if ((Math.random() * 95) < states[0].length())
                    {
                        System.out.println("S");
                    }
                    else
                    {
                        System.out.println("B");
                    }
                }
            }
            else
            {
                System.out.println("S");
            }
        }
    }

}

class Player
{
    int sharpLevel;

    public Player(char[] state)
    {
        sharpLevel = 0;
        for (char c : state)
        {
            switch (c)
            {
            case 'S':
                sharpLevel++;
                break;
            case 'P':
                sharpLevel--;
                break;
            case 'B':
                break;
            default:
                System.out.println(c);
            }
        }
    }

    public boolean hasSword()
    {
        return sharpLevel > 4;
    }

    public boolean canPoke()
    {
        return sharpLevel > 0;
    }
}