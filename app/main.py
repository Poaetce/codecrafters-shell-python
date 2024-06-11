from typing import Callable, Optional

import sys
import os
import subprocess


def get_file(command: str) -> Optional[str]:
    paths: list[str] = (os.getenv("PATH") or '').split(":")
    
    for path in paths:
        file_path: str = os.path.join(path, command)
        if os.path.exists(file_path):
            return file_path
    
    return None


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
        file_path: Optional[str] = get_file(command)
        if file_path:
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
            sys.stdout.write('\n')

        elif get_file(command):
            subprocess.run([command, *arguments])

        else:
            sys.stdout.write(f"{command}: command not found")
            sys.stdout.write('\n')
    
        sys.stdout.flush()


if __name__ == "__main__":
    main()