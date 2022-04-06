# import re

# pattern = r"pam"

# match = re.search(pattern, "eggspamsausage")
# if match:
#   print(match.group())
#   print(match.start())
#   print(match.end())
#   print(match.span())


def concatenate(*args):
    result = []

    for x in args:
        result = '-'.join(args)
        print(x)
    return result


print(concatenate("I", "love", "Python", "!"))
