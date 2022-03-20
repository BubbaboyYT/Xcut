import os
from time import sleep as wait
#import libarys if required
opener = "xcut V1.0.0 \n"
cmd = True
namecustompr = "FALSE"
namecustomcmd = "FALSE"
poppername = "FALSE"
while cmd == True:
    command = input(opener)
    if command == "xcut stop":
        cmd = False
    if command == "xcut get":
        print("Hit")
    if command == "term clear":
        os.system('CLS')
    if command == "files":
        os.system('dir')
    if command == "CUTO":
        module = input("Module :")
        if module == "xcut_propt":
            xcutpropte = True
            while xcutpropte == True: 
                print("xcut Propt Terminal\n")
                xcut_propt_cmd = input("Command :")
                if xcut_propt_cmd == "Opener Change":
                    arg1 = input("arg 1 :")
                    os.system('cls')
                    opener = arg1
                    xcutpropte = False
                if xcut_propt_cmd == "Custom Change printer":
                    namecustompr = input("Name :")
                    toprint = input("Response :")
                if xcut_propt_cmd == namecustompr:
                    print(toprint)
                if xcut_propt_cmd == "Custom Change command":
                    namecustomcmd = input("Name :")
                    toexu = input("CMD Command :")
                if xcut_propt_cmd == namecustomcmd:
                    os.system(toexu)
                if xcut_propt_cmd == "end":
                    xcutpropte = False
                if xcut_propt_cmd == "help":
                    print("end : ends this terminal \n Opener Change : Changes the opener \n Custom Change printer/command : printer commands print things while command commands can run any command off the system terminal")
        if module == "popper":
            poppere = True #Defines if the terminal for this module is enabled
            while poppere == True:
                popper_cmd = input("Popper V1.0.0 \n Used as a sample module for people to add there own module \n Use 'Xcut Propt' to change opener and add custom commands \n Welcome " + poppername + " Please type your command! :") #the input for commands
                if popper_cmd == "end":
                    poppere = False #ends the module and returns to main Xcut terminal
                if popper_cmd == "HW":
                    print("Hello World!") #prints Hello World!
                if popper_cmd == "ARG":
                    poppername = input("Name :") #Argument tester
                if popper_cmd == "help":
                    print("HW : prints hello world \n ARG : changes the welcome name") #\n is a new line BTW
    if command == "help":
        print("CUTO : opens any module installed \n files : list files in the dir \n xcut stop : ends the terminal \n xcut get : Prints HIT \n term clear : clears the terminal")
