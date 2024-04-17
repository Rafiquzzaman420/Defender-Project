from file_scanner import DllScanner
from std_dll_store import StandardDllStore


class DllChecker:
    def dll_checker():
        dll_scanner = DllScanner
        scan = dll_scanner.dll_scanner()

        check_with_dll_store = StandardDllStore

        if check_with_dll_store.standard_dll_store() == scan:
            print("Succeeded Perfectly")

        else:
            print("Something's not right!")


dll_check_start = DllChecker

dll_check_start.dll_checker()