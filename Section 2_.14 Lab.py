# FIXME (1): Finish reading another word and an integer into variables. 
# Output all the values on a single line
favorite_color = input('Enter favorite color:\n').lower().strip()
favorite_animal = input('Enter your favorite animal:\n').lower().strip()
user_number = input('Enter a number between 1-100:\n').lower().strip()
print('You entered: {} {} {}'.format(favorite_color, favorite_animal, user_number))

# FIXME (2): Output two password options
password1 = '{}_{}'.format(favorite_color,favorite_animal)
password2 = '{0}{1}{0}'.format(user_number,favorite_color)
print('\nFirst password:', password1)
print('Second password:', password2)


# FIXME (3): Output the length of the two password options
print('\nNumber of characters in {}:'.format(password1),len(password1))
print('Number of characters in {}:'.format(password2),len(password2))