from datetime import datetime
from numpy import array

try:
    fname = "../basics/data/backsorted.txt"

    with open(fname) as f:
        # converting array datatype string to int using numpy
        numbers = array(f.readlines()).astype(int)

    starttime = datetime.now()
    print("Quicksort backsorted. Elements: ", len(numbers))
    print("Start time: ", starttime)

    def partition(T, p, r):

        x = T[r]
        i = p-1

        for j in range(p, r):
            if T[j] <= x:
                i = i+1
                T[j], T[i] = T[i], T[j]

        T[i+1], T[r] = T[r], T[i+1]

        return i + 1

    def quickSort(T, p, r):

        if p < r:
            q = partition(T, p, r)
            quickSort(T, p, q - 1)
            quickSort(T, q + 1, r)

    quickSort(numbers, 0, len(numbers) - 1)
    # print(numbers)

    endtime = datetime.now()

    print("End time: ", endtime)
    timeTaken = endtime - starttime
    print("Time taken: ", timeTaken)

except FileNotFoundError as error:
    print("File is not available:", type(error))
except Exception as error:
    print("Something went wrong:", type(error))
