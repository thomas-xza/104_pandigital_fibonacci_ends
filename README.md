
Challenge
---------

Pandigital Fibonacci Ends, #104

https://projecteuler.net/problem=104


Idea 1
------

Minimal Fibonacci numbers will be held in memory whilst iterating upwards through them (i.e. a 
quantity of 3, maximum).

The data structure used to check each set of 9 sequential numbers within one Fibonacci number 
number will be initialised as follows:

    { 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0 }

A key-value store allows for O(1) lookups.

So each Fibonacci number, F_n, will involve a maximum of 2 lookups.

It is then simply a matter of taking a set of 9 numbers, and as soon as any quantity within the 
key-value store is equal to 2, moving onto the F_n set and resetting the key-value store.


Implementation
--------------

Idea 1 will be implemented in Python, and converted to Go if too slow. Tests written along the 
way to ensure Go port works as expected, if needed.

    gen_next_fibonacci(prev_fns: tuple[int]) -> tuple[int]

    convert_f_n_to_sets(fib: int) -> tuple[tuple[int]]

    check_f_n(fib_set: tuple[tuple[int]]) -> Bool

    check_set(set: tuple[int]) -> Bool


Tests
-----

`gen_next_fibonacci()`

- hardcoded expected fibonacci values, based on initial easily-verified sequence

`convert_f_n_to_set()`

- any number (including non-fibonacci) of length 9+ checks functionality
- number of length below 9 doesn't need to throw exception

`check_f_n()`

- f_n set length too small
- f_n set length correct, 0 sets are pandigital
- f_n set length correct, 1 set is pandigital
- f_n set length correct, 2 sets are pandigital


`check_set()`

- set of expected length for which true is expected
- set of expected length for which false is expected


Progress
--------

After 1 bugfix related to a type error, when both fib_funcs.py and
fib_funcs.go are initialised at the same time, output of both
implementations is identical - see `res_compare.sh`.

However, though faster, the Go implementation is too slow for the
intended purpose! A multi-core implementation would allow an n speed,
where n is the quantity of cores.

It seems unlikely there would be a pattern among the k sequence, as
the Fibonacci numbers do not appear to follow any obvious number base
(e.g. base 2, base 10).

The most computationally intensive part would seemingly be the adding
of the previous 2 Fibonacci numbers.


Solution
--------

The Go implementation is able to derive the solution within a
reasonable amount of time.