from datetime import datetime

try:
    fname = "../basics/data/backsorted.txt"

    with open(fname) as f:

        numbers = []
        for line in f:
            num = int(line)
            numbers.append(num)

    def insertSort(numbers):

        for i in range(1, len(numbers)):
            key = numbers[i]
            j = 0

            while key > numbers[j] and j < i:
                j = j + 1

            numbers.insert(j, key)
            del numbers[i+1]

        # print(numbers)

    starttime = datetime.now()
    print("InsertSort backsorted. Elements: ", len(numbers))
    print("Start time: ", starttime)

    insertSort(numbers)

    endtime = datetime.now()

    print("End time: ", endtime)
    timeTaken = endtime - starttime
    print("Time taken: ", timeTaken)

except FileNotFoundError as error:
    print("File is not available:", type(error))
except Exception as error:
    print("Something went wrong:", type(error))
