import os
import time
from time import ctime
import datetime
from prettytable import PrettyTable
import platform ### check OS
### pop up alert 
import tkinter as tk 
from tkinter import messagebox

# tkinter settings
root = tk.Tk()
root.withdraw()



tbl = PrettyTable(["MODE","USER", "OS_TYPE", "INO", "DEV", "NLINK", "UID", "GID", "SIZE", "ATIME", "MTIME", "CTIME"])

exampleFile = "C:/Users/j9cha/OneDrive/Desktop/AccountPasswordsAndBankInfo/.BankScreenshots.jpg"


stats = os.stat(exampleFile)

tbl = PrettyTable(["MODE","USER","OS_TYPE", "INO", "DEV", "NLINK", "UID", "GID", "SIZE", "ATIME", "MTIME", "CTIME"])

tbl.add_row([stats.st_mode, os.getlogin(), platform.system(), stats.st_ino, stats.st_dev, stats.st_nlink, stats.st_uid, stats.st_gid, 
             stats.st_size, ctime(stats.st_atime), ctime(stats.st_mtime), ctime(stats.st_ctime) ])
tbl.title = "Original"
print(tbl.get_string())

# Modification Settings
fileLocation = r""
year = 2025
month = 10
day = 8
hour = 1
minute = 8
second = 25

# modify the modTime of the File
date = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
modTime = time.mktime(date.timetuple())

os.utime(exampleFile, (modTime, modTime))

stats = os.stat(exampleFile)

tbl = PrettyTable(["MODE","USER", "OS_TYPE", "INO", "DEV", "NLINK", "UID", "GID", "SIZE", "ATIME", "MTIME", "CTIME"])

tbl.add_row([stats.st_mode,os.getlogin(),  platform.system(), stats.st_ino, stats.st_dev, stats.st_nlink, stats.st_uid, stats.st_gid, 
             stats.st_size, ctime(stats.st_atime), ctime(stats.st_mtime), ctime(stats.st_ctime) ])

tbl.title = "MODIFIED"
print(tbl.get_string())
# Tkinter 

original_atime = stats.st_atime
while True:
    try:
        stats = os.stat(exampleFile)

        # Only pop-up if file is opened
        if stats.st_atime != original_atime:
            messagebox.showwarning("WARNING", "File is being accessed!")
            print("[WARNING] File is being accessed!")
            original_atime = stats.st_atime 

        time.sleep(2)
    except FileNotFoundError:
        messagebox.showerror("WARNING", "File was DELETED!")
        print("[WARNING] File was DELETED!")
        break
