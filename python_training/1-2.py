import sys

buffer = sys.stdin.read().splitlines()

for i in buffer:
    print int(i) ** 3
