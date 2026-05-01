import math as m
import numpy as np


class Program:
    def menu_program(self):
        print("\nWelcome to ( CTS ) Calculator")
        print("1. Calculator")
        print("2. Trigonometric Calculator")
        print("3. Statistics Calculator")
        print("4. Exit")

        try:
            return int(input("Enter your choice:- "))
        except ValueError:
            return -1

    def run(self):
        while True:
            choice = self.menu_program()

            if choice == 1:
                Calculator()
            elif choice == 2:
                TrigonometricCalculator()
            elif choice == 3:
                StatisticsCalculator()
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please enter 1-4.")


# ---------------- CALCULATOR ----------------

class Calculator:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.run()

    def menu(self):
        print("\nCalculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        try:                                          # FIX #1: added try/except (was crashing on non-int input)
            return int(input("Enter your choice:- "))
        except ValueError:
            return -1

    def get_value(self):
        try:
            self.x = float(input("Enter first value:- "))
            self.y = float(input("Enter second value:- "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            return False
        return True

    def addition(self):
        return self.x + self.y

    def subtraction(self):
        return self.x - self.y

    def multiplication(self):
        return self.x * self.y

    def division(self):
        if self.y == 0:
            return "You can't divide by zero!"
        return self.x / self.y

    def run(self):
        while True:
            choice = self.menu()

            if choice == 5:
                print("Returning to main menu...")
                break
            elif choice == -1:
                print("Invalid choice! Please enter 1-5.")
                continue
            elif choice not in [1, 2, 3, 4]:
                print("Invalid choice! Please enter 1-5.")
                continue

            if not self.get_value():              # FIX #2: was ignoring False return (would crash on bad input)
                continue

            if choice == 1:
                print("Addition:", self.addition())
            elif choice == 2:
                print("Subtraction:", self.subtraction())
            elif choice == 3:
                print("Multiplication:", self.multiplication())
            elif choice == 4:
                print("Division:", self.division())


# ---------------- TRIGONOMETRIC ----------------

class TrigonometricCalculator:
    def __init__(self):
        self.run()

    def menu(self):
        print("\nTrigonometric Calculator")
        print("Format : sin 30 | cos 60 | tan 45")
        print("Available: sin, cos, tan, cot, sec, cosec")
        print("Type 0 to go back")

    def run(self):
        while True:
            self.menu()
            user = input("Enter function:- ").strip().lower()

            if user == "0":
                print("Returning to main menu...")
                break

            try:
                parts = user.split()
                if len(parts) != 2:
                    raise ValueError
                y, x = parts
                value = int(x)
            except ValueError:
                print("Format should be like: sin 30")
                continue

            if value not in [0, 30, 45, 60, 90, 120, 180, 270, 360]:
                print("Invalid angle! Valid angles: 0, 30, 45, 60, 90, 120, 180, 270, 360")
                continue

            rad = m.radians(value)

            try:
                if y == "sin":
                    print(f"{y} {value}:- {round(m.sin(rad), 4)}")

                elif y == "cos":
                    print(f"{y} {value}:- {round(m.cos(rad), 4)}")

                elif y == "tan":
                    if value in [90, 270]:
                        print(f"{y} {value}:- undefined")
                    else:
                        print(f"{y} {value}:- {round(m.tan(rad), 4)}")

                elif y == "cot":
                    if value in [0, 180, 360]:
                        print(f"{y} {value}:- undefined")
                    else:
                        print(f"{y} {value}:- {round(1 / m.tan(rad), 4)}")

                elif y == "sec":
                    if value in [90, 270]:
                        print(f"{y} {value}:- undefined")
                    else:
                        print(f"{y} {value}:- {round(1 / m.cos(rad), 4)}")

                elif y == "cosec":
                    if value in [0, 180, 360]:
                        print(f"{y} {value}:- undefined")
                    else:
                        print(f"{y} {value}:- {round(1 / m.sin(rad), 4)}")

                else:
                    # FIX #3: was showing "invalid angle" message for an invalid *function* name
                    print("Unknown function! Use: sin, cos, tan, cot, sec, cosec")

            except Exception:
                print("Unexpected error! Try again.")


# ---------------- STATISTICS ----------------

class StatisticsCalculator:
    def __init__(self):
        self.run()

    def menu(self):
        print("\nStatistics Calculator")
        print("1. Mean")
        print("2. Variance")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Max")
        print("6. Min")
        print("7. Sum")
        print("8. Exit")

    def run(self):
        # FIX #4: added try/except around n input (was crashing on non-int)
        try:
            n = int(input("Enter how many data values you want to input:- "))
        except ValueError:
            print("Invalid input! Please enter a whole number.")
            return

        if n <= 0:
            print("Dataset cannot be empty! Enter a positive number.")
            return

        dataset = []                               # FIX #5: removed duplicate dataset = [] that was above this

        for i in range(n):
            while True:
                try:
                    dataset.append(float(input(f"Enter value {i + 1}:- ")))
                    break
                except ValueError:
                    print("Invalid input! Please enter a number.")

        print("Dataset:", dataset)

        arr = np.array(dataset)

        while True:
            self.menu()
            choice = input("Enter your choice:- ").strip().lower()

            if choice in ["1", "mean"]:
                print("Mean:", np.mean(arr))

            elif choice in ["2", "variance"]:
                print("Variance:", np.var(arr))

            elif choice in ["3", "median"]:
                print("Median:", np.median(arr))

            elif choice in ["4", "std", "standard deviation"]:   # FIX #6: added "standard deviation" alias
                print("Standard Deviation:", np.std(arr))

            elif choice in ["5", "max"]:
                print("Max:", np.max(arr))

            elif choice in ["6", "min"]:
                print("Min:", np.min(arr))

            elif choice in ["7", "sum"]:
                print("Sum:", np.sum(arr))

            elif choice in ["8", "exit"]:
                print("Returning to main menu...")
                break

            else:
                print("Invalid choice! Please enter 1-8.")


# ---------------- RUN PROGRAM ----------------

Program().run()