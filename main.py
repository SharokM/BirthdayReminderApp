def main():
    print("Welcome to Python!")
    print("=" * 40)
    
    name = input("What's your name? ")
    print(f"\nHello, {name}! Nice to meet you.")
    
    print("\nHere's a simple calculator:")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        print(f"\nResults:")
        print(f"{num1} + {num2} = {num1 + num2}")
        print(f"{num1} - {num2} = {num1 - num2}")
        print(f"{num1} * {num2} = {num1 * num2}")
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print(f"{num1} / {num2} = Cannot divide by zero")
    except ValueError:
        print("Invalid input! Please enter numbers only.")

if __name__ == "__main__":
    main()
