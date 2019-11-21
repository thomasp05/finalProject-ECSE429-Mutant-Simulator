def main():
    answer = sutProgram()
    print(answer)

def sutProgram():
    a = 1
    b = 1

    c = (a * b) + 2 + 3
    d = c - b
    e = d / 2
    f = e - d + 15
    return f

if __name__ == '__main__':
    main()