#! /bin/python3
#-------------------
# This tool will make all of our scripts for tool selection
#-------------------
import os
#---------------------------------
#functions
#---------------------------------
def script():
    print("Here we build the script")
    # // Here we need to figure out how to build the script
    # // So we got the script with the tools
    # // So the first line will be to do a "cat" on the file
    # // Lets make the script
    # So here we are going to input our code
    #os.system("/home/florens/Scripts/.Pentest/scanner/bfile.txt")
    os.system("cp wc.txt .count.txt")
    os.system("rm -rf wc.txt")
    # We got the tools now 
    # We will use some sample code to see how the output is
    script_f = '''#! /bin/python3
import os
import sys
#------------------------------------------------------
# This tool is for the Fuzzer category of the BlackArch Repo
# We use the Web tool check for programs and checking if the directory exists
#-------------------------------------------------
dir_f = "/home/florens/Scripts/.Pentest/{}/bfile.txt" # This needs to be changed
print(50 * "")
os.command("cat" + " " + dir_f)print(50 * "-")
sel = input("Enter the tool you want to access:" + " ")
print(50 * "-")
filename = '/home/florens/Scripts/.Pentest/{}/bfiles.txt'
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
    in_f = "/home/florens/Scripts/.Pentest/{}/bfile.txt"
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
                f_d = "/home/florens/Scripts/.Pentest/{}/./run.sh"
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
        in_x = "/home/florens/Scripts/.Pentest/{}}/afile.txt"
        dir_x = "/usr/bin/" + sel
        with open(in_x) as f:
            if dir_x in f.read():
                sel2_x = dir_c
                final_c = "gnome-terminal -e" + " " + sel2_x
                print(final_c)
                bscp = ("")
                with open ('run.sh', 'w') as rsh:
                    rsh.write(bscp)
                os.system("chmod +x run.sh")
                f_dx = "/home/florens/Scripts/.Pentest/{}}/./run.sh"
                os.system("gnome-terminal --window -- bash -c" + " " + f_dx)
                #os.system("/home/florens/Scripts/.Pentest/{}}/./run.sh")
                os.system("rm -rf afile.txt")
                os.system("rm -rf ts.txt")
                os.system("rm -rf run.sh")
                # This section is done!
                os.system("clear")
                exit()'''
    with open ('test.py', 'w') as rsh:
        rsh.write(script_f)
    print("Done!")
    print(50 * "-")
    input("Press any key to continue:")          
    print(50 * "")
    os.system("clear")
    print(50 * "-")

    print("WARNING!")
    print(50 * "-")
    print(''' 
    So now we are going to configure the tool, for that we will do the following
    1: ''')
    input("Press any key to continue:")
    pwd_f = "/home/florens/Scripts/.Pentest/./test.py"
    bscpx = ('''\
            #! /bin/bash
            nano''' + " " + pwd_f + '''
            exec bash''')
    with open ('run.sh', 'w') as rsh1:
        rsh1.write(bscpx)
    os.system("chmod +x test.py")
    os.system("chmod +x run.sh")
    pwd_d =  "/home/florens/Scripts/.Pentest/./run.sh" 
    os.system("gnome-terminal --window -- bash -c" + " " + pwd_d)
    input("Press any key to continues")





def startup():
    print(50 * "-")
    print("Welcome to Cmake!")
    print(50 * "-")
    print(''' WARNING!
    REMEMBER TO DISABLE LINE 62 ON
    Web-Tools.py FOR THIS TO WORK
    ''')
    print(50 * "-")
    input("Press any key to continue")

def get_vals():
    os.system("clear")
    print(50 * "-")
    print("Categories:")
    print(50 * "-")
    os.system("cat /home/florens/Scripts/.BlackArch/installed.txt")
    print(50 * "-")
    sel = input("Please enter category to install script: " + " ")
    #---------------------------------------------------
    os.system("pacman -Sgg | grep" + " " + sel + " " + "> afile.txt")
    #----------------------------------------------------------.txt")
    sel1 = input("Please enter BlackArch category:" + " ")
    infile = "/home/florens/Scripts/.Pentest/afile.txt"
    outfile = "/home/florens/Scripts/.Pentest/bfile.txt"
    #----------------------------------------------------
    delete_list = ["blackarch-" + sel1]
    with open(infile) as fin, open(outfile, "w+") as fout:
        for line in fin:
            for word in delete_list:
                line = line.replace(word, "")
            fout.write(line)
    os.system("mkdir" + " " + sel1)
    os.system("rm -rf afile.txt")
    pwd = "/home/florens/Scripts/.Pentest/" + sel1
    os.system("mv bfile.txt" + " " + pwd)
    os.system("cat /home/florens/Scripts/.Pentest/" + sel1 + "/bfile.txt | wc -l > wc.txt")
    script()
    #-----------------------------------------------------------



#-------------------
# Execution
#-------------------
startup()
get_vals()

# //TODO TO FINISH