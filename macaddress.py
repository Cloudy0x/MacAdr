#!/usr/local/bin/python3.10

# imports
import sys
import os
import uuid
import subprocess

# color storage
class color:
        ### Regular Colors      
        reset   = "\x1b[0m" # All attributes off(color at startup)

        bold    = "\x1b[1m" # Bold on(enable foreground intensity)
        _bold   = "\x1b[21m" # Bold off(disable foreground intensity)

        underline = "\x1b[4m" # Underline on
        _underline = "\x1b[24m" # Underline off

        blink   = "\x1b[5m" # blink on(enable background intensity)
        _blink  = "\x1b[25m" # blink off(disable background intensity)


        ### foreground colors ###
        black   = "\x1b[30m"
        red     = "\x1b[31m"
        green   = "\x1b[32m" 
        yellow  = "\x1b[33m"
        blue    = "\x1b[34m" 
        magenta = "\x1b[35m"
        cyan    = "\x1b[36m" 
        white   = "\x1b[37m" 

        resetCo = "\x1b[39m " # Default(foreground color at startup)

        light_gray              = "\x1b[90m"
        light_red               = "\x1b[91m" 
        light_green     = "\x1b[92m" 
        light_yellow    = "\x1b[93m" 
        light_blue              = "\x1b[94m" 
        light_megenta   = "\x1b[95m" 
        light_cyan              = "\x1b[96m" 
        light_white     = "\x1b[97m" 



        ### backgrounds colors ###
        black_Bg        = "\x1b[40m"
        red_Bg          = "\x1b[41m"
        green_Bg        = "\x1b[42m" 
        yellow_Bg       = "\x1b[43m"
        blue_Bg         = "\x1b[44m" 
        magenta_Bg      = "\x1b[45m"
        cyan_Bg         = "\x1b[46m" 
        white_Bg        = "\x1b[47m" 

        resetBg = "\x1b[49m " # Default(foreground color at startup)

        light_gray_Bg           = "\x1b[100m"
        light_red_Bg            = "\x1b[101m" 
        light_green_Bg          = "\x1b[102m" 
        light_yellow_Bg         = "\x1b[103m" 
        light_blue_Bg           = "\x1b[104m" 
        light_megenta_Bg        = "\x1b[105m" 
        light_cyan_Bg           = "\x1b[106m" 
        light_white_Bg          = "\x1b[107m" 


# function to get OUI from txt file
def OUI(MacAddr , txt=False):
    if len(MacAddr) != 17:
        print(color.light_red+"\tsomething is wrong !" , color.reset)

        return ""
    MacAddr = MacAddr.replace(":","")

    MacAddr = MacAddr[:6]
    _MacAddr = "" 
    for i in range(len(MacAddr)):
        _MacAddr += MacAddr[i]
        if (i+1) % 2 == 0 and i != 5: 
            _MacAddr += "-"

    path = os.path.dirname(os.path.realpath(__file__))
    res = subprocess.check_output(["grep","-i","-A3",_MacAddr,path+"/oui.txt"],text=txt)
    
    # res = res.split()
    # res = res.pop(0)
    # res = ' '.join(map(res))
    return res
        




print(color.light_green , end="")
print("           _         _   _  \n"
     +"|\/|  /\  /     /\  | \ |_) \n"
     +"|  | /--\ \_   /--\ |_/ | \ \n")

print(color.reset)


# get user mac address
try:
    usr_ma = (hex(uuid.getnode()))
    usr_ma = usr_ma[2:]

    # user mac address
    print("\tyour mac address:" ,color.light_blue, end="")
    for i in range(12):
        if (i) % 2 == 0 and i != 0: 
            print(":" , end="")
        print(usr_ma[i] , end="")
    print(color.reset)
except: 
    print(color.light_red + "\tproblem to find your mac address .-.")


print(color.reset)

print("\tYo! I can find out which OUI is related to the each mac address")
print("\tokay , What is the Mac Address?","example -> 00:01:02:03:04:05 ")
print("\ttype exit to quit")

while True:
    print(color.magenta)
    ma = input("\t >"+color._blink)

    if ma == "exit":
        print("\n\thave nice day ;)")
        break
    ma = OUI(ma,True)

    print(color.cyan)
    print("\t" + ma.replace("\n","\n\t"))


    print(color.reset , "\n")


# By ydnaCieR