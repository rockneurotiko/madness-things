---------------------------------------- luabf.lua
-- lua brainf*** interpreter : by entreido at yahoo dot com
-- usage: put text like return "bf.prog.here" into a file you give as
-- a command line param
file = dofile(arg[1])
array = {}
ip = 0
p = 0
while 1 do
  ip = ip + 1
  x = strsub(file,ip,ip)
  if array[p] == nil then array[p] = 0 end
  if x == "+" then
    array[p] = array[p] + 1
  elseif x == "-" then
    array[p] = array[p] - 1
  elseif x == ">" then
    p = p + 1
  elseif x == "<" then
    p = p - 1
  elseif x == "," then
    array[p] = strbyte(read(1))
  elseif x == "." then
    write(strchar(array[p]))
  elseif x == "[" then
    lastlbrack = ip
    nextrbrack = strfind(file,"]",ip)
    if not nextrbrack then
      print("**Program terminated: No accompanying closing \"]\" for \"[\"")
      exit()
    elseif array[p] == 0 then
      ip = nextrbrack
    end
  elseif x == "]" then
    if not lastlbrack then
      print("**Program terminated: No accompanying opening \"[\" for \"]\"")
      exit()
    elseif array[p] ~= 0 then
      ip = lastlbrack
    end
  else
    print("**Program terminated: Invalid character `"..x.."'");
    exit()
  end
  if ip == strlen(file) then
    exit()
  end
end
---------------------------------------- eof





