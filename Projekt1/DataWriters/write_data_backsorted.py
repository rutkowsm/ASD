import random
fname = "basics/data/backsorted.txt"

i = 1
n = 1000000

with open(fname, "w") as fout:

  while i <= 400000:
    fout.write(str(n) + "\n")
    # print(i)
    n = n - random.randint(0,4)
    i = i + 1

print("Elements:")
print(i-1)