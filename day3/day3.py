
import itertools


def read_file(filename):
    # Create an empty two-dimensional array
    two_dimensional_array = []

    with open(filename, "r") as file:
        # Iterate over each line in the file
        for line in file:
            # Remove any leading or trailing whitespace
            line = line.strip()
            
            # Split the line into individual characters
            characters = list(line)
            
            # Append the characters to the two-dimensional array
            two_dimensional_array.append(characters)
    
    return two_dimensional_array

def findNeighbours(schematic, elementIndex, rowIndex):
    neighbours = ""
    rows = len(schematic)
    cols = len(schematic[0])
    
    # Define the relative positions of the neighbours
    positions = [
        (-1, -1),  # top-left
        (-1, 0),   # top
        (-1, 1),   # top-right
        (0, -1),   # left
        (0, 1),    # right
        (1, -1),   # bottom-left
        (1, 0),    # bottom
        (1, 1)     # bottom-right
    ]
    
    # Iterate over the relative positions
    for dx, dy in positions:
        x = rowIndex + dx
        y = elementIndex + dy
        
        # Check if the position is within the bounds of the schematic
        if 0 <= x < rows and 0 <= y < cols:
            neighbours += schematic[x][y]
    
    return neighbours

def part1():
    schematic = read_file("day3/input")
    numbers = []
    
    for row_index, row in enumerate(schematic):
        tmp_number = ''
        neighbours = []
        for element_index, element in enumerate(row):
            if element.isdigit():
                tmp_number += element
                neighbours += findNeighbours(schematic, element_index, row_index)
            else:
                neighbours = ''.join(filter(lambda x: not x.isdigit() and x != '.', neighbours))
                if len(tmp_number) > 0 and len(neighbours) > 0:
                    numbers.append(int(tmp_number))
                tmp_number = ''
                neighbours = []

        # Check if there is a number at the end of the row
        neighbours = ''.join(filter(lambda x: not x.isdigit() and x != '.', neighbours))
        if len(tmp_number) > 0 and len(neighbours) > 0:
            numbers.append(int(tmp_number))

    filtered_numbers = sum(numbers)
    print(filtered_numbers)

def findNeighboursWithPos(schematic, elementIndex, rowIndex):
    neighbours = []
    rows = len(schematic)
    cols = len(schematic[0])
    
    # Define the relative positions of the neighbours
    positions = [
        (-1, -1),  # top-left
        (-1, 0),   # top
        (-1, 1),   # top-right
        (0, -1),   # left
        (0, 1),    # right
        (1, -1),   # bottom-left
        (1, 0),    # bottom
        (1, 1)     # bottom-right
    ]
    
    # Iterate over the relative positions
    for dx, dy in positions:
        x = rowIndex + dx
        y = elementIndex + dy
        
        # Check if the position is within the bounds of the schematic
        if 0 <= x < rows and 0 <= y < cols:
            neighbours.append({'char':schematic[x][y], 'pos':(x,y) })
    
    return neighbours

def part2():
    schematic = read_file("day3/input2")
    numbers = []
    
    for row_index, row in enumerate(schematic):
        tmp_number = ''
        neighbours = []
        for element_index, element in enumerate(row):
            if element.isdigit():
                tmp_number += element
                neighbours += findNeighboursWithPos(schematic, element_index, row_index)
            else:
                neighbours = list(filter(lambda x: not x.get('char').isdigit() and x.get('char') == '*', neighbours))
                if len(tmp_number) > 0 and len(neighbours) > 0:
                    numbers.append({'number':int(tmp_number), 'gear': neighbours[0].get('pos')})
                tmp_number = ''
                neighbours = []

        # Check if there is a number at the end of the row
        neighbours = list(filter(lambda x: not x.get('char').isdigit() and x.get('char') == '*', neighbours))
        if len(tmp_number) > 0 and len(neighbours) > 0:
            numbers.append({'number':int(tmp_number), 'gear': neighbours[0].get('pos')})

     # Group numbers by the same 'pos' property
    grouped_numbers = []
    numbers.sort(key=lambda x: x['gear'])
    for pos, group in itertools.groupby(numbers, key=lambda x: x['gear']):
        group_numbers = [number['number'] for number in group]
        grouped_numbers.append({'pos': pos, 'numbers': group_numbers})

    
    grouped_numbers = list(filter(lambda x: len(x['numbers']) == 2, grouped_numbers))
    sum = 0
    for entry in grouped_numbers:
        numbers = entry['numbers']
        product = numbers[0] * numbers[1]
        sum += product

    print(sum)

if __name__ == "__main__":
    part2()
