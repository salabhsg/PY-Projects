#Excercise (3)======================================>>>>>>>>>>>>>>>>>>>>>>
#You will need to write a format string which prints out the 
# data using the following syntax:
#  Hello John Doe. Your current balance is $53.44.

data = ("John", "Doe", 53.44)
format_string = "Hello"

print("%s %s %s. Your current balance is $%.2f."%(format_string,data[0],data[1],data[2]))

#=======================================

#first_name = "John"
#last_name = "Doe"
#balance = 53.44

#print("Hello %s %s. Your current balance is $%.2f."%(first_name,last_name,balance))

#========================================

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)