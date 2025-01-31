# Two Sum II : Input Array is sorted
# Difficulty: Medium
# Description: Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
#The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

def twoSum(numbers: list[int], target: int) -> list[int]:
    lptr = 0
    rptr = 1

    while rptr < len(numbers):
        if target == numbers[lptr] + numbers[rptr]:
            return [lptr+1, rptr+1]
        else: 
            rptr = rptr + 1
            if rptr >= len(numbers):
                lptr = lptr + 1
                rptr = lptr + 1

def main():
    numbers = [1,2,3,4]
    target = 3
    indices = twoSum(numbers, target)
    print(indices)

if __name__ == "__main__":
    main()