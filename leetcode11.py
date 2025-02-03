# Container With Most Water
# Difficulty: Medium
# Description: You are given an integer array heights where heights[i] represents the height of the ithith bar.
# You may choose any two bars to form a container. Return the maximum amount of water a container can store.

def maxArea(heights: list[int]) -> int:

    # AREA = (i2 - i1)*(min(heights[i1], heights[i2]))
    # Need to maximize the area
    # Increases distance between indexes increase the area
    # 

    rptr = len(heights) - 1
    lptr = 0
    m_area = 0

    while rptr != lptr:
        area = (rptr - lptr) * min(heights[lptr], heights[rptr])
        if area > m_area:
            m_area = area
        if heights[lptr] <= heights[rptr]:
            lptr += 1
        else:
            rptr -= 1
        
    return m_area

def main():
    h = [1,7,2,5,4,7,3,6]
    m_area = maxArea(h)
    print(m_area)

if __name__ == "__main__":
    main()
