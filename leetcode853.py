# Car Fleet
# Difficulty: Medium
# Description: There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.
# You are given two integer array position and speed, both of length n, where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.
# A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.
# A car fleet is a car or cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.
# If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.
# Return the number of car fleets that will arrive at the destination.



def carFleet(target, position, speed):
    car_info = []
    
    for i in range(len(position)):
        car_info.append((position[i], speed[i]))
    car_info.sort(key=lambda x: x[0])
    car_info.reverse()

    stack = []
    for p, s in car_info:
        stack.append((target - p) / s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
        
            
    return len(stack)

def main():
    target = 12
    position = [10,8,0,5,3]
    speed = [2,4,1,1,3]

    fleet_count = carFleet(target, position, speed)
    print(fleet_count)

if __name__ == "__main__":
    main()

    