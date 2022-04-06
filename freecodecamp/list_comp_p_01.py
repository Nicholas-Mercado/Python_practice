# h_letters = []

# for letter in 'human':
#     h_letters.append(letter)

# print(h_letters)

# letters = [letter for letter in 'human' if letter != 'n']

# print(letters)

num_list = [y for y in range(1,51) if y%2 ==0 if y%5 == 0 ]

# print(num_list)

nums = [i for i in range(1,1001) if i%8 == 0]
nums = [i for i in range(1,1001) if '6' in str(i) ]


string = "Practice Problems to Drill List Comprehension in Your Head."
count = 0
string_count = len([x for x in string if x == ' '])
# print(string_count)

no_vowels = ''.join([x for x in string if x not in ['a','e','i','o','u']])

words = string.split(' ')
less_then = [char for char in words if len(char) < 5]
print(less_then)



