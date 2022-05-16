import random
fname = "../basics/data/random.txt"

i = 1

with open(fname, "w") as fout:

    while i <= 400000:
        fout.write(str(random.randint(1, 1000000)) + "\n")
        i = i + 1

print("Completed:")
print(i-1)
