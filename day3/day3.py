
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

def findNumber(schematic, row_index, element_index):
    number = schematic[row_index][element_index]
   
    leftIndex = element_index - 1;
    while leftIndex >= 0 and schematic[row_index][leftIndex].isdigit():
        number = schematic[row_index][leftIndex] + number
        leftIndex -= 1

    rightIndex = element_index + 1;
    while rightIndex < len(schematic[row_index]) and schematic[row_index][rightIndex].isdigit():
        number = number + schematic[row_index][rightIndex]
        rightIndex += 1

    return int(number)
    

def checkForNeighbor(positions, element_index, row_index, schematic, rows, cols):
    # Iterate over the relative positions
    for dx, dy in positions:
        x = row_index + dx
        y = element_index + dy
        
        # Check if the position is within the bounds of the schematic
        if 0 <= x < rows and 0 <= y < cols:
            if schematic[x][y].isdigit():
                return findNumber(schematic, x, y)
            
    return 0

def findRatio(schematic, element_index, row_index):
    rows = len(schematic)
    cols = len(schematic[0])
    
    # Define the relative positions of the neighbours
    toppositions = [
        (-1, -1),  # top-left
        (-1, 0),   # top
        (-1, 1),   # top-right
    ]

    bottompositions = [
        (1, -1),   # bottom-left
        (1, 0),    # bottom
        (1, 1)     # bottom-right
    ]

    leftpositions = [
        (0, -1),   # left
    ]
    
    rightpositions = [
        (0, 1),    # right
    ]

    topNumber = checkForNeighbor(toppositions, element_index, row_index, schematic, rows, cols)
    bottomNumber = checkForNeighbor(bottompositions, element_index, row_index, schematic, rows, cols)
    leftNumber = checkForNeighbor(leftpositions, element_index, row_index, schematic, rows, cols)
    rightNumber = checkForNeighbor(rightpositions, element_index, row_index, schematic, rows, cols)
    
    numbers = [num for num in [topNumber, bottomNumber, leftNumber, rightNumber] if num != 0]
    
    if len(numbers) == 2:
         # Calculate the multiplication of the numbers
        multiplication = 1
        for num in numbers:
            multiplication *= num
        return multiplication

    return 0
   

def part2():
    schematic = read_file("day3/test_input2")

    numbers = 0
    for row_index, row in enumerate(schematic):
        for element_index, element in enumerate(row):
            if element == '*':
                numbers += findRatio(schematic, element_index, row_index)

    print(numbers)

if __name__ == "__main__":
    part2()
