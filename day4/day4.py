def filter_winning_numbers(ticket):
    winning_numbers = list(filter(lambda x: x != '', ticket.split(' | ')[0].split(' ')))
    my_numbers = list(filter(lambda x: x != '', ticket.split(' | ')[1].split(' ')))
    return list(filter(lambda x: x in winning_numbers, my_numbers))

if __name__ == "__main__":
    with open('day4/test_input', 'r') as file:
        lines = file.readlines()
        print(list(map(filter_winning_numbers, map(lambda x: x.split(': ')[1].strip(), lines))))