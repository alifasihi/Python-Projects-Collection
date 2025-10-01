import itertools
import string
import time


def common_guess(word: str) -> str | None:
    with open('words.text', 'r') as words:
        word_list: list[str] = words.read().splitlines()

        for i, match in enumerate(word_list, start=1):
            if match == word:
                return f'Common match: {match} (#{i})'


def brute_force(word: str, lenght: int, digits: True, symbol: True) -> str | None:
    chars: str = string.ascii_lowercase

    if digits:
        chars += string.digits

    if symbol:
        chars += string.punctuation

    attempts: int = 0
    for guess in itertools.product(chars, repeat=lenght):
        attempts += 1
        guess = ''.join(guess)

        if guess == word:
            return f'{word} was cracked in {attempts} guess'

        # print(guess, attempts) #test


def main():
    print('Searching....')

    password: str = 'pass1'

    start_time: float = time.perf_counter()

    if common_match := common_guess(password):
        print(common_match)

    else:
        if cracked := brute_force(password, lenght=5, digits=True, symbol=True):
            print(cracked)

        else:
            print('there was no match...')

    end_time: float = time.perf_counter()

    print(round(end_time - start_time, 2), 's')


if __name__ == '__main__':
    main()
