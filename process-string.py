# Application 1
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "

user_input = input("Please type in a string of word here: ")
letter = user_input.split

output_str = ""

for char in user_input:
    output_str += char * 2

print(output_str)



# Application 2
#  Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes A hyphen will separate the two letters in the string.


alphabet = "abcdefghijklmnopqrstuvwxyz"

user_range = input("Enter a range of letters (e.g., a-z): ")

start, end = user_range.split('-')
start_index = alphabet.index(start)
end_index = alphabet.index(end)

result_str = alphabet[start_index:end_index + 1]

print(result_str)


