# #is used for comments in Python
#Print command --Yay I ran my first python code
print("Hello, world!")

#Python allows using single quotes as well to define a string : This is helpful in case I have a string containing ("") as above 
print('My favorite quote is "To be or not to be."')

#Statements are executed in order
print("Line1")
print("Line2")

#Variables
message ="This string is stored in a variable"
print(message)
print(message)

#Variable naming : Only letters and underscores, Do not start with numbers

capital_of_uk ="London"
print(capital_of_uk)

#In python we generally use Snake case i.e as below (WORDS ARE LOWER CASE AND ARE SEPERATED BY UNDERSCORE)
snake_case = "hello_world"
print(snake_case)

#Reassiging variables in Python
#Values will be updated 
message = "this is message1"
print(message)
message = "this is message2"
print(message)

#Multiple Assignments x, y, z = "a", "b", "c"
x,y = 10, 20
print(x)
print(y)

x, y = y, x
print(x)
print(y)

#Types
#Dynamic Typing : No need to declare type
age =25              #integer
temperature =98.6    #floating-point number
is_true =True        #boolean
name ="Neeha"        #string
my_list =[1,2,300]   #list

#We can print the type of a variable using type print(type(age))
print(type(age))
print(type(temperature))
print(type(is_true))
print(type(name))
print(type(my_list))

#Dynamic Typing in Python : You can  change the type of a variable after it has been created
#This should generally be avoided (As it is error prone)
variable =10;
print(type(variable))
variable = "New Value Assigned to the variable"
print(type(variable))

#Type casting in Python
variable =10.9
print(int(variable))

#Empty variable : Npne is used to create a variable with no value assigned
variable = None
print(variable)

#Operators 
arithmetic_operators_add= 10 + 5
arithmetic_operators_sub = 10 - 5
arithmetic_operators_mul = 10 * 5
arithmetic_operators_div = 10 / 5 #Div always gives float result
print(arithmetic_operators_div)
#If one of the operator is float , it results in float 

#Order of operations ( paranthesis, exponentials, Add,sub (left to right), mul,div (left to right))

#Floor Division
x,y =8,3
print(x//y)
#Modulus Operator
print(x%y)
#Exponentation
print(x**y)