
def loadProblem():

    with open("problem.txt") as problemFile:
        problem = [];
        for line in problemFile.readlines():
            parts = line.strip().split(" ");
            if (len(parts) == 3):
                problem.append(("SET", parts[2], (parts[0],)));
            elif (len(parts) == 4):
                problem.append(("NOT", parts[3], (parts[1],)));
            elif (len(parts) == 5):
                problem.append((parts[1], parts[4], (parts[0], parts[2])));
            else:
                raise ValueError;

    return problem;

def partOne(problem, suppress=False):

    evaluated = dict();
    def SET(src, args):
        evaluated[src] = args[0];

    def NOT(src, args):
        evaluated[src] = 65535-args[0];

    def RSHIFT(src, args):
        evaluated[src] = args[0] >> args[1];

    def LSHIFT(src, args):
        evaluated[src] = args[0] << args[1];

    def AND(src, args):
        evaluated[src] = args[0] & args[1];

    def OR(src, args):
        evaluated[src] = args[0] ^ args[1];

    operations = {"SET": SET, "NOT": NOT,
                  "RSHIFT": RSHIFT, "LSHIFT": LSHIFT,
                  "AND": AND, "OR": OR}

    pending = set(problem);

    while (len(pending) > 0):

        solved = set();
        for command, src, rargs in pending:
            args = [];
            valid = True;
            for arg in rargs:
                if arg.isnumeric():
                    args.append(int(arg));
                elif arg in evaluated:
                    args.append(evaluated[arg]);
                else:
                    valid = False;
                    break;
            if (valid):
                operations[command](src, args);
                solved.add((command, src, rargs));

        if (len(solved) == 0):
            raise Exception;
        else:
            pending = pending.difference(solved);

    if (not suppress):
        print("Part 1: {:d}".format(evaluated["a"]));

    return evaluated["a"];

def partTwo(problem, partOneSolution):

    newProblem = [*problem];
    for i in range(len(problem)):
        entry = problem[i];
        if (entry[1] == "b"):
            newProblem[i] = ("SET", "b", (str(partOneSolution),));
            break;

    solution = partOne(newProblem, suppress=True);
    print("Part 2: {:d}".format(solution));

if __name__ == "__main__":

    print("Solving Day  7, AoC 2015");

    problem = loadProblem();

    partOneSolution = partOne(problem);
    partTwo(problem, partOneSolution);