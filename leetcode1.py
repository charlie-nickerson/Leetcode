# Two Sum

# Description: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

from collections import Counter

def twoSum(nums: list[int], target: int) -> list[int]:
    c = Counter(nums)
    for i in range(len(nums)):
        dif = target - nums[i]
        if c[dif] > 0:
            print("index {value} is i".format(value = i))
            for j in range(i, len(nums)):
                if dif == nums[j] and i != j:
                    print("index {value} is j".format(value = j))
                    return [i, j]
        else: print("{value} is not index i".format(value = i))

def main():
    nums = [3,4,5,6]
    target = 7
    two_sum = twoSum(nums, target)
    print("The two indexes that sum to {target} are {sum}".format(target = target, sum = two_sum))

if __name__ == "__main__":
    main()