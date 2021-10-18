
def loadProblem():

    with open("problem.txt") as problemFile:
        rawData = problemFile.read().strip();

    loc = {};
    exec("problem = " + rawData, globals(), loc);
    problem = loc["problem"];

    return problem;

def partOne(problem):

    def expandDict(D, collection):
        for key in D:
            value = D[key];
            expand(value, collection);

    def expandList(L, collection):
        for value in L:
            expand(value, collection);

    def expand(value, collection):
        if isinstance(value, int):
            collection.append(value);
        elif isinstance(value, str):
            collection.append(value);
        elif isinstance(value, dict):
            expandDict(value, collection);
        elif isinstance(value, list):
            expandList(value, collection);
        else:
            raise ValueError;

    expandedData = [];
    expand(problem, expandedData);

    result = sum(filter(lambda x: isinstance(x, int), expandedData));

    print("Part 1: {:d}".format(result));

def partTwo(problem):

    def expandDict(D, collection):
        skip = False;
        for key in D:
            value = D[key];
            if (value == "red"):
                skip = True;
                break;

        if (not skip):
            for key in D:
                value = D[key];
                expand(value, collection);

    def expandList(L, collection):
        for value in L:
            expand(value, collection);

    def expand(value, collection):
        if isinstance(value, int):
            collection.append(value);
        elif isinstance(value, str):
            collection.append(value);
        elif isinstance(value, dict):
            expandDict(value, collection);
        elif isinstance(value, list):
            expandList(value, collection);
        else:
            raise ValueError;

    expandedData = [];
    expand(problem, expandedData);

    result = sum(filter(lambda x: isinstance(x, int), expandedData));

    print("Part 2: {:d}".format(result));

if __name__ == "__main__":

    print("Solving Day 12, AoC 2015");

    problem = loadProblem();

    partOne(problem);
    partTwo(problem);