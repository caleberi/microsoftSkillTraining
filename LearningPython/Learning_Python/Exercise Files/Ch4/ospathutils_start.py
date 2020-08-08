#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
  # Print the name of the OS
  print(os.name)

  # Check for item existence and type
  print("item exist"+str(path.exists("textfile.txt")))
  print("is file "+str(path.isfile("textfile.txt")))
  print("is dir "+str(path.isdir("textfile.txt")))
  
  # Work with file paths
  print("item exist"+str(path.realpath("textfile.txt")))
  print("item path and name"+str(path.split(path.realpath("textfile.txt"))))
  
  # Get the modification time
  ti = time.ctime(path.getmtime("textfile.txt"))

  
  # Calculate how long ago the item was modified

if __name__ == "__main__":
  main()
