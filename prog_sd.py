#!/bin/python3
# Remember to turn value in minutes and then seconds
# Deffo have to check this tool and modify it
#-----------------------------------------------------
# In hour case we want to set it to sleep in 90 mins
# Which means 5400 seconds
#-----------------------------------------------------
import os
import time
import sys
#-----------------------------------------------------
print(50 * "-")
print("Remember to run the progam as SUDO!")
print(50 * "-")
x=int(input("seconds: "))
print(50 * "-")
print("The timer has started. Time remaining for shut down: ")
def custom_print(string, how = "normal", dur = 0, inline = True):
    if how == "typing": # if how is equal to typing then run this block of code
        letter = 1
        while letter <= len(string):
            new_string = string[0:letter]
            if inline: sys.stdout.write("\r")
            sys.stdout.write("{0}".format(new_string))
            if inline == False: sys.stdout.write("\n")
            if inline: sys.stdout.flush()
            letter += 1 
            time.sleep(float(dur))
            if new_string=="0": 
                print("\nShut down has started")
                os.system("sudo shutdown")
            else: 
                pass
for k in range(1,x+1):
    k=x-k
    custom_print(str(k), "typing", 1)