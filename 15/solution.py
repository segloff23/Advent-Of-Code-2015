import re;

def loadProblem():

    with open("problem.txt") as problemFile:
        pattern = re.compile(r"^(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)$");
        problem = dict();
        for line in problemFile.readlines():
            m = re.match(pattern, line.strip());
            problem[m.group(1)] = tuple(int(m.group(i)) for i in range(2, 7));

    return problem;

def partOne(problem):

    t = [problem[k] for k in problem];

    score = 0
    best = 0
    for i in range(0,100):
        for j in range(0,100-i):
            for k in range(0,100-i-j):
                h = 100-i-j-k
                a = t[0][0]*i+t[1][0]*j+t[2][0]*k+t[3][0]*h
                b = t[0][1]*i+t[1][1]*j+t[2][1]*k+t[3][1]*h
                c = t[0][2]*i+t[1][2]*j+t[2][2]*k+t[3][2]*h
                d = t[0][3]*i+t[1][3]*j+t[2][3]*k+t[3][3]*h

                if (a > 0 and b > 0 and c > 0 and d > 0):
                    score = a*b*c*d;
                    if (score > best):
                        best = score;

    print("Part 1: {:d}".format(best));

def partTwo(problem):

    t = [problem[k] for k in problem];

    score = 0
    best = 0
    for i in range(0,100):
        for j in range(0,100-i):
            for k in range(0,100-i-j):
                h = 100-i-j-k
                a = t[0][0]*i+t[1][0]*j+t[2][0]*k+t[3][0]*h
                b = t[0][1]*i+t[1][1]*j+t[2][1]*k+t[3][1]*h
                c = t[0][2]*i+t[1][2]*j+t[2][2]*k+t[3][2]*h
                d = t[0][3]*i+t[1][3]*j+t[2][3]*k+t[3][3]*h
                e = t[0][4]*i+t[1][4]*j+t[2][4]*k+t[3][4]*h

                if (e == 500 and (a > 0 and b > 0 and c > 0 and d > 0)):
                    score = a*b*c*d;
                    if (score > best):
                        best = score;

    print("Part 2: {:d}".format(best));

if __name__ == "__main__":

    print("Solving Day 15, AoC 2015");

    problem = loadProblem();

    partOne(problem);
    partTwo(problem);
