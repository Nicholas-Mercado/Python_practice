


nums = [1,2,3,4,5,6,7,8,9,10]

# p = print

# my_list = []
# for n in nums:
#   my_list.append(n)
# p(my_list)

# my_list = [n for n in nums]

# p(my_list)

# my_list = []

# for n in nums:
#   my_list.append(n*n)
# p(my_list)

# my_list = [n*n for n in nums]

# p(my_list)


# my_list = []
# for n in nums:
#   if n%2 == 0:
#     my_list.append(n)
# print(my_list)

# my_list = [n for n in nums if n%2 ==0]

# print(my_list)

# Using a filter + lambda
# my_list = filter(lambda n: n%2 == 0, nums)
# print(list(my_list))

# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
# my_list = []
# for letter in 'abcd':
#   for num in range(4):
#     my_list.append((letter,num))
# for elem in my_list:
#         print (elem)
        
# my_list = [(letter, num) for letter in'abcd' for num in range (4)]
# for elem in my_list:
#         print (elem)
# print (my_list)

# Dictionary Comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# print(list(zip(names, heros)))

my_dict = {}
for name, hero in zip(names, heros):
  my_dict[name] = hero
# print(my_dict)

my_dict = {a: x for a,x  in zip(names,heros) if len(x) >= 5}  
# for elem in my_dict:
#         print (elem)

# my_dict["Bruce"] = 'not Bruce'
# my_dict['Bruce'] = my_dict['test']
    
print(my_dict)

# Set Comprehensions
# nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
# my_set = set()
# for n in nums:
#     my_set.add(n)
# print (my_set)

# my_set = {n for n in nums if n%2 != 0}
# print(my_set)

# my_gen = (n*n for n in nums)

# for i in my_gen:
#   print(i)

# Set Comprehensions


print(len(nums))
