"""

"""
def isValidPrefs(manPrefs, womanPrefs):
    # Check both lists of preferences are equal length
    n = len(manPrefs)
    if len(womanPrefs) != n:
        return False

    # Check each list contains an order of preferences for other gender from 0 to n-1
    for i in range(n):
        if i not in manPrefs or i not in womanPrefs:
            return False
    
    return True

def isValidMatching(matching):
    # Check all matchings are to index from 0 to n-1
    n = len(matching)
    manMatches = [x[0] for x in matching]
    womanMatches = [x[1] for x in matching]
    for i in range(n):
        if i not in manMatches or i not in womanMatches:
            return False

    return True

def getMatchingPair(matching, gender, index):
    """
    Return the (man,woman) pair that the person is in, None if not matched 
    gender = "m" for man, "w" for woman
    """
    i = 0 if gender =="m" else 1
    for pair in matching:
        if pair[i] == index:
            return pair
    return None

def getStableMatching(manPrefs, womanPrefs):
    """
    Generate a stable matching using Gale-Shapley/deferred-acceptance algorithm
    """
    # Check that the matching is valid
    #if not isValidPrefs(manPrefs, womanPrefs):
        #raise ValueError("Invalid preferences")
    
    n = len(manPrefs)
    matching = []

    # List of free men by index (man who has not been paired with a woman) from 0 to n-1
    freeMen = [x for x in range(n)]
    # Keep track of which women each man has already proposed to
    # proposals[i][j] = 1 if man i has already proposed to woman j, else 0
    proposals = [[0] * n for _ in range(n)]

    ncalls = 0
    while len(freeMen) > 0:
        ncalls += 1
        if ncalls > 10:
            pass
        # Find a man who has not proposed to every woman yet
        candidate = None
        for m in freeMen:
            if 0 in proposals[m]:
                candidate = m
                break
        # Exit if cannot find a candidate
        if candidate is None:
            break

        # Find the woman highest on his preference list that he has not proposed to
        for i in range(n):
            w = manPrefs[candidate][i]
            if proposals[candidate][w] == 0:
                break

        # Propose to this woman
        proposals[m][w] = 1

        # A woman who has been proposed to always gets paired, so check matchings 
        # to see if she has already been proposed to
        pair = getMatchingPair(matching, "w", w)

        # If the woman is not matched, she is instantly matched
        if pair is None:
            matching.append((m, w))
            freeMen.remove(m)
        # 
        else:
            mOld = pair[0]
            # lower index = higher preference
            if womanPrefs[w].index(m) < womanPrefs[w].index(mOld):
                matching.remove(pair)
                freeMen.append(mOld)
                freeMen.remove(m)
                #proposals[mOld] = [0]*n
                matching.append((m, w))
            else:
                continue
    
    return matching

def isMatchingStable(matching, manPrefs, womanPrefs):
    n = len(manPrefs)
    # Search all men and women, find their match and see if they prefer each other 
    # over the one they are currently with
    for w in range(n):
        for m in range(n):
            wPair = getMatchingPair(matching, "w", w)
            mPair = getMatchingPair(matching, "m", m)
            if womanPrefs[w].index(m) < womanPrefs[w].index(wPair[0]) and manPrefs[m].index(w) < manPrefs[m].index(mPair[1]):
                # print debug?
                return False
    return True


if __name__ == "__main__":
    """
    manPrefs = [[0,1], [0,1]]
    womanPrefs = [[0,1], [0,1]]
    manPrefs = [[0,1], [1,0]]
    womanPrefs = [[1,0], [0,1]]
    """
    manPrefs = [
        [1,3,0,2],
        [2,0,3,1],
        [1,2,0,3],
        [3,0,2,1],
    ]
    womanPrefs = [
        [1,0,3,2],
        [3,2,0,1],
        [0,3,2,1],
        [1,0,3,2],
    ]
    
    #matching = getStableMatching(manPrefs, womanPrefs)
    matching = [(0,0),(1,1),(2,2),(3,3)]
    print(matching)
    print(isMatchingStable(matching, manPrefs, womanPrefs))
