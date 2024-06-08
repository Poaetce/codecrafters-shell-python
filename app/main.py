import sys


def main() -> None:
    sys.stdout.write('$ ')
    sys.stdout.flush()

    user_input: str = input()
    command: str = user_input.split(' ')[0]

    match command:
        case _:
            sys.stdout.write(f"{command}: command not found")
    
    sys.stdout.write('\n')
    sys.stdout.flush()


if __name__ == "__main__":
    main()
