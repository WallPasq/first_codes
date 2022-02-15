# My first calculator in Python
# Developed by Wallacy Pasqualini
# Contact me: wallacypasqualini@gmail.com
# LinkedIn: https://www.linkedin.com/in/wallacypasqualini
# See other projects in my GitHub: https://github.com/WallPasq


import os


def calculator(op, num):
    # Creates a calculator that performs calculations with as many numbers as the user wants
    result = num[0]
    validator = 0
    print("\n")
    if op == 1:
        for i in num:
            if validator != 0:
                print("%d + %d = %d" % (result, i, result + i))
                result += i
            validator = 1
    elif op == 2:
        for i in num:
            if validator != 0:
                print("%d - %d = %d" % (result, i, result - i))
                result -= i
            validator = 1
    elif op == 3:
        for i in num:
            if validator != 0:
                print("%d * %d = %d" % (result, i, result * i))
                result *= i
            validator = 1
    elif op == 4:
        for i in num:
            if validator != 0:
                if i == 0:
                    print("%.2f / %d = Cannot divide by 0" % (result, i))
                    break
                print("%.2f / %d = %.2f" % (result, i, result / i))
                result /= i
            validator = 1
    elif op == 5:
        for i in num:
            if validator != 0:
                if result == 0 and i <= 0:
                    print("%.2f ** %d = 0 cannot be raised to 0 or a negative power" % (result, i))
                    break
                else:
                    print("%.2f ** %d = %.2f" % (result, i, result ** i))
                    result **= i
            validator = 1
    elif op == 6:
        for i in num:
            if validator != 0:
                if i == 0:
                    print("%.2f ** (1/%d) = Cannot find 0th root" % (result, i))
                    break
                if result == 0 and i < 0:
                    print("%.2f ** (1/%d) = 0 cannot be raised to negative power" % (result, i))
                    break
                print("%.2f ** (1/%d) = %.2f" % (result, i, result ** (1 / i)))
                result **= (1 / i)
            validator = 1
    print("\n")
    return result


def correctingNumber(n):
    # Function that does not allow entries other than integers
    while True:
        try:
            n = int(n)
            break
        except ValueError:
            n = input("\n!!! Please enter an integer !!!\n")
    return n


# Main program
os.system('cls')
math_operation = 1
while math_operation != 0:
    math_operation = correctingNumber(input(
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
        math_operation = correctingNumber(input(
            "*****************************************************************\n"
            "Enter the number corresponding to the desired math operation:\n"
            "1 - Sum\n"
            "2 - Subtraction\n"
            "3 - Multiplication\n"
            "4 - Division\n"
            "5 - Exponentiation\n"
            "6 - Root\n"
            "*****************************************************************\n"))
    amount = correctingNumber(input("\nHow many numbers will your math operation have? "))
    while amount < 2:
        print("\n!!! The program needs two or more numbers to work !!!\n")
        amount = correctingNumber(input("\nHow many numbers will your math operation have? "))
    print("\n")
    x = 0
    numbers = []
    while x < amount:
        if x == 0:
            numbers.append(correctingNumber(input("Enter the 1st number: ")))
        elif x == 1:
            numbers.append(correctingNumber(input("Enter the 2nd number: ")))
        elif x == 2:
            numbers.append(correctingNumber(input("Enter the 3rd number: ")))
        else:
            numbers.append(correctingNumber(input("Enter the %dth number: " % (x + 1))))
        x += 1
    calculator(math_operation, numbers)
    math_operation = correctingNumber(input(
        "*****************************************************************\n"
        "Want to perform one more math operation?\n"
        "0 - No\n"
        "1 - Yes\n"
        "*****************************************************************\n"))
    while (math_operation != 0) and (math_operation != 1):
        print("\n!!! Please enter a valid number !!!\n")
        math_operation = correctingNumber(input(
            "*****************************************************************\n"
            "Want to perform one more math operation?\n"
            "0 - No\n"
            "1 - Yes\n"
            "*****************************************************************\n"))
    os.system('cls')
