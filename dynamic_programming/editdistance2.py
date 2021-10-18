"""
Edit distance, but each operation can have a different cost instead of all 1
"""

def minEditDistance(word1, word2, ci=1, cd=1, cr=1):
    len1 = len(word1)
    len2 = len(word2)
    dp = [[0]*(len2+1) for _ in range(len1+1)]
    for i in range(0, len1+1):
        for j in range(0, len2+1):
            if i == 0 or j == 0:
                dp[i][j] = i + j
            else:
                min_candidates = [dp[i-1][j]+1, dp[i][j-1]+1]
                if word1[i-1] == word2[j-1]:
                    min_candidates.append(dp[i-1][j-1])
                if word1[i-1] != word2[j-1]:
                    min_candidates.append(dp[i-1][j-1]+1)
                dp[i][j] = min(min_candidates)
    return dp[len1][len2]