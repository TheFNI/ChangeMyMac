#!/usr/bin/python3

import subprocess
import os
import sys


def cek_sudo():
    if os.geteuid() != 0:
        print("Requirement: Sudo!")
        sys.exit(1)


def variabel():
    interface = input("your interface > ")
    mac = "1a:2b:3c:4d:5e:6f"
    return interface, mac


def ubah(interface, mac):
    cek_sudo()

    subprocess.run(["sudo", "ifconfig", interface, "down"], check=True)
    subprocess.run(["sudo", "ifconfig", interface, "hw", "ether", mac], check=True)
    subprocess.run(["sudo", "ifconfig", interface, "up"], check=True)
    print("Finish!")

    return interface, mac


opsi, opsi1 = variabel()
ubah(opsi, opsi1)
