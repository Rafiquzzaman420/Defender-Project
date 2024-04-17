from os.path import getsize, abspath
from os import listdir


class MeFileCheck:
    @staticmethod
    def size_check():
        size_detect = getsize('delete_me.py')
        
        return size_detect

    @staticmethod
    def name_check():
        store = ['delete_me.py', 'file_scanner.py', 'os_check.py', 'win_scr_off.py', 'dll_checker.py',
                 'dll_scanner.py', 'drive_indexer.py', 'c_drive.py', 'info_storer.py', 'install.py',
                 'kill_switch.py', 'info_store_class.py', 'comment_create.py', 'program_caller.py', 'std_dll_store.py',
                 'virus_remover.py', 'me_file_check.py']
        store.sort(reverse=False)
        finder = listdir((abspath('')))
        constant = (finder in store)
        if constant:
            print('No problems found.')
            # Here needs to write some expressions to evaluate the data and it's workflow
        else:
            print('Something went wrong!')
            # Same here like the above
        return constant

name_checker = MeFileCheck
file_name_check = name_checker.name_check()