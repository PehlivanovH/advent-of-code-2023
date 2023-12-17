from functools import reduce

def extractCubeColorsForGame(game):
    cubes = game.replace('; ', ', ').split(', ')
    return reduce(lambda acc, cube: {**acc, cube.split(' ')[1]: max(acc[cube.split(' ')[1]], int(cube.split(' ')[0]))}, cubes, {'blue': 0, 'red': 0, 'green': 0})

def mapToDatastructure(line):
    return {
        'gameId': int(line.split(': ')[0].split(' ')[1]),
        'cubeColors': extractCubeColorsForGame(line.split(': ')[1].rstrip('\n'))
    }

def isGamePossible(game):
    return game.get('cubeColors').get('blue') <= 14 and game.get('cubeColors').get('red') <= 12 and game.get('cubeColors').get('green') <= 13

if __name__ == "__main__":
    with open('day2/input', 'r') as file:
        lines = file.readlines()
        print(sum(map(lambda game: game.get('gameId'), filter(isGamePossible, map(mapToDatastructure, lines)))))
        print(sum(map(lambda game: game.get('cubeColors').get('red') * game.get('cubeColors').get('green') * game.get('cubeColors').get('blue'), map(mapToDatastructure, lines))))

