#
# Example file for working with classes
#

class myClass():
          def method1(self):
                    print("method1")
          def method2(self,x):
                    print("method2" + str(x) )


class anotherClass(myClass):
          def method1(self):
                    myClass.method1(self)
                    print("another method1")
          def method2(self,x):
                    myClass.method2(self,x)
                    print("another method2" + str(x) )



def main():
  c= myClass()
  c.method1()
  c.method2(3)
  d = anotherClass()
  d.method1()
  d.method2(3)
  
if __name__ == "__main__":
  main()
