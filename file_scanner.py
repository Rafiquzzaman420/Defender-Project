from os.path import exists, getsize
from sys import platform

# Finding all the drive letters

def drive_letters():
    drives = ''.join(letters for letters in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                     if exists('%s:/' % letters)) if platform == 'win32' else ''
    return drives


# Finding the length to determine drive numbers
length = len(drive_letters())

# Class to store and find drive letters

class LetterFinder:
    @staticmethod
    # Function to store the drive letters in a file called 'letters.def'
    def storer():
        storer = open('letters.def', 'w')
        storer.write('\n'.join(drive_letters()))
        storer.close()

class FileSize:
    @staticmethod
    def file_size_checker(file_path):
        size_checker = getsize(file_path)
        return size_checker
