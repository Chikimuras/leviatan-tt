def check_divisibility(number):
    """
    Check the divisibility of a number by 3, 5, or both, and return a corresponding string.
    """
    if number % 3 == 0 and number % 5 == 0:
        return "LeviaTan"
    elif number % 3 == 0:
        return "Levia"
    elif number % 5 == 0:
        return "Tan"
    else:
        return str(number)


def main():
    """
    Print numbers from 1 to 101 and call check_divisibility function for each number.
    """
    for i in range(1, 102):
        print(check_divisibility(i))


if __name__ == "__main__":
    main()
