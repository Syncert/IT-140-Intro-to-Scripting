#format name input to last, first initial . middle initial . (could use additional formatting and element to verify input)

name_input = input().split()
list_length = len(name_input)
if list_length == 3 :
    last_name = name_input[-1].capitalize()
    first_initial = name_input[0][0:1].capitalize()
    middle_initial = name_input[1][0:1].capitalize()
    print('{}, {}.{}.'.format(last_name,first_initial,middle_initial))

if list_length == 2 :
    last_name = name_input[-1].capitalize()
    first_initial = name_input[0][0:1].capitalize()
    print('{}, {}.'.format(last_name,first_initial))