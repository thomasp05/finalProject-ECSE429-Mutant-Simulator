import sys
import os

def main():
    answer = sutProgram()
    print(answer)

def sutProgram():
    if(len(sys.argv) != 3):
        print("\nThis program takes 2 integer arguments: \n" +
           "\tArgument 1: Value for \"a\" \n" +
           "\tArgument 2: Value for \"a\" \n" +
           "\n\tExample command: python sut.py 3 2")
        raise SystemExit("InvalidArgumentException - Must have two arguments")
    else:
        # Parse to make sure arguments are integers
        for i in [1, 2]:
            try:
                arg = int(sys.argv[i])
            except ValueError:
                print("Argument is not an integer. Please enter an integer and try again")
                raise SystemExit("InvalidArgumentException - Arguments must be integers")
        
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    c = (a * b) + 2 + 3
    d = c - b
    e = d / 2
    f = e - d + 15
    return f

if __name__ == '__main__':
    main()