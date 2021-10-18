import re;

def loadProblem():

    with open("problem.txt") as problemFile:

        pattern = re.compile(r"(\w+): (\d+)");
        problem = []
        for line in problemFile.readlines():
            m = re.findall(pattern, line);
            problem.append(dict((k, int(v)) for k,v in m));

    return problem;

def partOne(problem, target):

    auntSue = None;

    for sue, types in enumerate(problem):
        valid = True;
        for t, v in types.items():
            if (t not in target or target[t] != v):
                valid = False;
                break;
        if (valid):
            auntSue = sue + 1;
            break;

    print("Part 1: {:d}".format(auntSue));

def partTwo(problem, target):

    auntSue = 1;

    for sue, types in enumerate(problem):
        valid = True;
        for t, v in types.items():
            if (t not in target):
                pass;
            elif (t == "cats" or t == "trees"):
                if (v <= target[t]):
                    valid = False;
                    break;
            elif (t == "pomeranians" or t == "goldfish"):
                if (v >= target[t]):
                    valid = False;
                    break;
            elif (target[t] != v):
                valid = False;
                break;
        if (valid):
            auntSue = sue + 1;
            break;

    print("Part 2: {:d}".format(auntSue));

if __name__ == "__main__":

    print("Solving Day 16, AoC 2015");

    target = {"children": 3,
              "cats": 7,
              "samoyeds": 2,
              "pomeranians": 3,
              "akitas": 0,
              "vizslas": 0,
              "goldfish": 5,
              "trees": 3,
              "cars": 2,
              "perfumes": 1}

    problem = loadProblem();

    partOne(problem, target);
    partTwo(problem, target);