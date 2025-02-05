# Generate Parentheses
# Difficulty: Medium
# Description: Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

def generateParenthesis(n: int) -> list[str]:
    def backtrack(openCount, closeCount, current, result):
        # Base case: if we've used all parentheses
        if len(current) == 2 * n:
            result.append(current)
            return
            
        # We can add an opening parenthesis if we haven't used all n
        if openCount < n:
            backtrack(openCount + 1, closeCount, current + "(", result)
            
        # We can add a closing parenthesis if we have more open than closed
        if closeCount < openCount:
            backtrack(openCount, closeCount + 1, current + ")", result)

    result = []
    backtrack(0, 0, "", result)
    return result



def main():
    # Example usage:
    for i in range(1, 5):
        print(f"\nFor n = {i}:")
        print(generateParenthesis(i))

if __name__ == "__main__":
    main()
