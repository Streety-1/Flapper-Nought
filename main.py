#------------------------------------IMPORTS------------------------------------#
import os
import subprocess
import sys
import urllib.request
import time
import requests
from simple_term_menu import TerminalMenu

#------------------------------------VALUES------------------------------------#
clear = lambda: os.system('cls')

ScriptVersion = 'V1.0.1'

urltocheckwifi = "https://www.google.com/"

requiredmodules = {'requests', 'simple-term-menu'}

#-------------------Functions-------------------#
def pipinstall(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package], stdout=subprocess.DEVNULL)

def systemCmd(command):
    os.system(command)

def runPython(name):
    clear()
    exec(open(name).read())


#------------------------------------INSTALLED IMPORTS------------------------------------#



#------------------------------------START------------------------------------#

def Wifi():
    print("Running...")
    time.sleep(3)
    runPython('ap-scanner.py')

def CheckForUpdate():
    print("Running...")
    time.sleep(3)
    runPython('updater.py')

def MainMenu():
    clear()
    print("| Flapper Nought |")
    print(ScriptVersion)

    options = ["AP Scanner", "Update"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()

    if options[menu_entry_index] == "AP Scanner":
        print("AP")
    if options[menu_entry_index] == "Update":
        print("Update")

    print(f"You have selected {options[menu_entry_index]}!")

MainMenu()
