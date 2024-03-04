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
def main():
    while True:
        # Create an instance of BasicMathOperation
        math_ops = BasicMathOperation()

        # Display list of questions/tasks to the user
        print("\nPlease choose an operation to perform:")
        print("0. End Program")
        print("1. Greet User")
        print("2. Add Numbers")
        print("3. Perform Operation")
        print("4. Square Number")
        print("5. Factorial")
        print("6. Count")
        print("7. Calculate Hypotenuse")
        print("8. Area of Rectangle")
        print("9. Power of Number")
        print("10. Type of Argument")

        # Prompt the user to pick a number corresponding to the task they want to execute
        choice = input("Enter the number corresponding to the operation you want to perform: \n")

        # Handle invalid selections
        if not choice.isdigit() or int(choice) < 0 or int(choice) > 10:
            print("Invalid selection. Please choose a number between 1 and 10.")
            continue

        # Convert choice to integer
        choice = int(choice)

        # Call the respective method based on the user's choice
        if choice == 1:
            math_ops.greet_user()
        elif choice == 2:
            result = math_ops.add_num()
            print("Result:", result)
        elif choice == 3:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            operator = input("Enter the operator (+, -, *, /): ")
            result = math_ops.perf_op(num1, num2, operator)
            print("Result:", result)
        elif choice == 4:
            num = int(input("Enter a number: "))
            result = math_ops.calculateSquare(num)
            print("Result:", result)
        elif choice == 5:
            num = int(input("Enter a number: "))
            result = math_ops.factorial(num)
            print("Result:", result)
        elif choice == 6:
            num1 = int(input("Enter the starting number: "))
            num2 = int(input("Enter the ending number: "))
            result = math_ops.count(num1, num2)
            print("Result:", result)
        elif choice == 7:
            num = int(input("Enter a number: "))
            result = math_ops.calculateHypotenuse(num)
            print("Result:", result)
        elif choice == 8:
            length = int(input("Enter the length of the rectangle: "))
            width = int(input("Enter the width of the rectangle: "))
            result = math_ops.a_rec(length, width)
            print("Result:", result)
        elif choice == 9:
            num = int(input("Enter a number: "))
            exp = int(input("Enter the exponent: "))
            result = math_ops.p_num(num, exp)
            print("Result:", result)
        elif choice == 10:
            argu = input("Enter an argument: ")
            result = math_ops.t_arg(argu)
            print("Result:", result)
        elif choice == 0:
            break

#-------------------------------------
main()