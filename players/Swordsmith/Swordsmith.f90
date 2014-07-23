program Swordsmith
   implicit none
   integer :: mySharp,ierr
   logical :: lexist

   inquire(file="SwordsmithSharp.txt",exist=lexist)
   if(lexist) then
      open(unit=10,file="SwordsmithSharp.txt",status='old')
      read(10,*,iostat=ierr) mySharp
      if(ierr/=0) then
         mySharp = 0
      endif
   else
      mySharp = 0
      open(unit=10,file="SwordsmithSharp.txt",status='new')
      write(10,*) mySharp
   endif
   close(10)

   if(mySharp < 5) then
      print*,"S"
      open(unit=10,file="SwordsmithSharp.txt",status='old')
      mySharp = mySharp + 1
      write(10,*) mySharp
      stop
   endif
   print *,"P"
end program Swordsmith