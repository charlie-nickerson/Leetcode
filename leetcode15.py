# 3Sum
# Difficulty: Medium
# Description: Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets. 

def threeSum(nums):
    output = []
    nums.sort()

    for i, n in enumerate(nums):
        if i > 0 and n == nums[i - 1]:
            continue
        
        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = n + nums[l] + nums[r]
            if threeSum > 0:
                r = r - 1
            elif threeSum < 0:
                l = l + 1
            else:
                output.append([n, nums[r], nums[l]])
                l = l + 1
                while nums[l] == nums[l-1] and l < r:
                    l = l + 1

    return output
    

def main():
    nums = [-1,0,1,2,-1,-4]
    output = threeSum(nums)
    print(output)

if __name__ == "__main__":
    main()