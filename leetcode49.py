from collections import defaultdict
# Group Anagram

# Description: Given an array of strings strs, group the anagrams
# together. You can return the answer in any order

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagram_groups = defaultdict(list)
    for word in strs:
        letters = [0] * 26
        for letter in word:
            letters[ord(letter) - ord('a')] += 1
        anagram_groups[tuple(letters)].append(word)
    return anagram_groups.values()

def main():
    anagrams = ["act","pots","tops","cat","stop","hat"]
    groups = groupAnagrams(anagrams)
    print(groups)

if __name__ == "__main__":
    main()