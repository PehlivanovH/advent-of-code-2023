from functools import reduce

def countWinningMoves(time, distance, speed):
    if time == 0:
        return 0
    elif time * speed > distance:
        return 1 + countWinningMoves(time - 1, distance, speed + 1)
    else:
        return countWinningMoves(time - 1, distance, speed + 1)

def calculate(race):
    return countWinningMoves(race[0], race[1], 0)

def part1():
    with open('day6/test_input', 'r') as file:
        time = list(map(int, filter(None, file.readline().split(':')[1].rstrip().split(' '))))
        distance = list(map(int, filter(None, file.readline().split(':')[1].rstrip().split(' '))))

        result = reduce(lambda x, y: x * y, map(calculate, zip(time, distance)))
        print(result)

if __name__ == "__main__":
    with open('day6/input', 'r') as file:
        time = list(map(int, filter(None, file.readline().split(':')[1].rstrip().split(' '))))
        distance = list(map(int, filter(None, file.readline().split(':')[1].rstrip().split(' '))))

        speed = 0
        racetime = time[0]
        racedistance = distance[0]

        sum = 0

        while(racetime > 0):
            if racetime * speed > racedistance:
                sum += 1
            racetime -= 1
            speed += 1

        print(sum)
