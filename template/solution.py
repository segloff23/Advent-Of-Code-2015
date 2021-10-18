
def loadProblem():

    with open("problem.txt") as problemFile:
        problem = problemFile.read().strip();

    return problem;

def partOne(problem):

    print("Part 1: {:d}".format(0));

def partTwo(problem):

    print("Part 2: {:d}".format(0));

if __name__ == "__main__":

    print("Solving Day XX, AoC 2015");

    problem = loadProblem();

    partOne(problem);
    partTwo(problem);