# 242. Valid Anagram

# Description:
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.


from collections import Counter

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t): return False
    c1 = Counter(s)
    c2 = Counter(t)
    if c1 == c2:
        return True
    else:
        return False
    
def main():
    s = "racecar"
    t = "carrace"

    Anagram = isAnagram(s, t)
    print(Anagram)

    
if __name__ == "__main__":
    main()