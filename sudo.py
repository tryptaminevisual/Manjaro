#! /bin/python3
# Remeber, for this program to work we need to open a root shell
# We need to ask for the package name so we need to get input
# We will build a final command
#print("Hello World") -> This is always a good testing line to make sure about the installation
import os
#----------------------------------

def install():
	os.system("clear")
	print(50 * "-")
	val = input('What package do you want to install?: ' + ' ')
	print(50 * '-')
	command = "pacman -S" + " " + val

#----------------------------------
print("Are you root?")
install()
