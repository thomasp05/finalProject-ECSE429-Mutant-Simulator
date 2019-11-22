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
   
    pool = mp.Pool(mp.cpu_count())
    start_time = time.time()

    for i in range(len(fileNameList)):
        try:
            pool.apply_async(testRunnnerMethod, args=(path + fileNameList[i], i+1),callback=collect_result )
            # success = testRunnnerMethod(path + fileNameList[i], i+1)
            # if(success[1]):
            #     # Handle success
            #     print(str(success[0]) + ", " + str(success[1]) + ", " + success[2]+" in " + success[3])
            # else:
            #     # Handle failure
            #     print(str(success[0]) + ", " + str(success[1]) + ", " + success[2]+" in " + success[3])
        except Exception as e:
            print(str(e))
    
    
    elapsed_time = time.time() - start_time
    print(elapsed_time)

    print("done")

if __name__ == '__main__':
    # start_time = time.time()
    # pool = mp.Pool(12)
    # pool.apply_async(main())
    main()
    time.sleep(2)
    print(results)
    # elapsed_time = time.time() - start_time
   
    # print(elapsed_time)
    #main()