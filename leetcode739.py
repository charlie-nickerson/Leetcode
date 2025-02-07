# Daily Temperatures
# Difficulty: Medium
# Description

def dailyTemperatures(temperatures: list[int]) -> list[int]:
    result = [0]*len(temperatures)
    stack = []


    for index, curTemp in enumerate(temperatures):
        while stack and curTemp > stack[-1][1]:
            i, t = stack.pop()
            result[i] = index - i
        stack.append((index, curTemp))
    
    return result


def main():
    temperatures = [73,74,75,71,69,72,76,73]
    res = dailyTemperatures(temperatures)
    print(res)

if __name__ == "__main__":
    main()