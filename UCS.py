import time
import ExcelFile

# Get the fuel level of all cars
def getFuel(pattern):
    txt = pattern.split(' ')
    fuel = {}
    for c in txt[0]:
        if c.isupper():
            fuel[c] = 100
    for i in range(1, len(txt)):
        if len(txt[i]) == 0:
            continue
        f = 0
        for j in range(1, len(txt[i])):
            f = f * 10 + ord(txt[i][j]) - ord('0')
        fuel[txt[i][0]] = f
    return fuel


# Showing the grid.
def getGrid(pattern):
    return pattern.split(' ')[0]


# Verify if the vehicule can move vertically
def canCol(pattern, v, s):
    if s == 0:
        return False
    c = 0
    rmin = -1
    rmax = -1
    for i in range(36):
        if pattern[i] == v:
            if i > 0 and pattern[i - 1] == pattern[i]:
                return False
            c = i % 6
            if rmin == -1:
                rmin = int(i / 6)
            rmax = int(i / 6)
    if rmin + s < 0:
        return False
    if rmax + s > 5:
        return False
    for i in range(36):
        if pattern[i] != v and pattern[i] != '.' and i % 6 == c and min(rmin, rmin + s) <= int(i / 6) and int(
                i / 6) <= max(rmax, rmax + s):
            return False
    return True



# move the vehicule vertically
def goCol(pattern, v, s):
    ans = pattern
    c = 0
    rmin = -1
    rmax = -1
    for i in range(36):
        if pattern[i] == v:
            if i > 0 and pattern[i - 1] == pattern[i]:
                return False
            c = i % 6
            if rmin == -1:
                rmin = int(i / 6)
            rmax = int(i / 6)
    ans = list(ans)
    for i in range(36):
        if ans[i] == v:
            ans[i] = '.'
    for i in range(36):
        if i % 6 == c and rmin + s <= int(i / 6) and int(i / 6) <= rmax + s:
            ans[i] = v
    ans = "".join(ans)
    return ans


# Verify if the vehicule can move horizontally
def canRow(pattern, v, s):
    if s == 0:
        return False
    r = 0
    cmin = -1
    cmax = -1
    for i in range(36):
        if pattern[i] == v:
            if i > 5 and pattern[i - 6] == pattern[i]:
                return False
            r = int(i / 6)
            if cmin == -1:
                cmin = i % 6
            cmax = i % 6
    if cmin + s < 0:
        return False
    if cmax + s > 5:
        return False
    for i in range(36):
        if pattern[i] != v and pattern[i] != '.':
            if int(i / 6) == r and min(cmin, cmin + s) <= i % 6 and i % 6 <= max(cmax, cmax + s):
                return False
    return True


# move the vehicule horizontaly
def goRow(pattern, v, s):
    ans = pattern
    r = 0
    cmin = -1
    cmax = -1
    for i in range(36):
        if pattern[i] == v:
            if i > 5 and pattern[i - 6] == pattern[i]:
                return False
            r = int(i / 6)
            if cmin == -1:
                cmin = i % 6
            cmax = i % 6
    ans = list(ans)
    for i in range(36):
        if ans[i] == v:
            ans[i] = "."
    for i in range(36):
        if int(i / 6) == r and cmin + s <= i % 6 and i % 6 <= cmax + s:
            ans[i] = v
    ans = "".join(ans)
    return ans


# Solving the problem using the Uniform Cost Search algorithm.
def SolveUCS(pattern, testCase):
    beg = float(time.time())
    fuel = getFuel(pattern)
    file_name = f"usc-sol-{testCase}.txt"
    file = open(file_name, "w")
    file.write("--------------------------------------------------------------------------------\n\n")
    file.write("Initial board configuration: ")
    file.write(pattern + "\n\n")
    file.write("!\n")
    for i in range(6):
        for j in range(6):
            file.write(pattern[i * 6 + j])
        file.write("\n")
    file.write("\n")
    file.write("Car fuel available: ")
    start = 0
    for i in fuel:
        if start == 1:
            file.write(", ")
        file.write(i)
        file.write(":")
        file.write(f"{fuel[i]}")
        start = 1
    file.write("\n")
    file_name = f"ucs-search-{testCase}.txt"
    # writing to an excel file
    excel_file = ExcelFile.ExcelFile()
    excel_file.set_puzzle_number(testCase)
    excel_file.set_algorithm("UCS")
    excel_file.set_heuristic('NO HEURISTIC')
    H = open(file_name, "w")
    Q = [pattern]
    st = {}
    st[getGrid(pattern)] = 0
    searchPathLength = 0
    solutionPathLength = 0
    memSol = {}
    memSol[getGrid(pattern)] = "Begin"
    finalState = ""
    while len(Q) > 0:
        searchPathLength += 1
        if searchPathLength > 7000:
            Q.pop(0)
            continue
        p = Q[0]
        dist = st[getGrid(p)]
        H.write(f"{dist} {dist} 0 {p}\n")
        if p[17] == 'A':
            finalState = p
            solutionPathLength = dist
            break;
        Q.pop(0)
        fuel = getFuel(p)
        p = getGrid(p)
        for V in fuel:
            if fuel[V] == 0:
                continue
            for i in range(-5, 6):
                if canCol(p, V, i):
                    tmp = goCol(p, V, i)
                    for k in fuel:
                        if k == V:
                            fuel[k] = fuel[k] - 1
                        if fuel[k] < 100:
                            tmp = tmp + " "
                            tmp = tmp + k
                            tmp = tmp + str(fuel[k])
                        if k == V:
                            fuel[k] = fuel[k] + 1
                    if (getGrid(tmp) in st) == False:
                        st[getGrid(tmp)] = dist + 1
                        if i < 0:
                            memSol[getGrid(tmp)] = f"{V} up {-i}"
                        else:
                            memSol[getGrid(tmp)] = f"{V} down {i}"
                        Q.append(tmp)
                if canRow(p, V, i):
                    tmp = goRow(p, V, i)
                    for k in fuel:
                        if k == V:
                            fuel[k] = fuel[k] - 1
                        if fuel[k] < 100:
                            tmp = tmp + " "
                            tmp = tmp + k
                            tmp = tmp + str(fuel[k])
                        if k == V:
                            fuel[k] = fuel[k] + 1
                    if (getGrid(tmp) in st) == False:
                        st[getGrid(tmp)] = dist + 1
                        if i < 0:
                            memSol[getGrid(tmp)] = f"{V} left {-i}"
                        else:
                            memSol[getGrid(tmp)] = f"{V} right {i}"
                        Q.append(tmp)

    if len(Q) == 0:
        file.write("Sorry, could not solve the puzzle as specified.\nError: no solution found\n")
        end = float(time.time())
        t = end - beg
        t = float(int(t * 100)) / 100
        excel_file.set_time(t)
        file.write(f"\nRuntime: {t} seconds\n")
        excel_file.set_solution_length("none")
        excel_file.set_search_path_length("none")
        excel_file.write_row()
        excel_file.clear_state()
    else:
        end = float(time.time())
        t = end - beg
        t = float(int(t * 100)) / 100
        file.write(f"\nRuntime: {t} seconds\n")
        file.write(f"Search path length: {searchPathLength} states\n")
        file.write(f"Solution path length: {solutionPathLength} moves\n")
        excel_file.set_time(t)
        excel_file.set_search_path_length(searchPathLength)
        excel_file.set_solution_length(solutionPathLength)
        excel_file.write_row()
        excel_file.clear_state()
        solutionPath = []
        impleState = []
        finalFuel = getFuel(finalState)
        finalGrid = getGrid(finalState)
        while memSol[getGrid(finalState)] != "Begin":
            ope = memSol[getGrid(finalState)]
            move = ope.split(' ')
            solutionPath.append(ope)
            car_fuel = getFuel(finalState)
            impleState.append(ope + "    " + str(car_fuel[move[0]]) + finalState)
            car_fuel[move[0]] += 1

            if car_fuel[move[0]] == 100:
                car_fuel.pop(move[0])
            if (move[1][0] == 'u'):
                finalState = goCol(getGrid(finalState), move[0], int(move[2]))
            if (move[1][0] == 'd'):
                finalState = goCol(getGrid(finalState), move[0], -int(move[2]))
            if (move[1][0] == 'l'):
                finalState = goRow(getGrid(finalState), move[0], int(move[2]))
            if (move[1][0] == 'r'):
                finalState = goRow(getGrid(finalState), move[0], -int(move[2]))
            for i in car_fuel:
                if car_fuel[i] == 100:
                    continue
                finalState = finalState + " " + i + str(car_fuel[i])

        file.write("Solution path:")
        SJ = 0
        for i in range(len(solutionPath) - 1, -1, -1):
            if SJ == 1:
                file.write(";")
            file.write(" " + solutionPath[i])
            SJ = 1
        file.write("\n\n")
        for i in range(len(impleState) - 1, -1, -1):
            file.write(impleState[i])
            file.write("\n")
        file.write("\n")

        file.write("!")
        for i in finalFuel:
            if finalFuel[i] == 100:
                continue
            file.write(" " + i + str(finalFuel[i]))
        file.write("\n")
        for i in range(6):
            for j in range(6):
                file.write(finalGrid[i * 6 + j])
            file.write("\n")
        file.write("\n")

    file.write("--------------------------------------------------------------------------------\n\n")




