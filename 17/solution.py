
def loadProblem():

    with open("problem.txt") as problemFile:
        problem = [int(line.strip()) for line in problemFile.readlines()];

    return sorted(problem);

def partOne(problem):

    def getNumWays(i, space):

        if (i >= len(problem)):
            return (1 if space == 0 else 0);
        else:
            dont = getNumWays(i+1, space);
            if (space < problem[i]):
                return dont;
            else:
                use = getNumWays(i+1, space-problem[i]);
                return use + dont;

    ways = getNumWays(0, 150);

    print("Part 1: {:d}".format(ways));

def partTwo(problem):

    cache = {};
    def getNumWays(previous, i, space):

        if (i >= len(problem)):
            if (space == 0):
                if (previous in cache):
                    cache[previous] += 1;
                else:
                    cache[previous] = 1;
                return 1;
            else:
                return 0;
        else:
            dont = getNumWays(previous, i+1, space);
            if (space < problem[i]):
                return dont;
            else:
                use = getNumWays(previous + (i,), i+1, space-problem[i]);
                return use + dont;

    getNumWays((), 0, 150);

    minContainers = len(min(cache, key=lambda X: len(X)));
    ways = 0;
    for way in cache:
        if (len(way) == minContainers):
            ways += cache[way];

    print("Part 2: {:d}".format(ways));

if __name__ == "__main__":

    print("Solving Day 17, AoC 2015");

    problem = loadProblem();

    partOne(problem);
    partTwo(problem);