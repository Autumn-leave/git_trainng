from calculator import add, subtract
from utils import greet_user

def main():
    greet_user("Meenachi")

    a = 10
    b = 5

    print("Add:", add(a, b))
    print("Subtract:", subtract(a, b))

if __name__ == "__main__":
    main()