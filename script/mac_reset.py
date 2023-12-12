#!/usr/bin/python3

import subprocess
import os
import sys
import time


def cek_sudo():
    if os.geteuid() != 0:
        print("Requirement: Sudo!")
        sys.exit(1)


def running():
    try:
        subprocess.run("clear", shell=True)
        cek_sudo()
        interface = input("your interface > ")
        
        # Ignore this, I'm going to fix soon :v
        if not subprocess.run(["ifconfig", interface], check=True):
            print("Something went wrong!")

        subprocess.run(["ifconfig", interface, "down"], check=True)
        subprocess.run(["macchanger", "-p", interface], check=True)
        subprocess.run(["ifconfig", interface, "up"], check=True)

    except subprocess.CalledProcessError:
        print("Your Mac is just like that, lol :v")


running()
