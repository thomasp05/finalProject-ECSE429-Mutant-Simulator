import sys
import os

def main():
    answer = sutProgram()
    print(answer)


# This code was taken from the website Geeks for Geeks 
# https://www.geeksforgeeks.org/python-program-for-binary-search/
# Returns index of x in arr if present, else -1 
def binarySearch (arr, l, r, x): 
  
    # Check base case 
    if r >= l: 
  
        mid = int(l + (r - l)/2)

        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        # Else the element can only be present in right subarray 
        else: 
            return binarySearch(arr, mid+1, r, x) 
  
    else: 
        # Element is not present in the array 
        return -1


def sutProgram():
    if(len(sys.argv) != 12 ):
        #print("\nThis program takes a list of integer arguments seperated by white spaces: \n" +
        #   "\n\tExample command: python sut.py 2 2 3 5 6 7 10 12 18 88 9")
        print("-1")
        exit()
    else:
        # Parse to make sure arguments are integers
        for i in range(1, len(sys.argv)):
            try:
                arg = int(sys.argv[i])
            except ValueError:
                #print("Argument is not an integer. Please enter an integer and try again")
                print("-1")
        
    # a = int(sys.argv[1])
    # b = int(sys.argv[2])

    myList = []
    for item in sys.argv[1:]: 
        myList.append(int(item))

    arr = myList[:-1]
    r = len(myList[:-1])
    x = myList[-1]

    #check if array is sorted and call binary search if it is. Return -1 if it is not 
    flag = 0
    i = 1
    while i < len(arr): 
        if(arr[i] < arr[i - 1]): 
            flag = 1
        i += 1  
    if flag == 1: 
        return -1
    else:
        f = binarySearch( arr, 0, r, x)
        return f

if __name__ == '__main__':
    main()


