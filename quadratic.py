import math
import os

print("--Welcome to Quadratic Equation Solver--")
print("[1] Start")
print("[2] Stop")

user_choice = int(input("Enter your choice: "))
while user_choice == 1 and user_choice != 2:
    try:
        os.system('cls')
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        c = int(input("Enter c: "))
        d = (b ** 2) - 4 * a * c
        print(f"The Formula: {a}x**2 + {b}x + {c}")
        form = (-b + math.sqrt(abs(d))) / (2 * a)
        form2 = (-b - math.sqrt(abs(d))) / (2 * a)
        if d < 0:
            print("Complex Roots")
            print(-b / (2 * a), "+", f"{math.sqrt(abs(d))}i")
            print(-b / (2 * a), "-", f"{math.sqrt(abs(d))}i")
        elif d == 0:
            print("One real root")
            print('X:', form)
        else:
            print("Two real roots")
            print('X1:', form)
            print('X2:', form2)
        break
    except ZeroDivisionError:
        os.system('cls')
        print("Enter a valid A! ")
        
