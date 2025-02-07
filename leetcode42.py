# Max Rain Water
# Difficulty: HARD
# Description: You are given an array non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.
# Return the maximum area of water that can be trapped between the bars.


def trap(height: list[int]) -> int:
    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]
    res = 0

    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]
    return res

def main():
    height = [0,2,0,3,1,0,1,3,2,1]
    maxWater= trap(height)
    print(maxWater)

if __name__ == "__main__":
    main()