
def loadProblem():

    with open("problem.txt") as problemFile:
        problem = [[line[:3], line[3:].split(", ")]
                   for line in problemFile.readlines()];

    for row in problem:
        row[1] = [x.strip() for x in row[1]];

    return problem;

def hlf(registers, ip, args):
    registers[args[0]] //= 2;
    return ip + 1;

def tpl(registers, ip, args):
    registers[args[0]] *= 3;
    return ip + 1;

def inc(registers, ip, args):
    registers[args[0]] += 1;
    return ip + 1;

def jmp(registers, ip, args):
    return ip + int(args[0]);

def jie(registers, ip, args):
    if (registers[args[0]] % 2 == 0):
        return ip + int(args[1]);
    else:
        return ip + 1;

def jio(registers, ip, args):
    if (registers[args[0]] == 1):
        return ip + int(args[1]);
    else:
        return ip + 1;

def runComputer(registers):

    ip = 0;
    while (ip < len(problem)):
        comm, args = problem[ip]
        ip = COMMANDS[comm](registers, ip, args);

    return ip;

COMMANDS = {"hlf": hlf, "tpl": tpl, "inc": inc,
            "jmp": jmp, "jie": jie, "jio": jio}

def partOne(problem):

    registers = {"a": 0, "b": 0}
    runComputer(registers);

    bVal = registers["b"];

    print("Part 1: {:d}".format(bVal));

def partTwo(problem):

    registers = {"a": 1, "b": 0}
    runComputer(registers);

    bVal = registers["b"];

    print("Part 2: {:d}".format(bVal));

if __name__ == "__main__":

    print("Solving Day 23, AoC 2015");

    problem = loadProblem();

    partOne(problem);
    partTwo(problem);