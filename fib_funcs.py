#!/usr/bin/env python3

def main():

    found_double_pandigital = False

    fib_seq = (1, 1)
    
    while found_double_pandigital == False:

        fib_seq = gen_next_fibonacci(fib_seq)

        print(fib_seq[1])

        found_double_pandigital = check_f_n(
            convert_f_n_to_sets(fib_seq[1])
            )        


def gen_next_fibonacci(prev_fns: tuple[int]) -> tuple[int]:

    return (prev_fns[1], prev_fns[0] + prev_fns[1])


def convert_f_n_to_sets(fib: int) -> tuple[tuple[int]]:

    fib_chars = list(str(fib))

    fib_xs = [0 for i in range(len(fib_chars))]

    for i, v in enumerate(fib_chars):

        fib_xs[i] = int(v)

    return (fib_xs)[0:9], (fib_xs[-9:])


def check_f_n(fib_sets: tuple[tuple[int]]) -> bool:

    if len(fib_sets) != 2:

        return False

    for fib_set in fib_sets:

        if len(fib_set) != 9 or check_set(fib_set) == False:

            return False

    return True
    

def check_set(fib_set: tuple[int]) -> bool:

    counter = { 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0 }

    print(fib_set)

    for v in fib_set:

        if v == 0:

            return False

        else:

            print(counter, v, counter[v])

            counter[v] = counter[v] + 1

            if counter[v] > 1:

                return False

    return True


if __name__ == '__main__':
    
    main()
