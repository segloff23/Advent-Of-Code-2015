from math import ceil;

def loadProblem():

    with open("problem.txt") as problemFile:
        problem = dict(tuple(line.split(": "))
                       for line in problemFile.readlines());

    for k in problem:
        problem[k] = int(problem[k].strip());

    return problem;

def winner(player, boss):

    if (player["Damage"] > boss["Armor"]):
        pDamage = player["Damage"] - boss["Armor"];
    else:
        pDamage = 1;

    if (boss["Damage"] > player["Armor"]):
        bDamage = boss["Damage"] - player["Armor"];
    else:
        bDamage = 1;

    hitsToKillBoss = ceil(boss["Hit Points"] / pDamage);
    hitsToKillPlayer = ceil(player["Hit Points"] / bDamage);

    if (hitsToKillBoss <= hitsToKillPlayer):
        return True;
    else:
        return False

def partOne(problem):

    boss = problem;
    player = {"Hit Points": 100, "Damage": 0, "Armor": 0};

    costs = [];
    for w in weapons:
        for a in armor:
            for r in rings:
                for r2 in rings:
                    if (r2 != r or (r2 == "None" and r == "None")):
                        player["Damage"] = weapons[w][1] + armor[a][1] + rings[r][1] + rings[r2][1];
                        player["Armor"] = weapons[w][2] + armor[a][2] + rings[r][2] + rings[r2][2];
                        if (winner(player, boss)):
                            c = weapons[w][0] + armor[a][0] + rings[r][0] + rings[r2][0];
                            costs.append((c, w, a, r, r2));

    best = min(costs, key=lambda x: x[0]);

    print("Part 1: {:d}".format(best[0]));

def partTwo(problem):

    boss = problem;
    player = {"Hit Points": 100, "Damage": 0, "Armor": 0};

    costs = [];
    for w in weapons:
        for a in armor:
            for r in rings:
                for r2 in rings:
                    if (r2 != r or (r2 == "None" and r == "None")):
                        player["Damage"] = weapons[w][1] + armor[a][1] + rings[r][1] + rings[r2][1];
                        player["Armor"] = weapons[w][2] + armor[a][2] + rings[r][2] + rings[r2][2];
                        if (not winner(player, boss)):
                            c = weapons[w][0] + armor[a][0] + rings[r][0] + rings[r2][0];
                            costs.append((c, w, a, r, r2));

    worst = max(costs, key=lambda x: x[0]);

    print("Part 2: {:d}".format(worst[0]));

if __name__ == "__main__":

    print("Solving Day 21, AoC 2015");

    weapons = {"Dagger":     ( 8, 4, 0),
               "Shortsword": (10, 5, 0),
               "Warhammer":  (25, 6, 0),
               "Longsword":  (40, 7, 0),
               "Greataxe":   (74, 8, 0)};

    armor = {"None":         ( 0, 0, 0),
             "Leather":      (13, 0, 1),
             "Chainmail":    (31, 0, 2),
             "Splintmail":   (53, 0, 3),
             "Bandedmail":   (75, 0, 4),
             "Platemail":   (102, 0, 5)};

    rings = {"None":         ( 0, 0, 0),
             "Damage +1":    (25, 1, 0),
             "Damage +2":    (50, 2, 0),
             "Damage +3":   (100, 3, 0),
             "Defense +1":   (20, 0, 1),
             "Defense +2":   (40, 0, 2),
             "Defense +3":   (80, 0, 3)};

    problem = loadProblem();

    partOne(problem);
    partTwo(problem);