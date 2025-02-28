def Sum_of_Two_Numbers():
    num1 = float(input("Enter Fisrt Number: "))
    num2 = float(input("Enter Second Number: "))
    print(f"\n::The Sum of {num1} and {num2} is {num1 + num2}::")

def Difference_of_Two_Numbers():
    num1 = float(input("Enter Fisrt Number: "))
    num2 = float(input("Enter Second Number: "))
    print(f"\n::The Difference of {num1} and {num2} is {num1 - num2}::\n")

def Product_of_Two_Numbers():
    num1 = float(input("Enter Fisrt Number: "))
    num2 = float(input("Enter Second Number: "))
    print(f"\n::The Product of {num1} and {num2} is {num1 * num2}::\n")

def quotient_of_two_numbers():
    num1 = float(input("Enter Fisrt Number: "))
    num2 = float(input("Enter Second Number: "))
    if num2 != 0:
        print(f"\n::The quotient of {num1} and {num2} is {num1 / num2}::\n")
    else:
        print("\n::Error: Cannot divide by zero!::\n")

def display_method_menu():
    print("*******************************")
    print("1 - Sum of Two Numbers")
    print("2 - Difference of Two Numbers")
    print("3 - Product of Two Numbers")
    print("4 - Quotient of Two Numbers")
    print("5 - Exit Program")
    print("*******************************")

def main():
    while True:
        display_method_menu()
        choice = int(input("Choose Menu: "))
        if choice == 1:
            print("\nYOU CHOOSE MENU 1 - SUM OF TWO NUMBERS")
            print("*************************************")
            Sum_of_Two_Numbers()
        elif choice == 2:
            print("\nYOU CHOOSE MENU 2 - DIFFERENCE OF TWO NUMBERS")
            print("*************************************")
            Difference_of_Two_Numbers()
        elif choice == 3:
            print("\nYOU CHOOSE MENU 3 - PRODUCT OF TWO NUMBERS")
            print("*************************************")
            Product_of_Two_Numbers()
        elif choice == 4:
            print("\nYOU CHOOSE MENU 4 - QUOTIENT OF TWO NUMBERS")
            print("*************************************")
            quotient_of_two_numbers()
        elif choice == 5:
            print("\nExit the program")
            break
        else:
            print("\nInvalid choice, Please enter a number between 1 and 5.\n")

if __name__ == "__main__":
    main()

    