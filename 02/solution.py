
def loadProblem():

    with open("problem.txt") as problemFile:
        problem = [tuple(int(x) for x in line.strip().split("x"))
                       for line in problemFile.readlines()];

    return problem;

def partOne(problem):

    areas = [2*(l*w + w*h + h*l) for l,w,h in problem];
    slacks = [min(l*w, w*h, h*l) for l,w,h in problem];
    totalArea = sum(areas) + sum(slacks);

    print("Part 1: {:d}".format(totalArea));

def partTwo(problem):

    ribbons = [2*sum(sorted(dimensions)[0:2]) for dimensions in problem];
    bows = [l*w*h for l,w,h in problem];
    totalLength= sum(ribbons) + sum(bows);

    print("Part 2: {:d}".format(totalLength));


if __name__ == "__main__":
    
    print("Solving Day  2, AoC 2015");

    problem = loadProblem();

    partOne(problem);
    partTwo(problem);