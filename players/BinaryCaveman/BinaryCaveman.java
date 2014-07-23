public class BinaryCaveman { 

    public static void main(String[] args) {
        int timelapse = 0;
        if(args.length>0)
        {
            timelapse = ((args.length - 1) / 2);
        }
        switch(timelapse % 2) 
        {
            case 0: System.out.println('S'); 
                    break;
            case 1: System.out.println('P'); 
                    break;
        }
    }
}