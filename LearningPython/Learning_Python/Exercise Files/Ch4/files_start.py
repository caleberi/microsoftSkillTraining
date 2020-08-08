#
# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist
  # fs = open("textfile.txt","w+")
  fs = open("textfile.txt","r")

  # Open the file for appending text to the end


  # write some lines of data to the file
  # for i in range(10):
  #           fs.write("This is line " +str(i) + "\r\n")
  # close the file when done
  # fs.close()
  
  # Open the file back up and read the contents
  if fs.mode=="r":
            content = fs.read()
  print(content)
  fs.close()
    
if __name__ == "__main__":
  main()
