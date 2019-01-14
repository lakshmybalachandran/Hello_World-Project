# MAIN 

import Console_app_new

class Helloworld():
 
 def do_helloworld(self):

  filename = open("configfile.txt","r")
  line = filename.readlines()
  obj = Console_app_new.Write()

 # Selection Logic using configuration file
 
  if (line[0] == "console"):
   obj = Console_app_new.Write_to_console()
    
  else:
   obj = Console_app_new.Write_to_database()
  
 # calling Write to Console logic
  obj.print()
  


def main():

 obj_helloworld = Helloworld()
 obj_helloworld.do_helloworld()

main()
