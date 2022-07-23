size = 5

def get_numbers(num):
    numbers = []
    user_input = input('Enter {} integers:\n'.format(num))

    i = 0
    for token in user_input.split():
        number = int(token)     # Convert string input into integer
        numbers.append(number)  # Add to numbers list

        print(i, number)
        i += 1

    return numbers

def print_all_numbers(numbers):
    print('Numbers: ', end = '')
    for number in numbers:
        print(number, end = ' ')
    print('')

def print_odd_numbers(numbers):
    print('Odd numbers: ', end = '')
    for number in numbers:
        if number % 2 > 0:
            print(number, end = ' ')
        else:
            continue
    print('')

def print_negative_numbers(numbers):
    print('Negative Numbers: ', end = '')
    for number in numbers:
        if number < 0:
            print(number, end = ' ')
        else:
            continue
    print('')


nums = get_numbers(size)
print_all_numbers(nums)
print_odd_numbers(nums)
print_negative_numbers(nums)