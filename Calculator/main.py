def calculator():
    print("Welcome to the Calculator!")
    print("Options:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    
    while True:
        choice = input("\nChoose an operation (1/2/3/4/5): ")
        
        if choice == '5':
            print("Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                
                if choice == '1':
                    result = num1 + num2
                    print(f"The result is: {result}")
                elif choice == '2':
                    result = num1 - num2
                    print(f"The result is: {result}")
                elif choice == '3':
                    result = num1 * num2
                    print(f"The result is: {result}")
                elif choice == '4':
                    if num2 != 0:
                        result = num1 / num2
                        print(f"The result is: {result}")
                    else:
                        print("Error: Division by zero is not allowed.")
            except ValueError:
                print("Error: Please enter valid numbers.")
        else:
            print("Invalid choice. Please select from the options.")
calculator()
