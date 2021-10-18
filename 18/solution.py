
def loadProblem():

    with open("problem.txt") as problemFile:
        problem = problemFile.read().strip().split("\n");

    problem = [[1 if c == "#" else 0 for c in row] for row in problem];

    return problem;

def partOne(problem):

    def isValid(r, c):

        if (r < rows and r >= 0):
            if (c < cols and c >= 0):
                return True;

        return False;

    def progress(grid, neighbors):

        newNeighbors = [[*row] for row in neighbors];
        newGrid = [[*row] for row in grid];

        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == 1):
                    if (neighbors[r][c] != 2 and neighbors[r][c] != 3):
                        newGrid[r][c] = 0;
                        for dr, dc in dSet:
                            if isValid(r+dr, c+dc):
                                newNeighbors[r+dr][c+dc] -= 1;
                else:
                    if (neighbors[r][c] == 3):
                        newGrid[r][c] = 1;
                        for dr, dc in dSet:
                            if (isValid(r+dr, c+dc)):
                                newNeighbors[r+dr][c+dc] += 1;

        return newGrid, newNeighbors;

    rows, cols = len(problem), len(problem[0]);
    grid = [[*row] for row in problem];

    neighbors = [[0]*cols for _ in range(rows)];

    dSet = [(0, 1), (1, 0), (0, -1), (-1, 0),
            (1, -1), (-1, 1), (1, 1), (-1, -1)];
    for r in range(rows):
        for c in range(cols):
            for dr, dc in dSet:
                if (isValid(r+dr, c+dc) and grid[r+dr][c+dc] == 1):
                    neighbors[r][c] += 1;

    for step in range(100):
        grid, neighbors = progress(grid, neighbors);

    lights = sum(sum(row) for row in grid);

    print("Part 1: {:d}".format(lights));

def partTwo(problem):

    def isValid(r, c):

        if (r < rows and r >= 0):
            if (c < cols and c >= 0):
                return True;

        return False;

    def isCorner(r, c):

        if (r == 0):
            if (c == 0 or c == cols-1):
                return True;
        elif (r == rows-1):
            if (c == 0 or c == cols-1):
                return True;

        return False;

    def progress(grid, neighbors):

        newNeighbors = [[*row] for row in neighbors];
        newGrid = [[*row] for row in grid];

        for r in range(rows):
            for c in range(cols):
                if (not isCorner(r, c)):
                    if (grid[r][c] == 1):
                        if (neighbors[r][c] != 2 and neighbors[r][c] != 3):
                            newGrid[r][c] = 0;
                            for dr, dc in dSet:
                                if isValid(r+dr, c+dc):
                                    newNeighbors[r+dr][c+dc] -= 1;
                    else:
                        if (neighbors[r][c] == 3):
                            newGrid[r][c] = 1;
                            for dr, dc in dSet:
                                if (isValid(r+dr, c+dc)):
                                    newNeighbors[r+dr][c+dc] += 1;

        return newGrid, newNeighbors;

    rows, cols = len(problem), len(problem[0]);
    grid = [[*row] for row in problem];

    grid[0][0] = 1;
    grid[0][cols-1] = 1;
    grid[rows-1][0] = 1;
    grid[rows-1][cols-1] = 1;

    neighbors = [[0]*cols for _ in range(rows)];

    dSet = [(0, 1), (1, 0), (0, -1), (-1, 0),
            (1, -1), (-1, 1), (1, 1), (-1, -1)];
    for r in range(rows):
        for c in range(cols):
            for dr, dc in dSet:
                if (isValid(r+dr, c+dc) and grid[r+dr][c+dc] == 1):
                    neighbors[r][c] += 1;

    for step in range(100):
        grid, neighbors = progress(grid, neighbors);

    lights = sum(sum(row) for row in grid);

    print("Part 1: {:d}".format(lights));

if __name__ == "__main__":

    print("Solving Day 18, AoC 2015");

    problem = loadProblem();

    partOne(problem);
    partTwo(problem);