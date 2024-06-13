from typing import Callable, Optional

import sys
import os
import subprocess


def exit_command(*_: str) -> None:
    exit()


def echo_command(*arguments: str) -> None:
    content: str = ' '.join(arguments)
    sys.stdout.write(content)
    sys.stdout.write('\n')


def type_command(*arguments: str) -> None:
    command: str = arguments[0]

    if command in builtin_commands:
        sys.stdout.write(f"{command} is a shell builtin")

    else:
        file_path: Optional[str] = get_file(command)
        if file_path:
            sys.stdout.write(f"{command} is {file_path}")
        else:
            sys.stdout.write(f"{command}: not found")
    sys.stdout.write('\n')


def pwd_command(*_: str) -> None:
    sys.stdout.write(os.getcwd())
    sys.stdout.write('\n')


def cd_command(*arguments: str) -> None:
    directory: str = arguments[0]
    try:
        os.chdir(os.path.expanduser(directory))
    except:
        sys.stdout.write(f"cd: {directory}: No such file or directory")
        sys.stdout.write('\n')


builtin_commands: dict[str, Callable] = {
    'exit': exit_command,
    'echo': echo_command,
    'type': type_command,
    'pwd': pwd_command,
    'cd': cd_command,
}


def get_file(command: str) -> Optional[str]:
    paths: list[str] = (os.getenv("PATH") or '').split(":")
    
    for path in paths:
        file_path: str = os.path.join(path, command)
        if os.path.exists(file_path):
            return file_path
    
    return None


def main() -> None:
    while True:
        sys.stdout.write('$ ')
        sys.stdout.flush()

        user_input: list[str] = input().split(' ')
        command: str = user_input[0]
        arguments: list[str] = user_input[1:]

        if command in builtin_commands:
            builtin_commands[command](*arguments)

        elif get_file(command):
            subprocess.run([command, *arguments])

        else:
            sys.stdout.write(f"{command}: command not found")
            sys.stdout.write('\n')
    
        sys.stdout.flush()


if __name__ == "__main__":
    main()