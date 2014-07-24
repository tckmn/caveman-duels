program Swordsmith
   implicit none
   integer :: mySharp,ierr,arg_count
   logical :: lExist
   character(38) :: filename = "players/Swordsmith/SwordsmithSharp.txt"

! check argument counts for initialization of storage file
   arg_count = command_argument_count()
   if(arg_count == 0) then
      inquire(file=filename,exist=lExist)
      mySharp = 0
      if(lExist) then
         open(unit=10,file=filename,status='replace')
      else
         open(unit=10,file=filename,status='new')
      endif
      write(10,*) mySharp
      close(10)
   endif

! open, read, & close the file for mySharp
   open(unit=10,file=filename,status='old')
   read(10,*) mySharp
   close(10)

! make decision
   if(mySharp < 5) then
      print '(a1)',"S"
      open(unit=10,file=filename,status='replace')
      mySharp = mySharp + 1
      write(10,*) mySharp
      stop
   endif
   print '(a1)',"P"
end program Swordsmith