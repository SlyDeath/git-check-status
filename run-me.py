#!/bin/env python3

import os
import subprocess
from pathlib import Path

user_home = Path('~').expanduser().__str__()
repos_path = 'Work' # Установить свою папку


class Style:
    CYAN = '\033[96m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'


for root, dirs, files in os.walk(os.path.abspath(user_home + '/' + repos_path)):
    path = root.split(os.sep)
    dir_name = os.path.basename(root)

    if dir_name == '.git' and root.find('vendor') == -1:
        project_path = os.path.dirname(root)
        command = 'cd ' + project_path + '&& git status -s'

        if subprocess.check_output(command, shell=True):
            print(' ')
            project_name = Style.YELLOW + os.path.basename(os.path.normpath(project_path))
            print(
                Style.BLUE +
                '☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢'
                + Style.END
            )
            print(Style.RED + Style.BOLD + 'Есть изменения в проекте ' + Style.CYAN + '❯❯❯ ' + project_name + Style.END)
            print(Style.GREEN + ' ⤵ ⤵ ⤵' + Style.END)
            print(project_path)
            print(Style.GREEN + ' ⤵ ⤵ ⤵' + Style.END)
            os.system(command)
            print(
                Style.BLUE +
                '☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢ ☢'
                + Style.END
            )
