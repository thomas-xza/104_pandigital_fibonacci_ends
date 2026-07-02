#!/usr/bin/env python3

def gen_next_fibonacci(prev_fns: tuple[int]) -> tuple[int]:

    return (prev_fns[1], prev_fns[0] + prev_fns[1])
    
def convert_f_n_to_sets(fib: int) -> tuple[tuple[int]]:

    fib_chars = list(str(fib))

    return (fib_chars)[0:9], (fib_chars[-9:])

# check_f_n(fib_set: tuple[tuple[int]]) -> Bool

# check_set(set: tuple[int]) -> Bool

