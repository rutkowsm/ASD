from datetime import datetime

try:
    fname = "../basics/data/random.txt"

    with open(fname) as f:

        numbers = []
        for line in f:
            num = int(line)
            numbers.append(num)

    starttime = datetime.now()
    print("Heapsort random. Elements: ", len(numbers))
    print("Start time: ", starttime)

    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # <- SWAP NUMBERS

            heapify(arr, n, largest)

    def heapSort(arr):
        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0)

    heapSort(numbers)
    n = len(numbers)

    endtime = datetime.now()

    print("End time: ", endtime)
    timeTaken = endtime - starttime
    print("Time taken: ", timeTaken)

    # PRINT SECTION
    # for row in range(len(numbers)):
    #     print(numbers[row])
    #     i = numbers[row]

except FileNotFoundError as error:
    print("File is not available:", type(error))
except Exception as error:
    print("Something went wrong:", type(error))
