#include <iostream>
#include <cstdio>
#include <string>
#include <ctime>
#include <cstdlib>

using namespace std;
pair<int,int> next_state(int s_self,int s_enemy,int player_move,int enemy_move);
int simulation (int s_self,int s_enemy,int n_turn);

int to_int(char c)
{
    if (c=='S')
    {
       return 0;
    }
    else if (c=='P')
    {
         return 1;
    }
    else
    {
        return 2;
    }
}

int main(int argc,char * argv[])
{
    srand(time(0));
    int self=0;
    int enemy=0;
    int n_turn=0;
    //argc=2
    if (argc==1)
    {
       //New Game
       //printf("New Game :D\n");
    }
    else
    {
        //Process States
        string s(argv[1]);
        string s1,s2;
        for (int i=0; i<s.length(); i++)
        {
            if (s[i]==',')
            {
               s1=s.substr(0,i);
               s2=s.substr(i+1,i);
            }
        }
        for (int i=0; i<s1.length(); i++)
        {
            pair<int,int> p=next_state(self,enemy,to_int(s1[i]),to_int(s2[i]));
            self=p.first;
            enemy=p.second;
        }
        n_turn=s1.length();
    }
    //printf("self: %d,enemy: %d\n",self,enemy);
    int t_self,t_enemy,n_iter=1000,s_win=0,p_win=0,b_win=0;
    for (int i=0; i<n_iter; i++)
    {
        pair<int,int> p=next_state(self,enemy,0,rand()%3);
        s_win+=simulation(p.first,p.second,n_turn+1);
        p=next_state(self,enemy,1,rand()%3);
        p_win+=simulation(p.first,p.second,n_turn+1);
        p=next_state(self,enemy,2,rand()%3);
        b_win+=simulation(p.first,p.second,n_turn+1);
    }
    //printf("s_win: %d,p_win: %d,b_win: %d\n",s_win,p_win,b_win);
    if (s_win>=p_win && s_win>=b_win)
    {
       printf("S");
    }
    else if (p_win>=s_win && p_win>=b_win)
    {
         printf("P");
    }
    else
    {
        printf("B");
    }
    //system("PAUSE");
}

pair<int,int> next_state(int s_self,int s_enemy,int player_move,int enemy_move) //Playermove, enemymove
{
    int a=player_move;
    int b=enemy_move;
    if (a==0) //Sharpen
    {
             if (b==0)
             {
                return make_pair(s_self+1,s_enemy+1);
             }
             else if (b==1)
             {
                  if (s_enemy==0)
                  {
                     return make_pair(s_self+1,s_enemy);
                  }
                  else
                  {
                      return make_pair(-1,-1);
                  }
             }
             else
             {
                 return make_pair(s_self+1,s_enemy);
             }
    }
    else if (a==1) //Poke
    {
         if (b==0)
         {
            if (s_self>0)
            {
                return make_pair(9001,9001);
            }
            else
            {
                return make_pair(-1,-1);
            }
         }
         else if (b==1)
         {
            if (s_self>=5 && s_enemy<5)
            {
               return make_pair(9001,9001);
            }
            else if (s_self<=0)
            {
                return make_pair(-1,-1);
            }
            else
            {
                return make_pair(s_self-1,s_enemy-1);
            }

         }
         else if (b==2)
         {
              if (s_self>=5)
              {
                 return make_pair(9001,9001);
              }
              else if (s_self<=0)
                {
                    return make_pair(-1,-1);
                }
              else
              {
                  return make_pair(s_self-1,s_enemy);
              }
         }
    }
    else //Block
    {
        if (b==0)
        {
           return make_pair(s_self,s_enemy+1);
        }
        else if (b==1)
        {
             if (s_enemy>=5)
             {
                return make_pair(-1,-1);
             }
             else
             {
                 return make_pair(s_self,s_enemy-1);
             }
        }
        else
        {
            return make_pair(s_self,s_enemy);
        }
    }
}

int simulation (int s_self,int s_enemy,int n_turn)
{
    if (s_self==9001)
    {
       return 1;
    }
    else if (s_self==-1)
    {
         return 0;
    }
    int a=rand()%3;
    int b=rand()%3;
    if (n_turn>=100)
    {
       return 0;
    }
    if (a==0) //Sharpen
    {
             if (b==0)
             {
                return simulation(s_self+1,s_enemy+1,n_turn+1);
             }
             else if (b==1)
             {
                  if (s_enemy==0)
                  {
                     return simulation(s_self+1,s_enemy,n_turn+1);
                  }
                  else
                  {
                      return 0;
                  }
             }
             else
             {
                 return simulation(s_self+1,s_enemy,n_turn+1);
             }
    }
    else if (a==1) //Poke
    {
         if (b==0)
         {
            if (s_self<=0)
            {
                return 0;
            }
            else
            {
                return 1;
            }
         }
         else if (b==1)
         {
            if (s_self>=5 && s_enemy<5)
            {
               return 1;
            }
            else if (s_self<=0)
            {
                return 0;
            }
            else
            {
                return simulation(s_self-1,s_enemy-1,n_turn+1);
            }

         }
         else if (b==2)
         {
              if (s_self>=5)
              {
                 return 1;
              }
              else if (s_self<=0)
              {
                return 0;
              }
              else
              {
                  return simulation(s_self-1,s_enemy,n_turn+1);
              }
         }
    }
    else //Block
    {
        if (b==0)
        {
           return simulation(s_self,s_enemy+1,n_turn+1);
        }
        else if (b==1)
        {
             if (s_enemy>=5)
             {
                return 0;
             }
             else
             {
                 return simulation(s_self,s_enemy-1,n_turn+1);
             }
        }
        else
        {
            return simulation(s_self,s_enemy,n_turn+1);
        }
    }
}