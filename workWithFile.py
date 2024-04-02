from functools import reduce
with open("filetest.txt", "r") as f:
    numbers = f.readlines()
    numbers = list(map(int, list(map(lambda x: x.strip(), numbers))))
    print(reduce(lambda x, y: x*y, numbers, 1))
