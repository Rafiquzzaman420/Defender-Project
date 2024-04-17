from os import sep, walk
from os.path import basename


class InfoStore:
    @staticmethod
    def info_store(root_path):
        store = open("store.txt", "a", encoding="utf-8")
        for root, folders, files in walk(root_path):
            tree = root.replace(root_path, '').count(sep)
            indent = ' ' * 4 * tree
            store.write('{}{}/'.format(indent, basename(root)) + "\n")
            sub_indent = ' ' * 4 * (tree + 1)
            for sub_files in files:
                store.write('{}{}'.format(sub_indent, sub_files) + "\n")

# An instance of FileLister class (Listing Class)
info_store = InfoStore
# ======================================================================================================================
# This 'InfoStore' class and 'info_store()' function contains all the code to list everything inside a Drive and it's
# all consecutive directories and also this will store them in a file named 'store.txt'. But it also takes a parameter
# which will be used to take the 'Drive Letter' to do it's work
# This will print information like :
# Folder1/
#         Subfolder1/
#                   File1
#         Subfolder2/
#                   File2
# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================
