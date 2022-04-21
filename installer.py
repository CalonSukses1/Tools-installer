#GwGakRecodePunyaOrngAnjing
#1/bin/python

import os
import sys
import time

def clear():
    os.system("clear")
    os.system("figlet Ninym")

def menu():
    clear()
    print "\tTools by \33[31;1mRen7\33[0;00m\n"
    print "\tGithub : RenSydicate"
    print "\n1.install nmap"
    print "\n2.instal wafw00f"
    print "\n3.install python"
    print "\n4.install python2"
    print "\n5.install debian" 
    pil = raw_input("\npilih : ")
    if pil =="1":
       os.system("pkg install nmap")
    elif pil =="2":
       os.system("pip install wafw00f")
    elif pil =="3":
       os.system("pkg install python")
    elif pil =="4":
       os.system("pkg install python2")
    elif pil =="5":
       os.system("pkg update && pkg upgrade -y")
       os.system("pkg install proot proot-distro")
       os.system("proot-distro install debian")
       os.system("proot-distro login debian")
    else:
      print "\33unknown input\33[0;00m"

menu()
