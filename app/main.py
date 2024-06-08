import sys


def main() -> None:
    while True:
        sys.stdout.write('$ ')
        sys.stdout.flush()

        user_input: str = input()
        command: str = user_input.split(' ')[0]

        match command:
            case 'exit':
                exit()
            
            case 'echo':
                content: str = user_input.split(' ', 1)[1]
                sys.stdout.write(content)

            case _:
                sys.stdout.write(f"{command}: command not found")
    
        sys.stdout.write('\n')
        sys.stdout.flush()


if __name__ == "__main__":
    main()