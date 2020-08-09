def determineTruth(s1, s2, s3, i, j, cache):
    k = i + j

    if i == len(s1) and j == len(s2):
        return True
    if (i, j) in cache:
        return cache[i, j]
    
    found = False
    if i < len(s1) and s1[i] == s3[k]:
        found = determineTruth(s1, s2, s3, i+1, j, cache) or found
    
    if j < len(s2) and s2[j] == s3[k]:
        found = determineTruth(s1, s2, s3, i, j+1, cache) or found
    
    cache[i,j] = found
    return found
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        return determineTruth(s1, s2, s3, 0, 0, {})

solution = Solution()

test1 = {
    's1': "aabcc",
    's2': "dbbca",
    's3': "aadbbcbcac"
}

test2 = {
    's1': "aabcc",
    's2': "dbbca",
    's3': "aadbcbbcac"
}

test3 = {
    's1': "aabd",
    's2': "abdc",
    's3': "aabdabcd"
}

test4 = {
    's1': "aabaabcd",
    's2': "abad",
    's3': "aabadabc"
}

print(solution.isInterleave(test1['s1'], test1['s2'], test1['s3']))
print(solution.isInterleave(test2['s1'], test2['s2'], test2['s3']))
print(solution.isInterleave(test3['s1'], test3['s2'], test3['s3']))
print(solution.isInterleave(test4['s1'], test4['s2'], test4['s3']))