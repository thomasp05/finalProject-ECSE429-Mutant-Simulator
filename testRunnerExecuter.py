import sys
import os
from os import listdir
from os.path import isfile, join
from testRunner import testRunnnerMethod
import multiprocessing as mp
import time 

results = []
# Step 2: Define callback function to collect the output in `results`
def collect_result(result):
    global results
    results.append(result)



def main():
    currLocation = os.path.dirname(os.path.realpath(__file__))
    path = ("/sutFolder/")
    fileNameList = [f for f in listdir(currLocation + path) if isfile(join(currLocation + path, f))]
   
    pool = mp.Pool(mp.cpu_count()) #gunna assign the number of processes depennding on the number available on the computer
    start_time = time.time() #start the timer for computing the elapsed time

    success = testRunnnerMethod("/sut_merge-sort.py", 0)
    print(str(success[0]) + ", " + str(success[1]) + ", " + success[2]+" in " + str(success[3]))

    for i in range(len(fileNameList)):
        try:

            #thats the function call to execute the loop in parallel
            pool.apply_async(testRunnnerMethod, args=(path + fileNameList[i], i+1),callback=collect_result )

            #uncomment the following code if you dont want to execute the loop in parallel
            # success = testRunnnerMethod(path + fileNameList[i], i+1)
            # if(success[1]):
            #     # Handle success
            #     print(str(success[0]) + ", " + str(success[1]) + ", " + success[2]+" in " + str(success[3]))
            # else:
            #     # Handle failure
            #     print(str(success[0]) + ", " + str(success[1]) + ", " + success[2]+" in " + str(success[3]))
        except Exception as e:
            print(str(e))
    
    pool.close() #close the pool
    pool.join()  #wait until all processes are done
    elapsed_time = time.time() - start_time #stop the timer and compute the elapsed time 

    #print the results
    for item in results:
        print(item)

    #print elapsed time 
    print(elapsed_time)

    print("done")

if __name__ == '__main__':
    
    main()
