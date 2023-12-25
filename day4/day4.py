def winning_numbers(ticket):
    winning_numbers = list(filter(lambda x: x != '', ticket.split(' | ')[0].split(' ')))
    my_numbers = list(filter(lambda x: x != '', ticket.split(' | ')[1].split(' ')))
    return list(filter(lambda x: x in winning_numbers, my_numbers))

def part1():
    with open('day4/input', 'r') as file:
        lines = file.readlines()
        print(sum(map(lambda winning: 2 ** (len(winning) - 1), filter(lambda winning: len(winning) > 0, map(winning_numbers, map(lambda x: x.split(': ')[1].strip(), lines))))))

def part2():
    tickets = []
    with open('day4/input2', 'r') as file:
        tickets = list(map(lambda ticket: {'count': 1, 'ticket':ticket.split(': ')[1].strip()}, file.readlines()))

    for index, ticket in enumerate(tickets):
        winning = winning_numbers(ticket['ticket'])
        for i in range(len(winning)):
            tickets[index + i + 1]['count'] += ticket['count']

    print(sum(map(lambda ticket: ticket['count'], tickets)))

if __name__ == "__main__":
    part2()