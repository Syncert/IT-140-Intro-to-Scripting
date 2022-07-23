#Word Games
#input integer float character & string

input_integer = int(input('Enter integer (32 - 126):\n'))
input_float = input('Enter float:\n')
input_character = input('Enter character:\n')
input_string = input('Enter string:\n')

print(input_integer, input_float, input_character, input_string)
# FIXME (2): Output the four values in reverse
print(input_string, input_character, input_float, input_integer)
# FIXME (3): Convert the integer to a characer, and output that character
print(input_integer, 'converted to a character is', chr(input_integer))