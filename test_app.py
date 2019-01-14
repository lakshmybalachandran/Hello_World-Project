#Unit Test Module

import unittest
import requests


class TestStringMethods(unittest.TestCase):# inheriting unittest.TestCase class


# Unit Test for "Web Server" Availability using GET method
 def test_status_upandrun_check(self):
  base_url = "http://127.0.0.1:5000/"
  response = requests.get(base_url)
  self.assertEqual(response.status_code, 200)


#Unit Test for "Write_to_console" functionality check
 def test_console_function_check(self):
  base_url = "http://127.0.0.1:5000/"
  response = requests.get(base_url)
  title = response.text
  print( title)



#Unit Test for "Write_to_database" functionality check
  def test_database_function_check(self):
   pass
   #todo after enhancement


#Unit Test for "Hello World" title match check

 def test_title_check(self):
  base_url = "http://127.0.0.1:5000/"
  response = requests.get(base_url)
  title = response.text
  print( title)
  self.assertEqual(title,"Hello World")

#Unit Test for mentioned POST method
  
 def test_write_check(self):
  base_url = "http://127.0.0.1:5000/"
  body = {"Sub Title" : " Hello Crowe!"}
  response = requests.post(base_url,json=body)
  print(response.text)
  

if __name__ == '__main__':
 unittest.main()

