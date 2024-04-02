import sys

i = 1
for arg in sys.argv[1:]:
    i *= int(arg)
print(i)
