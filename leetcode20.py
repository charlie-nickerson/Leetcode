# Valid Parentheses
# Difficulty: Easy
# Description: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:

#    Open brackets must be closed by the same type of brackets.
#    Open brackets must be closed in the correct order.
#    Every close bracket has a corresponding open bracket of the same type.


def isValid(s: str) -> bool:
    stack = []
    
    for c in s :
        if c == "{" or c == "(" or c == "[":
            stack.append(c)
        elif len(stack) == 0 and (c == "}" or c == "]" or c == ")"):
            print(stack)
            return False
        elif c == "}" and stack[-1] == "{":
            stack.pop()
        elif c == ")" and stack[-1] == "(":
            stack.pop()
        elif c == "]" and stack[-1] == "[":
            stack.pop()
        else: return False
    if stack == []: return True
    else: return False

def main():
    s = "(({()}))"
    valid = isValid(s)
    print(valid)

if __name__ == "__main__":
    main()


