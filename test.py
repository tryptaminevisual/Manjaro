#! /bin/python3
import os
import sys
#------------------------------------------------------
# This tool is for the Fuzzer category of the BlackArch Repo
# We use the Web tool check for programs and checking if the directory exists
#-------------------------------------------------
dir_f = "/home/florens/Scripts/.Pentest/scanner/bfile.txt" # This needs to be changed
print(50 * "")
os.command("cat" + " " + dir_f)print(50 * "-")
sel = input("Enter the tool you want to access:" + " ")
print(50 * "-")
filename = '/home/florens/Scripts/.Pentest/Fuzzer/.tools.txt'
with open(filename) as f_obj:
    tools_s = f_obj.read()
if sel in tools_s:
    print(50 * "-")
    print("Opening tool...")
    print(50 * "-")
    os.system("whereis" + " " + sel + " " + "> ts.txt")
    print(50 * "")
    print("WHat do you want to do?")
    print(50 * "-")
    print("Go to directory (1)")
    print("Run executable (2)")
    print(50 * "-")
    sel2 = input("Select an option: " + " ")
    in_f = "/home/florens/Scripts/.Pentest/Fuzzer/afile.txt"
    dir_c = "/usr/share/" + sel
    if sel2 == "1":
        with open(in_f) as f:
            if dir_c in f.read():
                sel2_c = "cd" + " " + dir_c
                final_c = "gnome-terminal -e" + " " + sel2_c
                print(final_c)
                # Here we will open a new shell with the tool
                # Ok we might need to create a script and then call it
                # So lets create a .sh script and then delete the files
                bscp = ("")
                with open ('run.sh', 'w') as rsh:
                    rsh.write(bscp)
                os.system("chmod +x run.sh")
                f_d = "/home/florens/Scripts/.Pentest/Fuzzer/./run.sh"
                os.system("gnome-terminal --window -- bash -c" + " " + f_d)
                #os.system("/home/florens/Scripts/.Pentest/Web/./run.sh")
                os.system("rm -rf afile.txt")
                os.system("rm -rf ts.txt")
                os.system("rm -rf run.sh")
                # This section is done!
                os.system("clear")
                exit()
    elif sel2 == "2":
        print(50 * "-")
        print("Lets run your command...")
        print(50 * "-")
        s_t = input("Press any key to continue...")
        in_x = "/home/florens/Scripts/.Pentest/Fuzzer/afile.txt"
        dir_x = "/usr/bin/" + sel
        with open(in_x) as f:
            if dir_x in f.read():
                sel2_x = dir_c
                final_c = "gnome-terminal -e" + " " + sel2_x
                print(final_c)
                bscp = (""))
                with open ('run.sh', 'w') as rsh:
                    rsh.write(bscp)
                os.system("chmod +x run.sh")
                f_dx = "/home/florens/Scripts/.Pentest/Fuzzer/./run.sh"
                os.system("gnome-terminal --window -- bash -c" + " " + f_dx)
                #os.system("/home/florens/Scripts/.Pentest/Web/./run.sh")
                os.system("rm -rf afile.txt")
                os.system("rm -rf ts.txt")
                os.system("rm -rf run.sh")
                # This section is done!
                os.system("clear")
                exit()