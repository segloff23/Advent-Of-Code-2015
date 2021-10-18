
def loadProblem():

    with open("problem.txt") as problemFile:
        problem = [line.strip() for line in problemFile.readlines()];

    return problem;

def partOne(problem):

    def hasAtLeastNvowels(word, N):
        count = 0;
        for vowel in "aeiou":
            count += word.count(vowel);
            if (count >= N):
                return True;
        return False;

    def hasDuplicate(word):

        for i in range(1, len(word)):
            if (word[i-1] == word[i]):
                return True;

        return False;

    def excludesSubstrings(word, substrings):

        for string in substrings:
            if string in word:
                return False;

        return True;

    exclusions = ["ab", "cd", "pq", "xy"];

    niceStrings = 0;
    for word in problem:
        if (
        hasAtLeastNvowels(word, 3)
            and
        hasDuplicate(word)
            and
        excludesSubstrings(word, exclusions)
        ):
            niceStrings += 1;

    print("Part 1: {:d}".format(niceStrings));

def partTwo(problem):

    def hasProperDuplicate(word):

        for i in range(1, len(word)):
            pair = word[i-1:i+1];
            if (pair in word[i+1:]):
                return True;

        return False;

    def hasSpacedPair(word):

        for i in range(2, len(word)):
            if (word[i-2] == word[i]):
                return True;

        return False;

    niceStrings = 0;
    for word in problem:
        if (hasProperDuplicate(word) and hasSpacedPair(word)):
            niceStrings += 1;

    print("Part 2: {:d}".format(niceStrings));


if __name__ == "__main__":

    print("Solving Day  5, AoC 2015");

    problem = loadProblem();

    partOne(problem);
    partTwo(problem);