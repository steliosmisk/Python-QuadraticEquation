import os
import math

print("---- Welcome to Quadratic Equation Solver ----")
print("[1] Solve Quadratic Equation")
print("[2] Exit")

while True:
    user_choice = input("Enter your choice (1/2): ")
    if user_choice == "1":
        try:
            os.system('cls')
            a = float(input("Enter a: "))
            if a == 0:
                print("Error! 'a' can not be zero.")
                continue
            b = float(input("Enter b: "))
            c = float(input("Enter c: "))
            d = (b ** 2) - 4 * a * c
            print(f"The Quadratic Equation: {a}x**2 + {b}x + {c}")
            if d < 0:
                print("The quadratic equation has complex roots")
                real_part = -b / (2 * a)
                imaginary_part = math.sqrt(abs(d)) / (2 * a)
                print(f"Roots: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")
            elif d == 0:
                print("The quadratic equation has one real root")
                root = -b / (2 * a)
                print(f"Root: {root}")
            else:
                print("The quadratic equation has two real roots")
                root1 = (-b + math.sqrt(d)) / (2 * a)
                root2 = (-b - math.sqrt(d)) / (2 * a)
                print(f"Roots: {root1} and {root2}")
        except ValueError:
            os.system('cls')
            print("Invalid input! Please enter a valid number.")
        except ZeroDivisionError:
            os.system('cls')
            print("Error! 'a' can not be zero.")
    elif user_choice == "2":
        break
    else:
        print("Invalid choice! Please enter a valid choice (1/2).")
