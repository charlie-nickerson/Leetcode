# Valid Parentheses
# Difficulty: Easy
# Description: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:

#    Open brackets must be closed by the same type of brackets.
#    Open brackets must be closed in the correct order.
#    Every close bracket has a corresponding open bracket of the same type.


def isOpen(c: str) -> bool:
    if c == "[" or c == "{" or c == "(":
        return True
    else:
        return False

def isValid(s: str) -> bool:
    set_count = 0
    p = []

    # Check if the array length is even
    if len(s) % 2 != 0: return False

    elif not isOpen(s[0]):
        return False
    else:
        for c in s:
            if isOpen(c):
                s.append(c)


