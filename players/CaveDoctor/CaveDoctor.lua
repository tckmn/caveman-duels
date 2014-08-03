caveman={havePointyStick=function (t)     
   local pointy=0   
   for i in t.stick:gmatch("[SP]") do
    if i=="S" then 
      pointy=pointy+1
    elseif pointy>0 then
      pointy=pointy-1
    end   
   end 
 t.sharp=pointy>0
 t.lastmove=t.stick:sub(t.stick:len())
 return pointy 
 end,
    Stupid=function (stick)--I put way to much effort in this...
      o = {} 
      setmetatable(o, caveman)
      o.smartness=0
      o.stick=stick
      caveman.__index = caveman
      return o
    end,
     Smart= function (stick)
      o ={} 
      setmetatable(o, caveman)
      o.smartness=100
      o.stick=stick
      caveman.__index = caveman
      return o
    end
       }


    if arg[1]==nil then  
       print("S")
    else   
      split=arg[1]:find(",")  
      me=caveman.Smart(arg[1]:sub(0,split-1)) 
      he=caveman.Stupid(arg[1]:sub(split+1)) 
      mesharp=me:havePointyStick()  
      hesharp=he:havePointyStick()
      if not he.sharp and mesharp<5 then print("S")--Go for the sword  
      elseif mesharp>4 or me.stick:len()>93 then
         if (mesharp>0) then print("P")--We're losing/about to win or time's running out
         else print("S")--uh-oh
         end
      else 
         u,g,h=he.stick:match("(B+)S+(B+)S+(B+)$")
         g,u,h=he.stick:match("(P+)S+(P+)S+(P+)$")
         if u~=nil and u==g and g==h then 
            if not me.sharp then print("S")
            else print("P")
            end
         elseif me.stick:match("SBSB$")~=nil then print("B")
         elseif he.stick:len()>7 and he.stick:match("P")==nil and me.lastmove~="S" then print("S")
         else
         b,u,h=he.stick:match("(B*)(S+)(B*)$")
         if u~=nil then
             if (h:len()>3 and me.lastmove=="B") or (b:len()>h:len() and b:len()>0 and h:len()>0) then print("S")
             else print("B")
             end
          else print("B")
          end   
      end   
   end 
end