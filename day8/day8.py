import math
if __name__ == "__main__":
    with open('day8/input', 'r') as file:
        steps = file.readline().rstrip()
        file.readline()
        map = {}
        for line in file.readlines():
            map[line.split(' = ')[0]] = {'L': line.split(' = ')[1].rstrip().split(', ')[0][1:], 'R': line.split(' = ')[1].rstrip().split(', ')[1][:-1]}

        stepcount = 0
        locations = []
        paths = []
        for location in map.keys():
            if location[-1] == 'A':
                locations.append(location)
        
        for path in locations:
            while(True):
                path = map[path][steps[stepcount % len(steps)]]
                stepcount += 1
                if path[-1] == 'Z':
                    paths.append(stepcount)
                    stepcount = 0
                    break

        lcm = math.lcm(*paths)
        print(lcm)