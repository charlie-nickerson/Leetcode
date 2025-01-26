# 217 Contains Duplicates
# Description: Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

def hasDuplicate(nums: list[int]) -> bool:
    if len(list(set(nums))) == len(nums): return False
    return True

def main():
    nums = [1,2,4,4]
    isDuplicate = hasDuplicate(nums)
    print(isDuplicate)

if __name__ == "__main__":
    main()
         