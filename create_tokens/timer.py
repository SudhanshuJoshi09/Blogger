# Timer for recording time taken by a function.
from time import perf_counter


# Decorater
def timing_func(func, *args):
    '''
    Calculates time taken by func.
    '''

    def inner(*args):
        '''
        Closure for decorater
        '''
        start = perf_counter()
        return_val = func(*args)
        end = perf_counter()

        print(f'Time Taken :: {end - start}')
        return return_val

    return inner

