from itertools import groupby, chain;
import numpy as np;

def loadProblem():

    with open("problem.txt") as problemFile:
        problem = problemFile.read().strip();

    return problem;

def loadElements():

    with open("elements.txt") as elementsFile:
        elements = dict();
        elementsByName = dict();
        for line in elementsFile.readlines():
            parts = line.strip().replace("\t", " ").split(" ");
            index = int(parts[0])-1;
            elements[index] = [parts[1], parts[-2], parts[2:-2]];
            elementsByName[parts[1]] = index;

    M = [[0]*92 for i in range(92)];
    for j in range(92):
        value = elements[j];
        for name in value[2]:
            i = elementsByName[name];
            M[i][j] += 1;

    return np.array(M), elements;

def partOne(problem, M, elements, N=40, suppress=False):

    vector = [0]*92;
    valid = False;
    for e in elements:
        string = elements[e][1];
        if (problem == string):
            vector[e] += 1;
            valid = True;
            break;
    v = np.array(vector).reshape(92, 1);

    if (valid):
        M_P = np.linalg.matrix_power(M, N);
        product = np.matmul(M_P, v);
        result = 0;
        for i in range(92):
            result += product[i, 0] * len(elements[i][1]);
    else:
        current = tuple(int(x) for x in problem);
        for i in range(N):
            current = tuple(chain.from_iterable(
                        (len(tuple(v)), k) for k, v in groupby(current)));
        result = len(current);

    if (not suppress):
        print("Part 1: {:d}".format(result));

    return result;

def partTwo(problem, M, elements):

    result = partOne(problem, M, elements, N=50, suppress=True);

    print("Part 2: {:d}".format(result));

if __name__ == "__main__":

    print("Solving Day 10, AoC 2015");

    problem = loadProblem();
    M, elements = loadElements();

    partOne(problem, M, elements);
    partTwo(problem, M, elements);