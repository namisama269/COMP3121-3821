"""
3 solutions to 0-1 knapsack problem, each optimises the space complexity
from O(nw) to O(1w)
x = capacity, v = values, w = weight, n = number of values/weights


Basic 2D solution. 
dp[i][j] = max value for capacity j from a subset of values 0,...,i

Space complexity = O(nx)
"""
def O_nx(x, v, w):
    n = len(v)
    dp = [[0 for _ in range(x+1)] for __ in range(n)]

    for i in range(n):
        for j in range(x+1):
            if i == 0:
                # base case: either can or cannot fit the first item
                dp[i][j] = v[0] if j >= w[0] else 0
            else:
                # the max value is at least as good as for the previous
                # subset since given values 1,...,i, not including value i
                # results in a subset of 1,...,i-1
                dp[i][j] = dp[i-1][j]
                # if can fit item i into capacity j, then another possible 
                # candidate for max value is putting item i into the knapsack 
                # and optimally filling the remaining capacity with previous
                # i-1 items.
                if w[i] <= j:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])

    return dp[n-1][x]

"""
In the basic solution, when looking at the row i, only need the values
from row i-1. Keep track of the current and previous row at each iteration.

Space complexity = O(2x)
"""
def O_2x(x, v, w):
    n = len(v)
    dp = [[0 for _ in range(x+1)] for __ in range(2)]
    curr = dp[0]
    prev = dp[1] # doesn't matter which order curr and prev initially

    for i in range(n):
        # swap the rows before iterating
        curr, prev = prev, curr
        for j in range(x+1):
            if i == 0:
                curr[j] = v[0] if j >= w[0] else 0
            else:
                curr[j] = prev[j]
                if w[i] <= j:
                    curr[j] = max(prev[j], prev[j-w[i]] + v[i])

    return curr[x]

"""
When looking at entry dp[i][j], we only look at dp[i-1][k], where k <= j.
So if we iterate the columns from right to left, the subproblems in a column
that have not been reached still represent the previous row (i-1). So only 
one row is needed.

Space complexity = O(1x)
"""
def O_1x(x, v, w):
    n = len(v)
    dp = [0 for _ in range(x+1)]

    for i in range(n):
        for j in range(x,-1,-1):
            if i == 0:
                dp[j] = v[0] if j >= w[0] else 0
            else:
                if w[i] <= j:
                    dp[j] = max(dp[j], dp[j-w[i]] + v[i])      

    return dp[x]


if __name__ == "__main__":
    x = int(input("Enter capacity: "))
    v = [int(x) for x in input("Enter values: ").split()]
    w = [int(x) for x in input("Enter weights: ").split()]
    if len(v) != len(w):
        raise ValueError("Enter same number of values and weights")
    print()
    # Check that all 3 return the same solution
    print(O_nx(x, v, w))
    print(O_2x(x, v, w))
    print(O_1x(x, v, w))
