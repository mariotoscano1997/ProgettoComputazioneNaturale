from pathlib import Path
import sys

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

files = Path('.').glob("*.csv")
print()

for fname in files:
    with fname.open() as file:
        lines = [line for line in file.readlines() if line.index(',')>=0]
        tuples = [line.split(',') for line in lines]
        values = [float(tuple[2]) for tuple in tuples if tuple[0]=="3000000"]
        fun = fname.stem.split('_')[-1].upper()
        print("{}: {:e}".format(fun, mean(values)))
