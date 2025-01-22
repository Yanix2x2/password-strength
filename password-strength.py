def is_very_long(password):
    return len(password) > 12


def has_digit(password):
    return any(i.isdigit() for i in password)


def has_upper_letters(password):
    return any(i.isupper() for i in password)


def has_lower_letters(password):
    return any(i.islower() for i in password)


def has_symbols(password):
    return any(not i.isdigit() and not i.isalpha() for i in password)


def get_rating(password):
    score = 0
    list_of_features = [
        is_very_long,
        has_digit,
        has_upper_letters,
        has_lower_letters,
        has_symbols,
    ]
    for i in list_of_features:
        if i(password):
            score += 2
    return score


def main():
    password = input('Введите пароль: ')
    get_rating(password)


if __name__ == '__main__':
    main()
