def outer_func(msg):

    message = msg

    def inner_func():
        print(message)

    return inner_func

hello_func = outer_func('hi')
hi_func = outer_func('hello')

hi_func()
hello_func()
