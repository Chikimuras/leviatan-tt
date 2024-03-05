def sum_of_even_numbers(numbers):
    total_sum = 0
    for number in numbers:
        if number % 2 == 0:
            total_sum += number
    return total_sum


def get_user_input():
    print("Saisissez une liste de nombres entiers et positifs séparés par des virgules")
    user_input = input()
    user_input = user_input.split(",")
    user_input = [int(number) for number in user_input]
    return user_input


def main():
    print(sum_of_even_numbers(get_user_input()))


if __name__ == "__main__":
    main()
