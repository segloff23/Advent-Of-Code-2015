import re;

def loadProblem():

    with open("problem.txt") as problemFile:
        pattern = re.compile(r"(row (\d+), column (\d+))");
        text = problemFile.read().strip();
        m = re.search(pattern, text);
        problem = (int(m.group(2)), int(m.group(3)));

    return problem;

def partOne(problem):

    def sumToN(n):
        return (n * (n+1)) // 2;

    def sumFromDtoN(d, n):
        return sumToN(n) - sumToN(d-1);

    def getNext(x):
        return (x * 252533) % 33554393;

    row, col = problem;
    num = 1 + sumToN(row-1) + sumFromDtoN(row+1, col+row-1);

    code = 20151125;
    for k in range(num-1):
        code = getNext(code);

    print("Part 1: {:d}".format(code));

def partTwo(problem):

    print("Part 2: {:s}".format("All 50 stars completed!"));

if __name__ == "__main__":

    print("Solving Day 25, AoC 2015");

    problem = loadProblem();

    partOne(problem);
    partTwo(problem);