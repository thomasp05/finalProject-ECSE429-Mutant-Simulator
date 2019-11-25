import os
import sys
import subprocess
from subprocess import check_output
from subprocess import PIPE
from threading import Timer

# Method used to run the SUT based on an inputs specified in the input
# Returns:
#   testNumber ----- for easy retrieval from the threadPool,
#   mutantDetected - boolean value determining if mutant was detected
#   testVector ----- Test vector which detected the mutant. Will be None if no mutant is detected
#
def testRunnnerMethod(filePath, testNumber):

    # This code will run the specified SUT
    testVectors = ["0 1 2 3 4 5 6 7 8 0", "0 1 2 3 4 5 6 7 8 9 10 2", "10 9 8 7 6 5 4 3 2 1 1", "1 2 3 4 5 6 7 8 9 10 1","1 2 3 4 5 6 7 8 9 10 5", "1 2 3 4 5 6 7 8 9 10 6","1 2 3 4 5 6 7 8 9 10 7", "1 2 3 4 5 6 7 8 9 10 10", "1 2 3 5", "a b c 5", "5 6 2 4 3 3"]
    expectedValues = [-1, -1, -1, 0, 3, 5, 6, 9, -1, -1, -1]

    for i in range(len(testVectors)):
        testVector = testVectors[i]
        expectedValue = expectedValues[i]
        try:
            #os.system(filePath + " " +  testVector[0] + " " + testVector[1])
            cmd = "python ." + filePath + " " +  testVector
            try:
                returnValue = subprocess.run(cmd, stdout=PIPE, stderr=PIPE, timeout=2)
            except subprocess.TimeoutExpired:
                 return testNumber, True, testVector, filePath[11:]
                
            if(not (float(returnValue.stdout) == expectedValue)):
                return testNumber, True, testVector, filePath[11:]
                
        except Exception as e:
            return testNumber, True, testVector, filePath[11:]
    
    # If no mutants are detected, return false
    return testNumber, False, " ", filePath[11:]
