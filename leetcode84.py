# Largest Rectangle in Histogram
# Difficulty: HARD
# Description: Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []  # Stack will store indices
        max_area = 0
        heights.append(0)  # Add a sentinel value to handle the last bars
        
        for i, height in enumerate(heights):
            start = i
            
            # While stack is not empty and current height is smaller than height at stack top
            while stack and height < heights[stack[-1]]:
                # Pop the stack and calculate area with the popped bar as height
                h = heights[stack.pop()]
                # Width is current position minus the new stack top (or start of array)
                w = i - (stack[-1] if stack else -1) - 1
                max_area = max(max_area, h * w)
            
            stack.append(i)
        
        return max_area

def main():
     heights = [2,4]
     output = largestRectangleArea(heights=heights)
     print(output)

if __name__ == "__main__":
     main()
