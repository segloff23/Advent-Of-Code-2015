
def loadProblem():

    with open("problem.txt") as problemFile:
        problem = problemFile.read().strip();

    return problem;

def partOne(problem, suppress=False):

    # assume excluded does not contain z=26 (no carryover)
    def removeExcluded(word, excluded=[8, 14, 11]):

        for i in range(len(word)):
            letter = word[i];
            if letter in excluded:
                word[i] += 1;
                word = word[:i+1] + [0]*(len(word)-i-1);
                break;

        return word;

    def hasConsecutive(word):

        for i in range(2, len(word)):
            if (word[i] == word[i-1]+1):
                if (word[i] == word[i-2]+2):
                    return True;

        return False;

    def hasDuplicate(word):

        pairs = set();
        for i in range(1, len(word)):
            if (word[i] == word[i-1]):
                pairs.add(word[i]);
                if (len(pairs) >= 2):
                    return True;

        return False;

    def increment(word):

        carry = 1;
        for i in range(len(word)-1, -1, -1):
            new = word[i] + carry;
            word[i] = new % 26;
            carry = 1 if new == 26 else 0;
            if (carry == 0):
                break;

        return word;

    word = [ord(x)-ord("a") for x in problem];
    word = removeExcluded(increment(word));

    while (not hasConsecutive(word) or not hasDuplicate(word)):
        word = removeExcluded(increment(word));

    word = "".join(chr(x+ord("a")) for x in word);
    if (not suppress):
        print("Part 1: {:s}".format(word));

    return word;

def partTwo(problem, partOneSolution):

    word = partOne(partOneSolution, suppress=True);

    print("Part 2: {:s}".format(word));

if __name__ == "__main__":

    print("Solving Day 11, AoC 2015");

    problem = loadProblem();

    partOneSolution = partOne(problem);
    partTwo(problem, partOneSolution);