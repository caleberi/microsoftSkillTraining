#
# Example file for working with functions
#

# define a basic function
def f1():
        print("I am a function")


# function that takes arguments
def f2(x):
        print(x**2)

# function that returns a value
def cube(x):
        return x**3

# function with default value for an argument
def power(x,n=1):
        result=1
        for i in range(n):
                result=result*x
        return  result

#function with variable number of arguments
def multi_add(*args):
        total=0
        for i in args:
                total = total+i
        return total

print(f1)
print(f1())
print(f2(2))
print(cube(4))
print(power(2,5))
print(multi_add(1,2,3,4,5,6,7,8,9))