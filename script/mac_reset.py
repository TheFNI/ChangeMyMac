#!/usr/bin/python3

import subprocess
import os
import sys


def cek_sudo():
    if os.geteuid() != 0:
        print("Requirement: Sudo!")
        sys.exit(1)


def rombak():
    try:
        subprocess.run("clear", shell=True)
        cek_sudo()
        interface = input("your interface > ")

        if not subprocess.run(["ifconfig", interface], check=True):
            print("If you see this error, I'm trying to fix it soon!")

        subprocess.run(["ifconfig", interface, "down"], check=True)
        subprocess.run(["macchanger", "-p", interface], check=True)
        subprocess.run(["ifconfig", interface, "up"], check=True)

    except subprocess.CalledProcessError:
        print("Your Mac has already reset :v")


rombak()
