import os
import sys
import subprocess
from subprocess import check_output
from subprocess import PIPE

# Method used to run the SUT based on an inputs specified in the input
# Returns:
#   testNumber ----- for easy retrieval from the threadPool,
#   mutantDetected - boolean value determining if mutant was detected
#   testVector ----- Test vector which detected the mutant. Will be None if no mutant is detected
#
def testRunnnerMethod(filePath, testNumber):

    # This code will run the specified SUT
    testVectors = ["1 2 3 4 5 6 7 8 9 10 10", "1 2 3 5", "a b c 5", "5 6 2 4 3 3"]
    expectedValues = [10, -1, -1, -1]

    for i in range(len(testVectors)):
        testVector = testVectors[i]
        expectedValue = expectedValues[i]
        try:
            #os.system(filePath + " " +  testVector[0] + " " + testVector[1])
            cmd = "python ." + filePath + " " +  testVector
            returnValue = subprocess.Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE, timeout=2)
            out, err = returnValue.communicate()
            if(not (float(out) == expectedValue)):
                return testNumber, True, testVector
        except Exception as e:
            return testNumber, True, testVector 
    
    # If no mutants are detected, return false
    return testNumber, False, None 
    
