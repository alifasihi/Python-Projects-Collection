import string
import secrets


def contains_upper(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True

    return False


def contains_symbols(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True

    return False


def generate_password(lenght: int, symbols: bool, uppercase: bool) -> str:
    combination: str = string.ascii_lowercase + string.digits

    if symbols:
        combination += string.punctuation

    if uppercase:
        combination += string.ascii_uppercase

    combination_lenght: int = len(combination)
    new_password: str = ''

    for _ in range(lenght):
        new_password += combination[secrets.randbelow(combination_lenght)]

    return new_password


if __name__ == '__main__':
    for i in range(1, 6):
        new_pass = generate_password(lenght=10, symbols=True, uppercase=True)
        print(f'pass number {i} is : {new_pass}')
