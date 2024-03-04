#Assignment 05 - Basic Math Operation
import math
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
        return None

    #Add Number Method
    def add_num(self):
        num1 = int(input("Enter the 1st number:\n"))
        num2 = int(input("Enter the 2nd number:\n"))
        return num1 + num2
    
    #Perform Operation Method
    def perf_op(self, num1, num2, operator):
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            return num1 / num2
        else:
            print("Sorry, you've enter a unknown operator, please try again. (+ - * / with quo. marks)")
            return None

    #Square Number Method
    def calculateSquare(self, num):
        if type(num) != int:
            print("Sorry, you've fail to enter an integer, please try again.")
            return None
        else:
            result = num**2
            return result

    #Factorial Method
    def factorial(self, num):
        result = 1
        if type(num) != int:
            print("Sorry, you've fail to enter an integer, please try again.")
            return None
        else:
            if num < 0:
                return "Factorial is not defined for negative numbers.\n"
            for i in range(1, num + 1):
                result *= i
            return result
        
    #Counting Method
    def count(self, num1, num2):
        if type(num1) != int or type(num2) != int:
            print("Sorry, you've fail to enter integer(s), please try again.")
            return None
        else:
            return list(range(num1, num2 + 1))

    #Hypotenuse Method
    def calculateHypotenuse(self, num):
        if type(num) != int:
            print("Sorry, you've fail to enter integer(s), please try again.")
            return None
        else:
            #Pythagorean theorem
            side_sq = self.calculateSquare(num) #Implement Square Number method
            return math.sqrt(2 * side_sq)
        
    #Area of Rectangle Method
    def a_rec(self, len, wid):
        if type(len) != int or type(wid) != int:
            print("Sorry, you've fail to enter integer(s), please try again.")
            return None
        else:
            return len * wid
    
    #Power of Number Method
    def p_num(self, num, exp):
        if type(num) != int or type(exp) != int:
            print("Sorry, you've fail to enter integer(s), please try again.")
            return None
        else:
            return num ** exp
        
    #Type of Argument Method
    def t_arg(self, argu):
        return type(argu)

#-----------------------------------
obj1 = BasicMathOperation()