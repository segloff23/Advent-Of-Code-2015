import hashlib;

def loadProblem():

    with open("problem.txt") as problemFile:
        problem = problemFile.read().strip();

    return problem;

def partOne(problem):

    number = 0;
    key = problem + str(number);
    md5 = hashlib.md5(key.encode()).hexdigest();

    while (not md5.startswith("0"*5)):
        number += 1;
        key = problem + str(number);
        md5 = hashlib.md5(key.encode()).hexdigest();

    print("Part 1: {:d}".format(number));

def partTwo(problem):

    number = 0;
    key = problem + str(number);
    md5 = hashlib.md5(key.encode()).hexdigest();

    while (not md5.startswith("0"*6)):
        number += 1;
        key = problem + str(number);
        md5 = hashlib.md5(key.encode()).hexdigest();

    print("Part 2: {:d}".format(number));


if __name__ == "__main__":

    print("Solving Day  4, AoC 2015");

    problem = loadProblem();

    partOne(problem);
    partTwo(problem);