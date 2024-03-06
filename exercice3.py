def invert_word(word):
    inverted_word = ""

    for i in range(len(word) - 1, -1, -1):
        inverted_word += word[i]

    return inverted_word


def get_valid_user_input():
    print("Saisissez un mot")
    # check if the input is a string
    user_input = input()
    if not isinstance(user_input, str):
        raise ValueError("Le mot doit être une chaîne de caractères")
    # check if the input is not empty
    if not user_input:
        print("Le mot ne peut pas être vide")
        return get_valid_user_input()

    return user_input


def main():
    print(invert_word(get_valid_user_input()))


if __name__ == "__main__":
    main()
