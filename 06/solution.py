import numpy as np;

def loadProblem():

    with open("problem.txt") as problemFile:
        problem = [];
        for line in problemFile.readlines():
            parts = line.strip().split(" ");
            command = parts[-4];
            start = tuple(int(x) for x in parts[-3].split(","));
            stop = tuple(int(x) for x in parts[-1].split(","));
            problem.append((command, start, stop));

    return problem;

def partOne(problem):

    grid = np.zeros((1000, 1000), dtype="uint16");

    for command, start, stop in problem:
        r0, c0 = start;
        r1, c1 = stop[0]+1, stop[1]+1;
        if command == "on":
            grid[r0:r1, c0:c1] = 1;
        elif command == "off":
            grid[r0:r1, c0:c1] = 0;
        else:
            grid[r0:r1, c0:c1] = 1 - grid[r0:r1, c0:c1];

    lightsOn = sum(sum(row) for row in grid);

    print("Part 1: {:d}".format(lightsOn));

def partTwo(problem):

    grid = np.zeros((1000, 1000), dtype="uint16");

    for command, start, stop in problem:
        r0, c0 = start;
        r1, c1 = stop[0]+1, stop[1]+1;
        if command == "on":
            grid[r0:r1, c0:c1] += 1;
        elif command == "off":
            grid[r0:r1, c0:c1] -= (grid[r0:r1, c0:c1] > 0);
        else:
            grid[r0:r1, c0:c1] += 2;

    brightness = sum(sum(row) for row in grid);

    print("Part 2: {:d}".format(brightness));

if __name__ == "__main__":

    print("Solving Day  6, AoC 2015");

    problem = loadProblem();

    partOne(problem);
    partTwo(problem);