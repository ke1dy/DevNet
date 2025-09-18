print("Calculator")

def calcu(operation, num1, num2):
    if operation == "+":
        return print("Addition: ", num1 + num2)

    elif operation == "-":
        return print("Subtraction: ",num1 - num2)

    elif operation == "*":
        return print("Multiplication: ",num1 * num2)

    elif operation == "/":
        return print("Division: ",num1 / num2)

    elif operation == "%":
        return print("Modulo: ",num1 % num2)

while True:
    num1 = int(input("Enter your first number: "))
    operation = input("Choose operation (+, -, *, /, %): ")
    num2 = int(input("Enter your second number: "))

    calcu(operation, num1, num2)

    pick = input("Want to calculate again? (Y/N): ").upper()
    if(pick == "Y"):
        print()
        continue
    else:
        break

if __name__ == "__main__":
    print("eya lunto ini")