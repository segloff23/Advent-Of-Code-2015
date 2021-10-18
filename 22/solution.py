
def loadProblem():

    with open("problem.txt") as problemFile:
        problem = problemFile.read().strip();

    return problem;

def applyMM(pHP, bHP, mana, s, p, r):

    bHP -= 4;
    mana -= SPELL_MANA["MM"];

    return (pHP, bHP, mana, s, p, r);

def applyDrain(pHP, bHP, mana, s, p, r):

    bHP -= 2;
    pHP += 2;
    mana -= SPELL_MANA["Drain"];

    return (pHP, bHP, mana, s, p, r);

def applyShield(pHP, bHP, mana, s, p, r):

    if (s != 0):
        return None;

    s = 6;
    mana -= SPELL_MANA["Shield"];

    return (pHP, bHP, mana, s, p, r);

def applyPoison(pHP, bHP, mana, s, p, r):

    if (p != 0):
        return None;

    p = 6;
    mana -= SPELL_MANA["Poison"];

    return (pHP, bHP, mana, s, p, r);

def applyRecharge(pHP, bHP, mana, s, p, r):

    if (r != 0):
        return None;

    r = 5;
    mana -= SPELL_MANA["Recharge"];

    return (pHP, bHP, mana, s, p, r);

def partOne(problem, hard=False, suppress=False):

    def updateAll(pHP, bHP, mana, s, p, r):

        if (p >= 1):
            bHP -= 3;
            p -= 1;
        if (r >= 1):
            mana += 101;
            r -= 1;
        if (bHP <= 0):
            return (pHP, bHP, mana, s, p, r);

        if (s >= 1):
            pHP -= max(1, BOSS_DAMAGE - 7)
            s -= 1;
        else:
            pHP -= BOSS_DAMAGE;

        if (hard):
            pHP -= 1;
        if (pHP <= 0):
            return None;

        if (p >= 1):
            bHP -= 3;
            p -= 1;
        if (r >= 1):
            mana += 101;
            r -= 1;
        if (s >= 1):
            s -= 1;

        return (pHP, bHP, mana, s, p, r);

    cache = {}
    parents = {}
    def DP(subprob):

        if (subprob not in cache):
            pHP, bHP, mana, s, p, r = subprob;

            if (bHP <= 0):
                cache[subprob] = 0;
                parents[subprob] = (subprob, "DONE");
            elif (mana < 53 or pHP <= 0):
                cache[subprob] = INF;
            else:
                costs = [];
                for spell in SPELL_MANA:
                    if (mana >= SPELL_MANA[spell]):
                        newProb = SPELL_APPLY[spell](*subprob);
                        if (newProb != None):
                            newProb = updateAll(*newProb);
                            if (newProb != None):
                                costs.append((newProb, spell, SPELL_MANA[spell] + DP(newProb)));

                if (len(costs) == 0):
                    cache[subprob] = INF;
                else:
                    optimal = min(costs, key = lambda x: x[-1]);
                    cache[subprob] = optimal[-1];
                    parents[subprob] = (optimal[0], optimal[1]);

        return cache[subprob];

    pHP = 50;
    bHP = 55;
    mana = 500;

    if (hard):
        pHP -= 1;

    start = (pHP, bHP, mana, 0, 0, 0);
    best = DP(start);

    if (False):
        start = [start, "NA"];
        while (start[1] != "DONE"):
            print(start);
            start = parents[start[0]];
        print(start);


    if (not suppress):
        print("Part 1: {:d}".format(best));

    return best;

def partTwo(problem):

    best = partOne(problem, hard=True, suppress=True);

    print("Part 2: {:d}".format(best));

if __name__ == "__main__":

    print("Solving Day 22, AoC 2015");

    INF = float("inf");
    SPELL_MANA = {"MM": 53, "Drain": 73, "Shield": 113,
                  "Poison": 173, "Recharge": 229}
    SPELL_APPLY = {"MM": applyMM, "Drain": applyDrain, "Shield": applyShield,
                   "Poison": applyPoison, "Recharge": applyRecharge}
    BOSS_DAMAGE = 8;

    problem = loadProblem();

    partOne(problem);
    partTwo(problem);