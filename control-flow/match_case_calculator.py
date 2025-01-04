
num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ").strip()

match operation:
    case "+":
        result = num_1 + num_2
        print(f"The result is {result}")
    
    case "-":
        result = num_1 - num_2
        print(f"The result is {result}")
    
    case "*":
        result = num_1 * num_2
        print(f"The result is {result}")

    case "/":
        if num_2 != 0:
            result = num_1 / num_2
            print(f"The result is {result}")
        else:
            print(f"Division by zero (0) is not allowed")
    
    case _:
        print(f"Invalid operation. Please choose from (+, -, *, /)")