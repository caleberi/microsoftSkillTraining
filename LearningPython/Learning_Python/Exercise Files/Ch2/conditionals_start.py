#
# Example file for working with conditional statements
#

def main():
  x, y = 100, 100
  
  # conditional flow uses if, elif, else  
  if (x<y):
            st=" x is less than y"
  elif x==y:
            st=" x is equal to y"
  else:
            st=" y is less than x"
  # conditional statements let you use "a if C else b"
  print(st)
  a = 10 if(x<y) else 23
  print(a)

if __name__ == "__main__":
  main()
