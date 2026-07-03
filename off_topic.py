
def main(end: int):

    total = 0

    for i in range(0, end+1):

        print(i)

        if i % 2 != 0:

            total += (i * i)

    print(total)


main(429000)
