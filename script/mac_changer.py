#!/usr/bin/python3

import subprocess
import os
import sys
import time


def cek_sudo():
    if os.geteuid() != 0:
        print("Requirement: Sudo!")
        sys.exit(1)
    return


def scan_interface():
    interface = input("your interface > ")

    if subprocess.run(["ifconfig", interface], check=True):
        subprocess.run("clear", check=True)
        print("Changing your mac....")
        time.sleep(3)
    else:
        print(f"Your {interface} is not detected!")
    return interface


def rombak():
    try:

        subprocess.run("clear", shell=True)
        cek_sudo()
        interface = scan_interface()

        subprocess.run(["ifconfig", interface, "down"], check=True)
        subprocess.run(["ifconfig", interface, "hw", "ether", "1a:2b:3c:4d:5e:6f"], check=True)
        subprocess.run(["ifconfig", interface, "up"], check=True)
        print("Your Mac has changed!")
        time.sleep(1)

    except subprocess.CalledProcessError:
        print("Error: Unable to change MAC address")


rombak()
