# This is a sample Python script.
from A import SolveA
from GBFS import SolveGBFS
from UCS import SolveUCS

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    F = open("sample-input.txt", "r")

    Data = F.read()

    Data = Data.split("\n")

    count = 1
    #  UCS
    for S in Data:
        if len(S) == 0:
            continue
        if S[0] == '#':
            continue
        SolveUCS(S, count)
        count += 1
    #  GBFS
    count = 1
    for S in Data:
        if len(S) == 0:
            continue
        if S[0] == '#':
            continue
        for method in range(1, 5):
            SolveGBFS(S, count, method)
        count += 1
    # A
    count = 1
    for S in Data:
        if len(S) == 0:
            continue
        if S[0] == '#':
            continue
        for method in range(1, 5):
            SolveA(S, count, method)
        count += 1
