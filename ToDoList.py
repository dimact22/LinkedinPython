import sys
import os


def readToDo():
    print("===============================\n")
    with open("ToDo.txt", "r") as f:
        lines = f.readlines()
        for i, i2 in enumerate(lines):
            print(f"{i+1}: {i2}")
    print("===============================")
    print("You can add, remove and just see all your tasks")


def addToDo():
    with open("ToDo.txt", "a") as f:
        f.write(sys.argv[2] + "\n")
    readToDo()


def removeToDo():
    lines = list()
    with open("ToDo.txt", "r") as f:
        lines = f.readlines()
    lines.pop(int(sys.argv[2])-1)
    with open("ToDo.txt", "w") as f:
        f.writelines(lines)


if not os.path.exists("ToDo.txt"):
    f = open("ToDo.txt", "w")
    f.close()
else:
    if len(sys.argv) == 1:
        readToDo()
    elif sys.argv[1] == "add":
        addToDo()
    elif sys.argv[1] == "remove":
        removeToDo()
    else:
        print("We don't have this command:(")
        exit(1)
