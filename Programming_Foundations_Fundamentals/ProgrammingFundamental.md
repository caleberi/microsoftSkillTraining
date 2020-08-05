# Programming Fundamentals 

Programming is more like creating a set of instruction for  the computer to follow . However , Computer only understand 0s and 1s  ,so this code are converted from human readable language to machine language using either an assembler/ interpreter / or compiler.

## Using python  

## Installation

* make sure you downloaded the latest version of Python from <http://www.python.org/downloads>.

## Troubleshooting Installation Issues

* If you are using an operating system other than Windows or Mac, you can find instructions for how to download Python here.
* If the python3 command is not available on the command line, make sure you downloaded the latest version of Python from <http://www.python.org/downloads>.
* If you’re using Windows and are having trouble accessing the Python interpreter on the command line, you can walk through the information in the official Python FAQ.
* If you are receiving an error that you don’t understand, you can paste it into the search box on Stack Overflow to look for a possible solution.

* Download either of this code editor [vscode/sublime-text] or any other code editor

## First Line of Code

write this pythonic line of code to get started . you can use either a code editor / python IDE.

```
print("Hello World\n")
```

## Why Python ?

Python is a general programming language for virtually any type of programmatic area / task .

## Variables and  data types

variables are containers  for  storing  certain  values.
variables in python  can be represented using letters,number and underscore.They cannot however,start  with number,special character or even have space between them. variable name should not be keyword.
```
        name = 42 #valid
        score_grade = "A" #valid
        ?name =90 #invalid
        student name = "sola" #invalid
```

## Conditional  Code

Use of if,if-elif,if-else statement  to perform conditional checks using relational operator and logical operator e.g ==,!=,<=,>=,<,> & and,or,not
```
if (condition):
        #statements
elif (condition):
         #statements
else
```

## Modular Code

use the following structure to create a function

```
        def function_name(parameters):
                """
                        functional documentation
                """
                 #functional body
                return  value
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)