# tkinter is used for the file prompt
import tkinter as tk
from tkinter import filedialog

# Beautifull soup is used for reading XML
from bs4 import BeautifulSoup
# for last message box
import ctypes
#for sleep
import time

print("Welcome!")
time.sleep(1)
print("In a second you will get a prompt asking you to open a file")
time.sleep(2)
print("Simply choose your Risk of Rain 2 userprofile file")
time.sleep(2)
print("and boom your done")
time.sleep(1)
print("Welp. . . .  here goes nothing")

# Begin of file prompt code
root = tk.Tk()
# Hides root element which causes a window to popup
root.withdraw()

file_path = filedialog.askopenfilename()

# End of file prompt code

time.sleep(1)
print("Loading file")
# Use file path to open the file with the XML parser
xmlFile = BeautifulSoup(open(file_path, encoding='utf-8'), "xml")
if(xmlFile):
    time.sleep(1)
    print("Finding value")
    # Locate coins tag
    coins = xmlFile.find_all('coins')
    # always returns multiple entries
    for coin in coins:
        coin.string.replace_with('999999999')
    time.sleep(1)
    print("Saving file")
    # open with with write and save
    with open(file_path, 'w') as f:
        f.write(str(xmlFile))
else:
    print('ERROR suck it fucker')

ctypes.windll.user32.MessageBoxW(0, "You're now either rich or your save file is fucked", "Finished", 0)