import os
from time import sleep as wait
opener = "xcut V1.0.0 \n"
cmd = True
namecustompr = "FALSE"
namecustomcmd = "FALSE"
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