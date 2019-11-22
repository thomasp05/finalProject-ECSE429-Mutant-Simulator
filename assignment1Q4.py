__author__ = "Thomas Philippon"
__ID__ = "260747645"
__email__ = "thomas.philippon@mail.mcgill.ca"


mutantList = ["+", "-", "*", "/"] #list of possible mutants
nbMutant = [0,0,0,0]  #list containing the total number of mutants for each type
output = open("mutantLibrary.txt", "w") #Output file containing the information about the mutants
sut = open("sut.txt") #Software Under Test.
lineCounter = 0 #line number

for line in sut:
    lineCounter = lineCounter + 1
    lineHistory = "" #string used to keep an history of what is on the line so we can avoid comments
    for char in line:
        if (not "#" in lineHistory) and(char =='+' or char =='-' or char =='*' or char =='/'):
            lineNumber = str(lineCounter)
            output.write( lineNumber + ": " + str(char) +  ", ")
            for i in mutantList:
                if i != char:
                    output.write(str(i)+ ", ")
                    j = mutantList.index(i) 
                    nbMutant[j] = nbMutant[j] +1 
            output.write("\n")
            
        else: 
            lineHistory = lineHistory+ char

#Print the information about the total number of mutants of each type
output.write("Number of mutants of type + : " + str(nbMutant[0]) + "\n")
output.write("Number of mutants of type - : " + str(nbMutant[1]) + "\n")
output.write("Number of mutants of type * : " + str(nbMutant[2]) + "\n")
output.write("Number of mutants of type / : " + str(nbMutant[3]) + "\n")
output.close()


