# pylint: disable=missing-module-docstring,missing-function-docstring,eval-used
import sys


def main():

    if sys.argv[2] == "+":
        return int(sys.argv[1]) + int(sys.argv[3])
    elif sys.argv[2] == "-":
        return int(sys.argv[1]) - int(sys.argv[3])
    elif sys.argv[2] == "*":
        return int(sys.argv[1]) * int(sys.argv[3])
    elif sys.argv[2] == "/":
        return int(sys.argv[1]) / int(sys.argv[3])


    """Implement the calculator"""



if __name__ == "__main__":
    print(main())
