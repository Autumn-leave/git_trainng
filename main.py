from calculator import add, subtract,multiply
from utils import greet_user

def main():
    greet_user("Meenachi")

    a = 10
    b = 5

    print("Add:", add(a, b))
    print("Subtract:", subtract(a, b))
    print("multiple: ", multiply(a, b))

if __name__ == "__main__":
    main()