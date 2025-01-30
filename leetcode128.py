# Longest Consecutive Sequence
# Diffulty: Medium
# Description: Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

from collections import defaultdict


def longestConsecutive(nums: list[int]) -> int:
    
    consec_count = defaultdict(int)
    starting_nums = []
    max_count = 1
    count = 1

    # Edge case where there is an empty list
    if nums == []: return 0

    # Get the count of each element
    for n in nums: consec_count[n] = consec_count[n] + 1

    # Find the starting numbers
    for n in nums:
        if consec_count[n-1] > 0: pass
        else: starting_nums.append(n)
    
    # Go through each starting value to find the longest sequence
    for n in starting_nums:
        while count > 0:
            if consec_count[n + count] > 0:
                count = count + 1
                if count > max_count: max_count = count
            else: count = 0
        count = 1

    return max_count

def main():
    nums = [2,20,4,10,3,4,5]
    max_count = longestConsecutive(nums)
    print(max_count)

if __name__ == "__main__":
    main()