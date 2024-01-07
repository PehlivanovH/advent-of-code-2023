def calc_difference(sequences):
    last = sequences[-1]
    if all(element == 0 for element in last):
        return;

    new_sequence = []
    for i in range(len(last) - 1):
        new_sequence.append(last[i + 1] - last[i])
    sequences.append(new_sequence)
    
    calc_difference(sequences)

def predict_next_value(line):
    input = list(map(int, line.split()))
    sequences = [input]
    calc_difference(sequences)

    for i in range(len(sequences) - 1, -1, -1):        
        if i == len(sequences) - 1:
            sequences[i].append(0)
        else:
            sequences[i].insert(0, sequences[i][0] - sequences[i + 1][0])

    return sequences[0][0]

if __name__ == "__main__":
    with open('day9/input', 'r') as file:
        print(sum(map(predict_next_value, file.readlines())))