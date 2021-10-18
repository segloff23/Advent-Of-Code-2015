import numpy as np;

def loadProblem():

    with open("problem.txt") as problemFile:
        problem = int(problemFile.read().strip());

    return problem;

def partOne(problem):

    problem //= 10;

    presents = np.ones(problem);

    for n in range(2, problem):
        presents[n-1::n] += n;
        if (presents[n-1] > problem):
            best = n;
            break;

    print("Part 1: {:d}".format(best));

def partTwo(problem):

    problem = (problem // 11) + (1 if problem % 11 != 0 else 0);

    presents = np.ones(problem);
    for n in range(2, problem):
        presents[n-1:(50*n):n] += n;
        if (presents[n-1] > problem):
            best = n;
            break;

    print("Part 2: {:d}".format(best));

if __name__ == "__main__":

    print("Solving Day 20, AoC 2015");

    problem = loadProblem();

    partOne(problem);
    partTwo(problem);