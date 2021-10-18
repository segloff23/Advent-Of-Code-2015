
def loadProblem():

    with open("problem.txt") as problemFile:
        problem = problemFile.read().strip();

    return problem;

def partOne(problem):

    directions = {">": 1, "<": -1, "^": 1j, "v": -1j};

    visited = set();
    start = 0+0j;
    visited.add(start);

    current = start;
    for move in problem:
        current += directions[move];
        visited.add(current);

    numVisited = len(visited);

    print("Part 1: {:d}".format(numVisited));

def partTwo(problem):

    directions = {">": 1, "<": -1, "^": 1j, "v": -1j};

    visited = set();
    start = 0+0j;
    visited.add(start);

    current = start;
    for move in problem[::2]:
        current += directions[move];
        visited.add(current);

    current = start;
    for move in problem[1::2]:
        current += directions[move];
        visited.add(current);

    numVisited = len(visited);

    print("Part 2: {:d}".format(numVisited));


if __name__ == "__main__":

    print("Solving Day  3, AoC 2015");

    problem = loadProblem();

    partOne(problem);
    partTwo(problem);