from datetime import datetime
from numpy import array

try:
    fname = "../basics/data/random.txt"

    with open(fname) as f:

        numbers = []
        for line in f:
            num = int(line)
            numbers.append(num)

        # print(numbers)

    # ###################
    # #    MAIN BODY    #
    # ###################

    def mergeSort(arr):
        if len(arr) > 1:

            center = len(arr)//2

            L = arr[:center]

            # print("L =", L)

            R = arr[center:]

            # print("R =", R)

            mergeSort(L)

            mergeSort(R)

            i = 0
            j = 0
            x = 0

            while i < len(L) and j < len(R):
                # print("i =", i, "; j =", j, "; k =", k, ";")
                # print("len(L) =", len(L))
                # print("len(R) =", len(R))
                # print("L[i] =", L[i], "; R[j] =", R[j])
                if L[i] < R[j]:
                    arr[x] = L[i]
                    i = i + 1
                else:
                    arr[x] = R[j]
                    j = j + 1
                x = x + 1
            #     print("arr =", arr)
            # print("End of loop")

            # Checking if any element was left
            # print("i < len(L); i =", i, "; len(L) =", len(L))
            while i < len(L):
                # print("i =", i, "; j =", j, "; k =", x, ";")
                # print("len(L) =", len(L))
                # print("len(R) =", len(R))
                # print("L[i] =", L[i])
                arr[x] = L[i]
                i = i + 1
                x = x + 1

            #     print("arr =", arr)
            #     print("j < len(R); j =", j, "; len(R) =", len(R))
            # print("End loop 2")

            while j < len(R):
                # print("i =", i, "; j =", j, "; k =", k, ";")
                # print("len(L) =", len(L))
                # print("len(R) =", len(R))
                # print("R[j] =", R[j])
                arr[x] = R[j]
                j = j + 1
                x = x + 1
            #     print("arr =", arr)
            # print("End loop 3")

    starttime = datetime.now()
    print("Merge-sort random. Elements: ", len(numbers))
    print("End time: ", starttime)
    arr = numbers
    mergeSort(arr)

    endtime = datetime.now()

    print("End time: ", endtime)
    timeTaken = endtime - starttime
    print("Time taken: ", timeTaken)


except FileNotFoundError as error:
    print("File is not available:", type(error))
except Exception as error:
    print("Something went wrong:", type(error))
