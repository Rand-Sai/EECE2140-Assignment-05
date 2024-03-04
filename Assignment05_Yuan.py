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
    
    #Perform Operation Method
    def perf_op(self, num1, num2, operator):
        if operator == "+":
            return print(num1 + num2)
        elif operator == "-":
            return print(num1 - num2)
        elif operator == "*":
            return print(num1 * num2)
        elif operator == "/":
            return print(num1 / num2)
        else:
            print("Sorry, you've enter a unknown operator, please try again. (+ - * / with quo. marks)")

    #Square Number Method
    def sq_num(self, num):
        if type(num) != int:
            print("Sorry, you've fail to enter an integer, please try again.")
        else:
            return print(num**2)

    #Factorial
    def factorial(self, num):
        result = 1
        if type(num) != int:
            print("Sorry, you've fail to enter an integer, please try again.")
        else:
            if num < 0:
                return "Factorial is not defined for negative numbers.\n"
            for i in range(1, num + 1):
                result *= i
            return print(result)
        
    #Counting
    def count(self, num1, num2):
        if type(num1) != int or type(num2) != int:
            print("Sorry, you've fail to enter integer(s), please try again.")
        else:
            return print(list(range(num1, num2 + 1)))

#-----------------------------------
obj1 = BasicMathOperation()
