# Exception Handling 
# How can we raise an exception, WAP

# We can raise an exception by using "raise" keyword
# syntax : raise ExceptionName("exception message")

try:
    age = int(input("Enter your age : "))
    if age < 0 :
        raise ValueError
    print("Your age is : ",age)
except ValueError:
    print("Please, Enter valid age not invalid")

# OUTPUT: Enter your age : -10
# Please, Enter valid age not invalid
# Enter your age : 56
# Your age is : 56

# if you give the message in raise statement then 
# format is 

try:
    name = str(input("Enter your name : "))
    if name.isnumeric() :
        raise ValueError ("Please, Enter valid name not invalid")
    print("Your name is : ",name)
except ValueError as var:
    print(var)

#OUTPUT: Enter your name : 567
# Please, Enter valid name not invalid
# Enter your name : yuvraj
# Your name is : yuvraj