
def loadProblem():

    with open("problem.txt") as problemFile:
        problem = {};
        for line in problemFile.readlines():
            parts = line.strip().split(" ");
            start = parts[0];
            stop = parts[2];
            dist = int(parts[4]);
            problem[(start, stop)] = dist;
            problem[(stop, start)] = dist;

    return problem;

def partOne(problem, maximize=False, suppress=False):

    cache = {};
    def DP(subproblem):

        if (subproblem not in cache):
            cameFrom, left = subproblem;
            if (len(left) == 0):
                cache[subproblem] = 0;
            else:
                dists = [];
                for upNext in left:
                    newLeft = tuple(filter(lambda loc: loc != upNext, left));
                    newSubproblem = (upNext, newLeft);
                    d = DP(newSubproblem);
                    if (cameFrom == None):
                        dists.append(d);
                    else:
                        dists.append(problem[(cameFrom, upNext)] + d);
                if (maximize):
                    cache[subproblem] = max(dists);
                else:
                    cache[subproblem] = min(dists);

        return cache[subproblem];

    locations = tuple(set(entry[0] for entry in problem.keys()));
    dist = DP((None, locations));

    if (not suppress):
        print("Part 1: {:d}".format(dist));

    return dist;

def partTwo(problem):

    dist = partOne(problem, maximize=True, suppress=True);

    print("Part 2: {:d}".format(dist));

if __name__ == "__main__":

    print("Solving Day  9, AoC 2015");

    problem = loadProblem();

    partOne(problem);
    partTwo(problem);