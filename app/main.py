from typing import Callable

import sys
import os

paths: list[str] = (os.getenv("PATH") or '').split(":")


def exit_command(*_: str) -> None:
    exit()


def echo_command(*arguments: str) -> None:
    content: str = ' '.join(arguments)
    sys.stdout.write(content)


def type_command(*arguments: str) -> None:
    command: str = arguments[0]

    if command in builtin_commands:
        sys.stdout.write(f"{command} is a shell builtin")

    else:
        for path in paths:
            file_path: str = os.path.join(path, command)
            if os.path.exists(file_path):
                sys.stdout.write(f"{command} is {file_path}")
        else:
            sys.stdout.write(f"{command} not found")


builtin_commands: dict[str, Callable] = {
    'exit': exit_command,
    'echo': echo_command,
    'type': type_command,
}


def main() -> None:
    while True:
        sys.stdout.write('$ ')
        sys.stdout.flush()

        user_input: list[str] = input().split(' ')
        command: str = user_input[0]
        arguments: list[str] = user_input[1:]

        if command in builtin_commands:
            builtin_commands[command](*arguments)
        else:
            sys.stdout.write(f"{command}: command not found")
    
        sys.stdout.write('\n')
        sys.stdout.flush()


if __name__ == "__main__":
    main()