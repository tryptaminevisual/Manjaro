#! /bin/python3

import os

print(50 * "-")
print("What do you want to do?")
print(50 * "-")
print("Look into black arch categories (1)")
print(50 * "-")
val = input("Please make your selection: " + " ")
if val == "1":
	print(50 * "-")
	os.system("pacman -Sg | grep blackarch")
	print(50 * "-")
	val2 = input("Please select a category: ")
	print(50 * "-")
	print("Results of your selection:")
	os.system("pacman -Sgg | grep" + " " + val2)
	print(50 * "50")



# //TODO -> Check out this website for completition