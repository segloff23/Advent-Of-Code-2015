import random;

def loadProblem():

    with open("problem.txt") as problemFile:
        formulas, start = problemFile.read().strip().split("\n\n");
        problem = [list(tuple(line.split(" => "))
                        for line in formulas.split("\n")), start];

    return problem;

def partOne(problem):

    formulas, start = problem;

    options = set();

    for f, g in formulas:
        i = 0;
        while (i < len(start)):
            j = start.find(f, i);
            if (j != -1):
                i = j;
                compound = start[:i] + start[i:].replace(f, g, 1);
                options.add(compound);
                i += 1;
            else:
                break;

    total = len(options);

    print("Part 1: {:d}".format(total));

def partTwo(problem):

    formulas, goal = problem;

    costs = [];
    for k in range(100):
        current = goal;
        steps = 0;
        while (current != "e"):
            found = False;
            random.shuffle(formulas);
            for sm, bg in formulas:
                if (current.find(bg) != -1):
                    current = current.replace(bg, sm, 1);
                    found = True;
                    steps += 1;
                    break;
            if (not found):
                break;
        if (current == "e"):
            costs.append(steps);

    best = min(costs);

    print("Part 2: {:d}".format(best));

if __name__ == "__main__":

    print("Solving Day 19, AoC 2015");

    problem = loadProblem();

    partOne(problem);
    partTwo(problem);