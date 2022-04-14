def get_fibonachi_numbers(count: int =10) -> list:
    # if count <= 2, them return default fib = [0, 1]
    fib = [0, 1]
    for _ in range(2, count):
        fib.append(fib[-1] + fib[-2])
    return fib


def main():
    count_of_numbers = int(input('Input need count of numbers fibonachi: '))

    # checking that user input count right
    assert count_of_numbers > 0, "count_of_numbers must be > 0"

    numbers = get_fibonachi_numbers(count=count_of_numbers)
    print(numbers)


if __name__ == "__main__":
    main()

