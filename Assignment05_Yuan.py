#Assignment 05 - Basic Math Operation
class BasicMathOperation:
    #Ask user to input name
    f_name = input("What is your first name:\n")
    l_name = input("What is your last name:\n")
    
    def __init__(self, first_name = f_name, last_name = l_name):
        self.__first_name = first_name
        self.__last_name = last_name

    #Greet User Method
    def greet_user(self):
        print("Welcome, " + self.__first_name + " " + self.__last_name + ".\n")

    #Add Number Method
    def add_num(self):
        num1 = int(input("Enter the 1st number:\n"))
        num2 = int(input("Enter the 2nd number:\n"))
        return print(num1 + num2)

#-----------------------------------
obj1 = BasicMathOperation()
#obj1.greet_user()
obj1.add_num()