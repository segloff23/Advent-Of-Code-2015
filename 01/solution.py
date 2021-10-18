
def loadProblem():

    with open("problem.txt") as problemFile:
        problem = problemFile.read().strip();

    return problem;

def partOne(problem):

    up = problem.count("(");
    down = len(problem) - up;
    finalFloor = up - down;

    print("Part 1: {:d}".format(finalFloor));

def partTwo(problem):

    floor = 0;
    for position, char in enumerate(problem):
        floor = floor + (1 if char ==  "(" else -1);
        if (floor == -1):
            finalPosition = position + 1;
            print("Part 2: {:d}".format(finalPosition));
            return;

    raise Exception("Problem has no solution");


if __name__ == "__main__":
    
    print("Solving Day  1, AoC 2015");

    problem = loadProblem();

    partOne(problem);
    partTwo(problem);