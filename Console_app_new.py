
import requests
import json

class Write():

 def __init__(self):
  pass

#Inherited class from base class Write  
class Write_to_console(Write):

 def __init__(self):
  Write.__init__(self)

 def print(self):
  print("Writing to Console....")
  print("Hello World")
  
 
#Inherited class from base class Write  
class Write_to_database(Write):
 
 def __init__(self):
  Write.__init__(self)
    
 def print(self):
  print("#Writing to DataBase.....")
  pass
  #Logic to write to DataBase
  
