import re

def filter_digits(input):
    return ''.join(filter(lambda character: character.isdigit(), input))

def first_last_digit(digits):
    return digits[0] + digits[-1]

def find_calibration_value(line):
    return int(first_last_digit(filter_digits(line)))

word_to_digit = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9'
    }

FIND_FROM_BEGINNING = lambda input, x: input[:x]
FIND_FROM_END = lambda input, x: input[-x:]

def find_first_digit(input, startFromFunction):
    for i in range(1, len(input) + 1):
        chunk = startFromFunction(input, i)
        for word, digit in word_to_digit.items():
            if word in chunk:
                return digit

def find_calibration_value_with_words(line):
    return int(find_first_digit(line, FIND_FROM_BEGINNING) + find_first_digit(line, FIND_FROM_END))
               
def test_filter_numbers():
    assert filter_digits('1abc2') == '12', f"Expected '12', but got {filter_digits('1abc2')}"
    assert filter_digits('pqr3stu8vwx') == '38', f"Expected '38', but got {filter_digits('pqr3stu8vwx')}"
    assert filter_digits('a1b2c3d4e5f') == '12345', f"Expected '1235', but got {filter_digits('a1b2c3d4e5f')}"
    assert filter_digits('treb7uchet') == '7', f"Expected '77', but got {filter_digits('treb7uchet')}"
    assert filter_digits('') == '', f"Expected '', but got {filter_digits('')}"

def test_first_last_digit():
    assert first_last_digit('12345') == '15', f"Expected 15, but got {first_last_digit('12345')}"
    assert first_last_digit('67890') == '60', f"Expected 60, but got {first_last_digit('67890')}"
    assert first_last_digit('9876543210') == '90', f"Expected 90, but got {first_last_digit('9876543210')}"
    assert first_last_digit('5') == '55', f"Expected 55, but got {first_last_digit('5')}"
    assert first_last_digit('0') == '00', f"Expected 00, but got {first_last_digit('0')}"

def test_find_first_digit():
    assert find_first_digit('two1nine', FIND_FROM_BEGINNING) == '2'
    assert find_first_digit('eightwothree', FIND_FROM_BEGINNING) == '8'
    assert find_first_digit('abcone2threexyz', FIND_FROM_BEGINNING) == '1'
    assert find_first_digit('xtwone3four', FIND_FROM_BEGINNING) == '2'
    assert find_first_digit('4nineeightseven2', FIND_FROM_BEGINNING) == '4'
    assert find_first_digit('zoneight234', FIND_FROM_BEGINNING) == '1'
    assert find_first_digit('7pqrstsixteen', FIND_FROM_BEGINNING) == '7'

def test_find_last_digit():
    assert find_first_digit('two1nine', FIND_FROM_END) == '9'
    assert find_first_digit('eightwothree', FIND_FROM_END) == '3'
    assert find_first_digit('abcone2threexyz', FIND_FROM_END) == '3'
    assert find_first_digit('xtwone3four', FIND_FROM_END) == '4'
    assert find_first_digit('4nineeightseven2', FIND_FROM_END) == '2'
    assert find_first_digit('zoneight234', FIND_FROM_END) == '4'
    assert find_first_digit('7pqrstsixteen', FIND_FROM_END) == '6'


if __name__ == "__main__":
    test_filter_numbers()
    test_first_last_digit()
    test_find_first_digit()
    test_find_last_digit()
    with open('input', 'r') as file:
        lines = file.readlines()
        sum_of_calibration_values = sum(map(find_calibration_value_with_words, lines))
        print(sum_of_calibration_values)
