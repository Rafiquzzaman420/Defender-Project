import os
import string

all_drives = ['%s:' % drives
              for drives in string.ascii_uppercase
              if os.path.exists('%s:' % drives)]

C_drive = all_drives.index('C:')


# function to print Drive name before the listing process
def drive_letter(num):
    name = all_drives
    printer = open("store.txt", 'w')
    printer.write(name[num] + '/' + '\n\n\n')
    printer.close()


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++^++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Specifically taking the C drive information as 'default' to print them first in 'store.txt'

drive_letter(C_drive)
# ======================================================================================================================
# Function 'drive_letter()' is used to take the letter such as 'C:' or 'D:' from the 'LetterCount' class as a single
# input and print them in the 'store.txt' file to clarify which file is in which directory. Like:
# 1. C:/
# 2.    info/
# 3.    info/
# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================
