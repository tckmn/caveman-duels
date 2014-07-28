public class PeriodicalCicadaCaveman
{
  const int Periodic = 13; //Could be 17
  public static void Main(string[] args)
  {
    if (args.Length == 0) 
    {
          System.Console.WriteLine("S");
          return;
    }
    var arg1 = args[0];
    if(arg1.Length == 0) 
    {
        //Always start with a sharp stick
        System.Console.WriteLine("S");
        return;
    }
    var myHistory = arg1.Split(',')[0];
    var theirHistory = arg1.Split(',')[1];
    int sharpness = 0;
    int timeElapsed =  myHistory.Length;

    for(int i = 0; i < timeElapsed; i++)
    {
        if(myHistory[i] == 'S')  
        {
            sharpness++;
        }
        if(myHistory[i] == 'P')
        {
            sharpness--;
        }
    }

    if((myHistory.Length % 13) == 0 
            || timeElapsed > 90 // Running out of time! To hell with the routine
        )
    {
        //The Secada strikes!
        if(sharpness > 1)
        {
            System.Console.WriteLine("P");
            return;
        }
        else
        {
            System.Console.WriteLine("S"); 
            return;
        }
    }
    System.Console.WriteLine("B"); 

  }

}