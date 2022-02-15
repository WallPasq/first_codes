# My first calculator in Python
# Developed by Wallacy Pasqualini
# Contact me: wallacypasqualini@gmail.com
# LinkedIn: https://www.linkedin.com/in/wallacypasqualini
# See other projects in my GitHub: https://github.com/WallPasq


import os


def calculator(op, num):
    # Creates a calculator that performs calculations with as many numbers as the user wants
    result = 0
    counter = 0
    if op == 1:
        for i in num:
            result += i
    elif op == 2:
        result = num[0]
        for i in num:
            if counter > 0:
                result -= i
                counter += 1
            counter += 1
    elif op == 3:
        result = num[0]
        for i in num:
            if counter > 0:
                result *= i
                counter += 1
            counter += 1
    elif op == 4:
        result = num[0]
        for i in num:
            if counter > 0:
                result /= i
                counter += 1
            counter += 1
    elif op == 5:
        result = num[0]
        for i in num:
            if counter > 0:
                result **= i
                counter += 1
            counter += 1
    elif op == 6:
        result = num[0]
        for i in num:
            if counter > 0:
                result **= (1 / i)
                counter += 1
            counter += 1
    return result


# Main program
os.system('cls')
math_operation = 1
while math_operation != 0:
    math_operation = int(input(
        "CALCULATOR - Developed by Wallacy Pasqualini\n\n"
        "*****************************************************************\n"
        "Enter the number corresponding to the desired math operation:\n"
        "1 - Sum\n"
        "2 - Subtraction\n"
        "3 - Multiplication\n"
        "4 - Division\n"
        "5 - Exponentiation\n"
        "6 - Root\n"
        "*****************************************************************\n"))
    while (math_operation < 1) or (math_operation > 6):
        os.system('cls')
        print(
            "CALCULATOR - Developed by Wallacy Pasqualini\n\n"
            "!!! Please enter a valid number !!!\n")
        math_operation = int(input(
            "*****************************************************************\n"
            "Enter the number corresponding to the desired math operation:\n"
            "1 - Sum\n"
            "2 - Subtraction\n"
            "3 - Multiplication\n"
            "4 - Division\n"
            "5 - Exponentiation\n"
            "6 - Root\n"
            "*****************************************************************\n"))
    amount = int(input("\nHow many numbers will your math operation have? "))
    while amount < 2:
        print("\n!!! The program needs two or more numbers to work !!!\n")
        amount = int(input("\nHow many numbers will your math operation have? "))
    print("\n")
    x = 0
    numbers = []
    while x < amount:
        if x == 0:
            numbers.append(int(input("Enter the 1st number: ")))
        elif x == 1:
            numbers.append(int(input("Enter the 2nd number: ")))
        elif x == 2:
            numbers.append(int(input("Enter the 3rd number: ")))
        else:
            numbers.append(int(input("Enter the %dth number: " % (x + 1))))
        x += 1
    print("\nThe result is", calculator(math_operation, numbers), "\n")
    math_operation = int(input(
        "*****************************************************************\n"
        "Want to perform one more math operation?\n"
        "0 - No\n"
        "1 - Yes\n"
        "*****************************************************************\n"))
    while (math_operation != 0) and (math_operation != 1):
        print("\n!!! Please enter a valid number !!!\n")
        math_operation = int(input(
            "*****************************************************************\n"
            "Want to perform one more math operation?\n"
            "1 - Yes\n"
            "0 - No\n"
            "*****************************************************************\n"))
    os.system('cls')
