from os import listdir


class DllScanner:
    @staticmethod
    def dll_scanner():
        # Listing all file names from the System32 directory
        dll_list = listdir("C:\\Windows\\System32")
        # Filtering out only the Dll files information in the dll_file_list variable
        dll_file_list = [dll_files for dll_files in dll_list if dll_files.endswith('.dll')]
        return dll_file_list
