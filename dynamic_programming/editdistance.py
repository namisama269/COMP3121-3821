"""
Find the minimum number of edits required to turn word1 into word2

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
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