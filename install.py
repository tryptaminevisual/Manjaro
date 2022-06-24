#! /bin/python3

import os

def install():
        os.system("clear")
        print(50 * "-")
        val = input('What package do you want to install?: ' + ' ')
        print(50 * '-')
        command = "sudo pacman -S" + " " + val
        os.system(command)
install()
