"""
Challenge: use decorators to trace time taken for function calls

Check out my_program, which relies on 3 different functions.  But
which one takes the most time?

We could add a start_time = time.time() to the beginning of each one,
and a print(time.time() - start_time) at the end, but that would be
very repetitive.  Figure out how to use a decorator to apply this
print pattern to all the functions, without duplicating code.

For bonus points: the little time printout should include the name
of the function

"""

from datetime import datetime
# from functools import wraps

def timeDecorator(fun):
    def trace_time():
        print('calling '+fun.__name__)
        start_time = datetime.now().microsecond
        result = fun()
        print('it takes %d microseconds' % (datetime.now().microsecond - start_time))
        return result
    return trace_time

def repeat(times, until_value):
    def wrap(fun):
        def repeat_fun():
            for i in range(times):
                result = fun()
                if result == until_value:
                    break
        return repeat_fun
    return wrap

# def repeat(fun):
#     @wraps(fun)
#     def repeat_fun(times, until_value):
#         for i in range(times):
#             result = fun()
#             if result == until_value:
#                 break
#     return repeat_fun

def my_program():
    main_screen_turn_on()
    if somebody_set_us_up_the_bomb():
        take_off_every_zig()

@timeDecorator
def main_screen_turn_on():
    print('\n'.join(['*' * 80] * 25))

@repeat(times=5, until_value=True)
def somebody_set_us_up_the_bomb():
    if datetime.now().microsecond % 7 == 0:
        return True
    return False

@timeDecorator
def take_off_every_zig():
    for i in range(1, 10001):
        print('Go {}! '.format(i), end='')

my_program()

"""
For bonus bonus points:

- now make a new decorator that will retry a function up to n times, until
it gets a certain value:

    @repeat(times=5, until_value=True)
    def somebody_set_us_up_the_bomb():
    ...

If you like, please take a look at the functools module in the standard
library; in particular at functools.wraps function, which is a very useful
decorator to help you building your own decorators.
"""

