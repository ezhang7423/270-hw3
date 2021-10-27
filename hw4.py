import numpy as np
from eight import solve_for_saddle
VALS = {
    "TLTL": 1,
    "TLTR": -1,
    "TLBL": 1,
    "TLBR": -1,
    "TRTL": -2,
    "TRTR": -1,
    "TRBL": 1,
    "TRBR": -1,
    "BLTL": -1,
    "BLTR": -3,
    "BLBL": -3,
    "BLBR": -1,
    "BRTL": -1,
    "BRTR": 2,
    "BRBL": -1,
    "BRBR": 2,
}
cor_p1 = {"TL": 1, "TR": 2, "BL": 3, "BR": 4}
cor_p2 = {
    "TLT": 1,
    "TLB": 1,
    "TRT": 2,
    "TRB": 3,
    "BLT": 4,
    "BLB": 4,
    "BRT": 5,
    "BRB": 5,
}


def genbin(n, vals, bs=""):
    all_moves = []
    if n - 1:
        all_moves += genbin(n - 1, vals, bs + vals[0])
        all_moves += genbin(n - 1, vals, bs + vals[1])
    else:
        return [vals[0] + bs, vals[1] + bs]
    return all_moves


p1_moves = genbin(5, ["T", "B"])
p2_moves = genbin(6, ["L", "R"])


def get_val(p1_policy, p2_policy):
    s = p1_policy[0] + p2_policy[0]
    s += p1_policy[cor_p1[s]]
    s += p2_policy[cor_p2[s]]
    return VALS[s]


game = np.zeros((len(p1_moves), len(p2_moves)))
for i, p1_policy in enumerate(p1_moves):
    for j, p2_policy in enumerate(p2_moves):
        game[i][j] = get_val(p1_policy, p2_policy)


pure_security_level_p1 = min([max(row) for row in game])
pure_security_level_p2 = max([min(row) for row in game.T])
print('pure_security_level_p1:', pure_security_level_p1)
print('pure_security_level_p2', pure_security_level_p2)

solve_for_saddle(game)