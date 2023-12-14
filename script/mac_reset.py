#!/usr/bin/python3

import subprocess
import os
import sys
import time


def cek_sudo():
    if os.geteuid() != 0:
        print("Requirement: Sudo!")
        sys.exit(1)


def scan_interface():
    interface = input("your interface > ")

    if subprocess.run(["ifconfig", interface], check=True):
        subprocess.run("clear", check=True)
        print("Resetting your mac....")
        time.sleep(3)
    else:
        print(f"your {interface} is not detected!")

    return interface


def rombak():
    try:
        subprocess.run("clear", shell=True)
        cek_sudo()
        interface = scan_interface()

        subprocess.run(["ifconfig", interface, "down"], check=True)
        subprocess.run(["macchanger", "-p", interface], check=True)
        subprocess.run(["ifconfig", interface, "up"], check=True)
        print("Your mac has been reset!")

    except subprocess.CalledProcessError:
        print("Your Mac has already reset :v")


rombak()
