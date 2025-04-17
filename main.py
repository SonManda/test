import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from fib import fibonacci

def main():
    n = 10
    print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
    print("Goodbye!")
    print("Thank you for using the Fibonacci calculator!")

if __name__ == "__main__":
    main()