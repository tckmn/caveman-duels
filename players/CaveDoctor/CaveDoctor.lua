function stickPointy(history)
  local pointy=0
  for i in history:gmatch("[SP]") do
    if i=="S" then 
      pointy=pointy+1
    elseif pointy>0 then
      pointy=pointy-1
    end
  end
  return pointy
end
if arg[1]==nil then
  print("S")
else
  split=arg[1]:find(",")
  player=arg[1]:sub(0,split-1)
  opponent=arg[1]:sub(split+1)
  psharp=stickPointy(player)
  osharp=stickPointy(opponent)
  if osharp<1 or psharp>4 or (osharp>2 and osharp>psharp) or player:len()>95 then
    if (psharp>0) then print("P")--We're losing/about to win or time's running out
    else print("S")--uh-oh
    end
  else
 amatch=false
  for x,y,z in opponent:gmatch("(B*)(S+)(B*)$") do
    if (z:len()>3 and player:sub(player:len())=="B") or (x:len()>z:len() and x:len()>0 and z:len()>0) then print("S")
    elseif z:len()==0 and y:len()>1 then print("P")--poke if there are successive sharpens
    else print("B")
    end
    amatch=true
    break
  end
  if not amatch then print("B") end
  end
end