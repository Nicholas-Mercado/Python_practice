


# def square(x):
#   return x * x

# # f = square


# # print(f(5))


# def cube(x):
#   return x * x * x

# def my_map(f, arg):
#   result = []
#   for i in arg:
#     result.append(f(i))
#   return result


# x = [1,2,3,4,5]
# squares = my_map(cube, x)
# squared = my_map(square, x)
# print(squares)
# print(squared)



# print(list(map(lambda x: max(x), x)))


def logger(msg):

  def log_msg():
    print('log:', msg)

  return log_msg

log_hi = logger('Hi!')
log_hi()
