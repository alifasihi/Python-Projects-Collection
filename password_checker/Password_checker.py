def check_password(password: str):
    with open('password.text', 'r') as file:
        common_password: list[str] = file.read().splitlines()
        # print(common_password
        for i, common_password in enumerate(common_password, start=1):
            if common_password == password:
                print(f'{password} : ❌ (#{i})')
                return
        print(f'{password}: ✅ (Unique)')


def main():
    user_pass = input('Enter your password: >>')
    check_password(user_pass)


if __name__ == '__main__':
    main()
