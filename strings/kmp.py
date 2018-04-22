def kmp(s, t):
    pi = getPi(t)
    matched = False
    j = 0
    for i in range(len(s)):
        if j < len(t):
            if t[j] != s[i] and j > 0:
                j = pi[j-1]
            elif t[j] == s[i]:
                j += 1
        if j == len(t):
            return True
    return matched

def getPi(t):
    pi = [0 for _ in range(len(t))]
    for i in range(1, len(t)):
        if pi[i-1] > 0:
            if t[i] == t[pi[i-1] + 1]:
                pi[i] = pi[i-1] + 1
            else:
                pi[i] = 0
        else:
            if t[i] == t[0]:
                pi[i] = 1
            else:
                pi[i] = 0
    return pi


if __name__ == "__main__":
    s = "abcefgabcdefg"
    t = "abcde"
    print s
    print t
    print kmp(s, t)
