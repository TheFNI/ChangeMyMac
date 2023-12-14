#!/usr/bin/python3

import subprocess
import os
import sys


def cek_sudo():
    if os.geteuid() != 0:
        print("Requirement: Sudo!")
        sys.exit(1) 
    return


def run():
    cek_sudo()
    lolcat_path = "/usr/games/lolcat"
    subprocess.run(f"figlet TheFNI | {lolcat_path} -a", shell=True, check=True)

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
