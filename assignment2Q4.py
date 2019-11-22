__author__ = "Thomas Philippon"
__ID__ = "260747645"
__email__ = "thomas.philippon@mail.mcgill.ca"

import os
from shutil import copyfile

#Operator List
opList = [] 
mutants = "+-*/"

#Provide the path of the SUT and mutant library
sutPath = 'sut_merge-sort.py'
mutantLibraryPath = 'mutantLibrary.txt'

#create a folder in the directory of this python script where the SUT with injected mutants will be saved 
if not os.path.exists('sutFolder'):
    os.mkdir('sutFolder')

#open the mutant library file
mutantLibrary = open(mutantLibraryPath)

#variables used to keep track of the mutant and its line number on the previous line of the mutant library  
prevLineNumber = 0
prevOperator = ""
opratorLineCount = 0

#iterate through each line of the mutant library 
libraryLineNumber = 0 #line number
for line in mutantLibrary:
    libraryLineNumber = libraryLineNumber + 1

    #Get the line number of the mutant in the SUT 
    sutLineNumber =  line.split(":")[0]

    #Get the original operator
    mutantList = []
    for char in line: 
        if char in mutants:
            mutantList.append(char)
    originalOperator = mutantList[0]

    #Discard mutantList for the last three lines of the mutant library (where the stats are displayed)
    if len(mutantList) == 1:
        mutantList = []
    
    #List of possible mutants from the mutant library generated in assignment 1
    mutantList = mutantList[1:]

    #Check if the previous operator was the same operator and on the same line of the SUT
    #If it is the case, increment operatorLineCount 
    if originalOperator == prevOperator and sutLineNumber == prevLineNumber:
        operatorLineCount = operatorLineCount + 1
    else:
        operatorLineCount = 0

    #Loop through the list of possible mutants, make a copy of the SUT and inject the mutants
    mutantCounter = 0
    for operator in mutantList:
        #make a copy of the SUT 
        newProgramPath ='sutFolder/'+ str(libraryLineNumber)+ "_" +str(mutantCounter)+'test.py'
        newProgram = open(newProgramPath, "w")

        #open the orriginal SUT
        sut = open(sutPath)

        #copy each line of code from the original SUT into the copy and inject the mutant in the right line of code
        lineCounterMutant = 0
        for mutantLine in sut: 
            lineCounterMutant = lineCounterMutant + 1
            if str(lineCounterMutant) == sutLineNumber:
                mutantIndex =  [i for i, ltr in enumerate(mutantLine) if ltr == str(originalOperator)]
                mutantIndex = mutantIndex[operatorLineCount]
                mutantLine = list(mutantLine)
                mutantLine[mutantIndex] = mutantList[mutantCounter]
                mutantLine =  ''.join([str(string) for string in mutantLine])
                newProgram.write(mutantLine)
            else: 
                newProgram.write(mutantLine)
        newProgram.close
        mutantCounter = mutantCounter +1

    #Update the previous line number and operator
    prevLineNumber = sutLineNumber
    prevOperator = originalOperator





