import os

dir_path: str = "sutFolder/"

# TODO get the return values of the exec functions.
expectedOutput = os.system("python sut.py")

for filename in os.listdir("sutFolder"):
    if filename.endswith(".py"):
        print(filename)
        # execute
        a = os.system("python " + dir_path + filename)

        # doesnt enter here for now.
        if (expectedOutput == a):
            print("not killed")
            # TODO something here about the vector
        else:
            print("mutant is killed")
    else:
        print("no file found")
