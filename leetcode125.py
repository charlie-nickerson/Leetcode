# Valid Palindrome
# Difficulty: Easy
# Description: A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

def isPalindrome(s: str) -> bool:
    # remove uppercase and non alphanumerical characters
    processed_string = "".join(ch for ch in s.lower() if ch.isalnum())
    print(processed_string)

    # Compare the string to its reversed version
    if processed_string == str("".join(reversed(processed_string))): return True
    return False
        
def main():
    string = "Was it a car or a cat I saw?"
    isValid = isPalindrome(string)
    print(isValid)

if __name__ == "__main__":
    main()