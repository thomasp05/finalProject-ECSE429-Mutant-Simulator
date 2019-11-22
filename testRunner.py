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
    testVectors = [["1","2"], ["2","3"], ["a","3"], ["-1", "33"]]
    expectedValues = [12.5, 11, None, 45.5]

    for i in range(len(testVectors)):
        testVector = testVectors[i]
        expectedValue = expectedValues[i]
        try:
            #os.system(filePath + " " +  testVector[0] + " " + testVector[1])
            cmd = filePath + " " +  testVector[0] + " " + testVector[1]
            returnValue = subprocess.Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
            out, err = returnValue.communicate()
            if(expectedValue is None):
                try:
                    val = int(out)
                    return testNumber, True, testVector
                except:
                    # This is expected behavior
                    pass
            elif(not (float(out) == expectedValue)):
                return testNumber, True, testVector
        except Exception as e:
            return testNumber, True, testVector 
    
    # If no mutants are detected, return false
    return testNumber, False, None 