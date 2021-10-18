import re;

def loadProblem():

    with open("problem.txt") as problemFile:
        pattern = re.compile(r"^(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\.$");
        problem = dict();
        for line in problemFile.readlines():
            m = re.match(pattern, line.strip());
            name = m.group(1);
            speed = int(m.group(2));
            duration = int(m.group(3));
            rest = int(m.group(4));
            problem[name] = (speed, duration, rest);

    return problem;

def calcDistance(speed, duration, rest, time):

    interval = duration + rest;

    numIntervals = time // interval;
    remainder = time % interval;

    distance = speed * duration * numIntervals;
    if (remainder < duration):
        distance += speed * remainder;
    else:
        distance += speed * duration;

    return distance;

def partOne(problem):

    time = 2503;
    best = max(calcDistance(*problem[k], time) for k in problem.keys())

    print("Part 1: {:d}".format(best));

def partTwo(problem):

    leaderboard = dict((k, 0) for k in problem.keys());
    distances = dict((k, 0) for k in problem.keys());

    for t in range(1, 2504):
        for k in problem.keys():
            distances[k] = calcDistance(*problem[k], t);
        best = max(distances.values());
        for k in problem.keys():
            if (distances[k] == best):
                leaderboard[k] += 1;

    best = max(leaderboard.values());

    print("Part 2: {:d}".format(best));

if __name__ == "__main__":

    print("Solving Day 14, AoC 2015");

    problem = loadProblem();

    partOne(problem);
    partTwo(problem);