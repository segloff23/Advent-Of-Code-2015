import re;
from itertools import permutations;

def loadProblem():

    with open("problem.txt") as problemFile:
        pattern = re.compile(r"^(\w+) would (lose|gain) (\d+) happiness units by sitting next to (\w+)\.$");
        problem = dict();
        for line in problemFile.readlines():
            m = re.match(pattern, line.strip());
            name = m.group(1);
            happiness = int(m.group(3)) * (1 if m.group(2) == "gain" else -1);
            target = m.group(4);
            problem[(name, target)] = happiness;

    return problem;

def partOne(problem, suppress=False):

    def calcHappiness(seating):

        total = 0;
        for i in range(0, len(seating)):
            total += problem[(seating[i], seating[i-1])]
            total += problem[(seating[i], seating[(i+1) % len(seating)])];

        return total;

    people = set(x[0] for x in problem.keys());
    happiness = [calcHappiness(seating) for seating in permutations(people)];
    best = max(happiness);

    if (not suppress):
        print("Part 1: {:d}".format(best));

    return best;

def partTwo(problem):

    people = set(x[0] for x in problem.keys());
    for p in people:
        problem[("Myself", p)] = 0;
        problem[(p, "Myself")] = 0;

    best = partOne(problem, suppress=True);

    print("Part 2: {:d}".format(best));

if __name__ == "__main__":

    print("Solving Day 13, AoC 2015");

    problem = loadProblem();

    partOne(problem);
    partTwo(problem);