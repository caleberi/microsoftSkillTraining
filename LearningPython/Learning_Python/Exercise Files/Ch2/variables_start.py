# 
# Example file for variables
#

# Declare a variable and initialize it
f=0
print(f)
f="abc"


# # re-declaring the variable works


# # ERROR: variables of different types cannot be combined
# print("This is a string "+23)
print("This is a string "+str(23))

# Global vs. local variables in functions

def someFunc():
        # global f
        f="def"
        print(f)
        
someFunc()
del f # for deleting variable 
print(f)