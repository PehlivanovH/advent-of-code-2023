import sys

seeds = []
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

current = []

def readSeeds(line):
    global seeds
    seeds = list(map(int, filter(None, line.split(':')[1].rstrip().split(' '))))

def readMaps(line):
    global current
    numbers = list(map(int, line.rstrip().split(' ')))
    # destination, source, length
    current.append([numbers[0], numbers[1], numbers[2]])

def read_input(line):
    global current, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location
    if line.strip() == '':
        return
    if 'seeds' in line:
        readSeeds(line)
        return
    if 'seed-to-soil' in line:
        current = seed_to_soil
        return
    if 'soil-to-fertilizer' in line:
        current = soil_to_fertilizer
        return
    if 'fertilizer-to-water' in line:
        current = fertilizer_to_water
        return
    if 'water-to-light' in line:
        current = water_to_light
        return
    if 'light-to-temperature' in line:
        current = light_to_temperature
        return
    if 'temperature-to-humidity' in line:
        current = temperature_to_humidity
        return
    if 'humidity-to-location' in line:
        current = humidity_to_location
        return
    readMaps(line)

def findValue(range, key):
    # range: [destination, source, length]
    for item in range:
        if item[1] <= key and item[1] + item[2] > key:
            return item[0] + key - item[1]
        
    return key

def findBackwards(ranges, key):
    # range: [destination, source, length]
    for item in ranges:
        if item[0] <= key and item[0] + item[2] > key:
            return item[1] + key - item[0]
        
    return key

def findLocation(seed):
    global current, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location
    soil = findValue(seed_to_soil, seed)
    fertilizer = findValue(soil_to_fertilizer, soil)
    water = findValue(fertilizer_to_water, fertilizer)
    light = findValue(water_to_light, water)
    temperature = findValue(light_to_temperature, light)
    humidity = findValue(temperature_to_humidity, temperature)
    location = findValue(humidity_to_location, humidity)
    return location

def findSeed(location):
    global current, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location
    humidity = findBackwards(humidity_to_location, location)
    temperature = findBackwards(temperature_to_humidity, humidity)
    light = findBackwards(light_to_temperature, temperature)
    water = findBackwards(water_to_light, light)
    fertilizer = findBackwards(fertilizer_to_water, water)
    soil = findBackwards(soil_to_fertilizer, fertilizer)
    seed = findBackwards(seed_to_soil, soil)

    for i in range(0, len(seeds), 2):
        seed1 = seeds[i]
        length = seeds[i+1]
        if seed1 <= seed and seed1 + length > seed:
            return seed

    return -1

def part1():
    global current, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location
    with open('day5/test_input', 'r') as file:
        list(map(read_input, file.readlines()))
    
    print(min(map(findLocation, seeds)))

def part2():
    global current, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location
    with open('day5/input', 'r') as file:
        list(map(read_input, file.readlines()))

    '''
    min_value = sys.maxsize
    for i in range(0, len(seeds), 2):
        seed1 = seeds[i]
        length = seeds[i+1]
        
        for j in range(seed1, seed1 + length):
            location = findLocation(j)
            if location < min_value:
                min_value = location
    '''
    for i in range (0, sys.maxsize):
        seed = findSeed(i)
        if seed != -1:
            print(i)
            break

if __name__ == "__main__":
    part2()
