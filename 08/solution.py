
def loadProblem():

    with open("problem.txt") as problemFile:
        problem = [line.strip() for line in problemFile.readlines()];

    return problem;

def partOne(problem):

    codeLength = 0;
    memLength = 0;
    for string in problem:

        codeLength += len(string);
        string = string[1:-1].replace('\\"', " ").replace("\\\\", " ");

        i = 0;
        while (i < len(string)):
            memLength += 1;
            if (string[i] == "\\"):
                i += 4;
            else:
                i += 1;

    diff = codeLength - memLength;

    print("Part 1: {:d}".format(diff));

def partTwo(problem):

    codeLength = 0;
    newLength = 0;

    for string in problem:

        codeLength += len(string);

        newLength += 2;
        for char in string:
            if (char == '"'):
                newLength += 2;
            elif (char == "\\"):
                newLength += 2;
            else:
                newLength += 1;

    diff = newLength - codeLength;

    print("Part 2: {:d}".format(diff));

if __name__ == "__main__":

    print("Solving Day  8, AoC 2015");

    problem = loadProblem();

    partOne(problem);
    partTwo(problem);