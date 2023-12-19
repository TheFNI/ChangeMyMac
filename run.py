#!/usr/bin/python3

import subprocess
import os
import sys


def cek_sudo():
    if os.geteuid() != 0:
        print("Requirement: Sudo!")
        sys.exit(1) 
    return


def name():
    print('''
  ____ _                            __  __       __  __            
 / ___| |__   __ _ _ __   __ _  ___|  \/  |_   _|  \/  | __ _  ___ 
| |   | '_ \ / _` | '_ \ / _` |/ _ \ |\/| | | | | |\/| |/ _` |/ __|
| |___| | | | (_| | | | | (_| |  __/ |  | | |_| | |  | | (_| | (__ 
 \____|_| |_|\__,_|_| |_|\__, |\___|_|  |_|\__, |_|  |_|\__,_|\___|
                         |___/             |___/                   
''')
    


def run():
    cek_sudo()
    lolcat_path = "/usr/games/lolcat"
    name()
    print("[1] Changing Mac")
    print("[2] Resetting Mac")
    print("\n[?] Which one do you want to choose? ", end="")
    pilihan()
    return


def pilihan():
    choose = input()

    if choose == "1":
        subprocess.run("sudo python3 script/mac_changer.py", shell=True, check=True)
    elif choose == "2":
        subprocess.run("sudo python3 script/mac_reset.py", shell=True, check=True)
    else:
        print("Exit!")


run()
