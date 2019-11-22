import sys
import os
from os import listdir
from os.path import isfile, join
from testRunner import testRunnnerMethod


def main():
    currLocation = os.path.dirname(os.path.realpath(__file__))
    path = ("/sutFolder/")
    fileNameList = [f for f in listdir(currLocation + path) if isfile(join(currLocation + path, f))]

    for i in range(len(fileNameList)):
        try:
            success = testRunnnerMethod(path + fileNameList[i], i+1)
            if(success[1]):
                # Handle success
                print(str(success[0]) + ", " + str(success[1]) + ", " + success[2]+" in " + fileNameList[i])
            else:
                # Handle failure
                print(str(success[0]) + ", " + str(success[1]) + ", " + success[2]+" in " + fileNameList[i])
        except Exception as e:
            print(str(e))

    print("done")

if __name__ == '__main__':
    main()