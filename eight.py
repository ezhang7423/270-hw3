import numpy as np
import scipy
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable, LpMinimize
from scipy.optimize import linprog

A = np.array(
    [
        [2, 6, -2, 10],
        [-6, -4, -3, -6],
        [0, 4, -3, -8],
    ]
)

B = np.array(
    [
        [0, 1, 2, 3],
        [1, 0, 1, 2],
        [0, 1, 0, 1],
        [-1, 0, 1, 0],
    ]
)


def solve_for_saddle(A):

    y, v = saddle_helper(A, 0)
    z, v2 = saddle_helper(A, 1)
    # Get the results
    print("Mixed value:", v.value())
    print("Optimal policy for P2:")
    for var in y.values():
        print(f"{var.name}: {var.value()}")

    print("Optimal policy for P1:")
    for i, var in enumerate(z.values()):
        print(f"z{i}: {var.value()}")

    assert v == v2

def saddle_helper(A, dim):
    # Define the model
    if dim == 0:
        model = LpProblem(sense=LpMinimize)
    else:
        model = LpProblem(sense=LpMaximize)

    # Define the decision variables
    y = {i: LpVariable(name=f"y{i}", lowBound=0) for i in range(A.shape[dim])}
    v = LpVariable(name="v")

    y_np = np.array([y[i] for i in range(A.shape[dim])])

    # Add constraints
    model += (lpSum(y.values()) == 1, "prob dis")

    if dim == 0:
        for i in range(A.shape[dim]):        
            model += (
                np.dot(A.T[i], y_np) <= v,
                f"security policy def {i}",
            )
    else:
        for i in range(A.shape[0]):        
            model += (
                np.dot(A[i], y_np) >= v,
                f"security policy def {i}",
            )

    # objective
    model += v

    # Solve the optimization problem
    model.solve()

    return y, v

if __name__ == '__main':
    solve_for_saddle(A)
    solve_for_saddle(B)