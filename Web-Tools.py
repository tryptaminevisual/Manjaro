#! /bin/python3
#----------------------------------------------------------
# Here we will reserach the location of where
# the tool is located, and where to execute
# So first we will pull the List of tools installed on web
# The we will make a checkup to see if said tools exist
# [We need the location for that]
#----------------------------------------------------------
# Requirements
import os
#----------------------------------------------------------
#----------------------------------------------------------
# Functions
def cleanup():
    os.system("clear")
    os.system("rm -rf /home/florens/Scripts/WebCheck/")

def custom_s():
    print(50 * "-")
    print("What tool do you want to check for?")
    print(50 * "-")
    c_s = input("Please enter the tool name: " + " ")
    command_s = "whereis" + " " + c_s
    command_f = command_s
    print(command_f)

def check():
    print(50 * "-")
    print("Lets make some checks")
    print(50 * "-")
    input("Press any key to start: " + " ")
    print(50 * "-")
    #---------------------------------------------------
    infile = "/home/florens/Scripts/WebCheck/webapp.txt"
    outfile = "/home/florens/Scripts/WebCheck/cfile.txt"
    #----------------------------------------------------
    delete_list = ["blackarch-webapp"]
    with open(infile) as fin, open(outfile, "w+") as fout:
        for line in fin:
            for word in delete_list:
                line = line.replace(word, "")
            fout.write(line)
    #-------------------------------------------------------
    file_f = open("/home/florens/Scripts/WebCheck/cfile.txt")
    Lines = file_f.readlines()
    #--------------------------------------------------------
    count = 0
    #--------------------------------------------------------
    for line in Lines:
        count += 1
        print("Line{}: {}".format(count, line.strip()))
    print(50 * "-")
    print("The above result is the name of the programs for the web category.")
    print(50 * "-")
    input("Press any key to start location check:")
    print(50 * "-")
    os.system("/home/florens/Scripts/.Check/./checkt.sh")
    print(50 * "-")
    print("Checks done!")
    print(50 * "-")
    input("Press any key to exit:")
    #cleanup()
    exit()
    

def main_menu():
    print(50 * "-")
    print("Welcome to the main menu!")
    print(50 * "-")
    print("Do a whole tool check (1)")
    print("Search for a tool (2)")
    print("Check Installed Categories (3)")
    print("Exit (4)")
    print(50 * "-")
    opt = input("Please select an option: " + " ")
    if opt == "1":
        os.system("clear")
        check()
    elif opt == "2":
        os.system("clear")
        custom_s()
    elif opt == "4":
        exit()
    elif opt == "3":
        print(50 * "-")
        print("The Following Categories are installed:")
        print(50 * "-")
        os.system("cat /home/florens/Scripts/.BlackArch/installed.txt")
        print(50 * "-")
        input("Press any key to continue:")
def start_1():
    print(50 * "-")
    print("Lets see what Web Tools are available...")
    print(50 * "-")
    sel_1 = input("Please enter a category: " + " ")
    print("Working...")
    print(50 * "-")
    os.system("pacman -Sgg | grep" + " " + sel_1 + " " + "> webapp.txt") # blackarch-webapp
    input("Done! Press any key to continue:")
    print(50 * "-")
    os.system("cat webapp.txt")
    os.system("mkdir WebCheck")
    os.system("mv webapp.txt WebCheck/")
    print(50 * "-")
    input("Lets go the the main menu...")
    os.system("clear")
def start():
    print(50 * "-")
    print("Welcome to the Web Searcher")
    print(50 * "-")
    input("Press any key to continue:")
    os.system("clear")
#----------------------------------------------------------
# Executing functions
start()
start_1()
main_menu()
#----------------------------------------------------------
# Notes
#-----------------------------------------------------------
# So for the check we need first to get the commands
# We will use the command 'whereis' and where if it spits
# A location then We will give a Tick, it not an X
# We will need a menu, 3 options, check, search, and exit
# We will start with the menu:
# We added a section to check what packages are installed
# This has to be done Manually on the folder .BlackArch