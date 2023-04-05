# tkinter is used for the file prompt
import tkinter as tk
from tkinter import filedialog

# Beautifull soup is used for reading XML
from bs4 import BeautifulSoup

# Begin of file prompt code
root = tk.Tk()
# Hides root element which causes a window to popup
root.withdraw()

file_path = filedialog.askopenfilename()

# End of file prompt code


 

 
# Use file path to open the file with the XML parser
xmlFile = BeautifulSoup(open(file_path, encoding='utf-8'), "xml")

# Locate coins tag
coins = xmlFile.find_all('coins')
# always returns multiple entries
for coin in coins:
    coin.string.replace_with('999999999')

# open with with write and save
with open(file_path, 'w') as f:
    f.write(str(xmlFile))