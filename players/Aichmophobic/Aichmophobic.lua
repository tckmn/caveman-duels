if arg[1] == nil then
  response = "S"
elseif not arg[1]:match('SSSSS') == nil then
  --PANIC
  response = "B"
else  
  --Minds his own business and goes where he pleases
  math.randomseed(os.time())
  local rand = math.random();

  response = rand > 0.6 and "P" or "S"
end

print(response)