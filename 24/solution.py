import itertools;

def loadProblem():

    with open("problem.txt") as problemFile:
        problem = [int(x.strip()) for x in problemFile.readlines()];

    return problem;

def partOne(problem):

    def doesSubsetExist(array, target):

        def DP(subprob):

            if (subprob not in cache):
                S, i = subprob;

                if (S == 0):
                    cache[subprob] = True;
                elif (S < 0):
                    cache[subprob] = False;
                elif (i >= lengthA):
                    cache[subprob] = False;
                elif (S > partials[i]):
                    cache[subprob] = False;
                else:
                    e = A[i];
                    if (DP((S-e, i+1))):
                        cache[subprob] = True;
                    elif (DP((S, i+1))):
                        cache[subprob] = True;
                    else:
                        cache[subprob] = False;

            return cache[subprob];

        A = tuple(sorted(array, reverse=True));
        partials = [sum(A[i:]) for i in range(len(A))];
        lengthA = len(A);

        start = (target, 0);
        cache = {}

        return DP(start);

    def product(L):

        p = 1;
        for e in L:
            p *= e;

        return p;

    def findBestSubset(n):

        options = [];

        while (len(options) == 0):
            for subset in itertools.combinations(problem, n):
                if (sum(subset) == target):
                    options.append(subset);
            n += 1;

        options.sort(key=product);

        i = 0;
        best = options[0];
        remaining = list(set(problem).difference(set(best)));
        valid = doesSubsetExist(remaining, target)
        while (not valid and i < len(options)-1):
            i += 1;
            best = options[i];
            remaining = list(set(problem).difference(set(best)));
            valid = doesSubsetExist(remaining, target)

        if (not valid):
            return None, len(best);
        else:
            return best, len(best);

    target = sum(problem) // 3;

    best, bestL = findBestSubset(1);
    while (best == None):
        best, bestL = findBestSubset(bestL+1);

    print("Part 1: {:d}".format(product(best)));

def partTwo(problem):

    def doesDoubleSubsetExist(array, target):

        def DP(subprob):

            if (subprob not in cache):
                SA, SB, i = subprob;

                if (SA == 0 and SB == 0):
                    cache[subprob] = True;
                elif (SA < 0 or SB < 0):
                    cache[subprob] = False;
                elif (i >= lengthA):
                    cache[subprob] = False;
                elif (SA + SB > partials[i]):
                    cache[subprob] = False;
                else:
                    e = A[i];
                    if (DP((SA, SB, i+1))):
                        cache[subprob] = True;
                    elif (DP((SA-e, SB, i+1))):
                        cache[subprob] = True;
                    elif (DP((SA, SB-e, i+1))):
                        cache[subprob] = True;
                    else:
                        cache[subprob] = False;

            return cache[subprob];

        A = tuple(sorted(array, reverse=True));
        partials = [sum(A[i:]) for i in range(len(A))];
        lengthA = len(A);

        start = (target, target, 0);
        cache = {}

        return DP(start);

    def product(L):

        p = 1;
        for e in L:
            p *= e;

        return p;

    def findBestSubset(n):

        options = [];

        while (len(options) == 0):
            for subset in itertools.combinations(problem, n):
                if (sum(subset) == target):
                    options.append(subset);
            n += 1;

        options.sort(key=product);

        i = 0;
        best = options[0];
        remaining = list(set(problem).difference(set(best)));
        valid = doesDoubleSubsetExist(remaining, target)
        while (not valid and i < len(options)-1):
            i += 1;
            best = options[i];
            remaining = list(set(problem).difference(set(best)));
            valid = doesDoubleSubsetExist(remaining, target)

        if (not valid):
            return None, len(best);
        else:
            return best, len(best);

    target = sum(problem) // 4;

    best, bestL = findBestSubset(1);
    while (best == None):
        best, bestL = findBestSubset(bestL+1);
        print("here", bestL);

    print("Part 2: {:d}".format(product(best)));

if __name__ == "__main__":

    print("Solving Day 24, AoC 2015");

    problem = loadProblem();

    partOne(problem);
    partTwo(problem);