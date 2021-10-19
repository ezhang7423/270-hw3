import numpy as np
from eight import solve_for_saddle

def J(R):
    return abs(1 - 1 / R)


dev = np.arange(-10, 11)
nom = np.arange(0.7, 1.21, 0.05)

dev_calc = 1 + (0.01 * dev)


game = np.vstack((dev_calc,) * 11)


for i in range(11):
    game[i] = J(game[i] * nom[i])

#1 
# Game is initialized

#2. 
v_under = min([max(i) for i in game])
v_over = max([min(i) for i in game.T])
print(v_over, v_under)


#3


solve_for_saddle(game)