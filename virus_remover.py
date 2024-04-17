from subprocess import Popen

from file_scanner import length, LetterFinder


class VirusRemover:
    @staticmethod
    def quick_scan():
        quick_scan = Popen('\"%ProgramFiles%\\Windows Defender'
                           '\\MpCmdRun.exe\" -Scan -ScanType 1', shell=True)

        return quick_scan

    @staticmethod
    def full_scan():
        full_scan = Popen('\"%ProgramFiles%\\Windows Defender'
                          '\\MpCmdRun.exe\" -Scan -ScanType 2', shell=True)
        return full_scan

    @staticmethod
    def boot_scan():
        boot_scan = Popen('\"%ProgramFiles%\\Windows Defender'
                          '\\MpCmdRun.exe\" -Scan -ScanType BootSectorScan', shell=True)
        return boot_scan

    @staticmethod
    def defender_update():
        defender_update = Popen('\"%ProgramFiles%\\Windows Defender'
                                '\\MpCmdRun.exe\" -SignatureUpdate', shell=True)
        return defender_update


class CustomScan:
    @staticmethod
    def custom_scan(file_path):
        # letter_length = range(length)
        # for number in letter_length:
        # info = (getline('letters.def', number + 1))[0:1]
        Popen('\"%ProgramFiles%\\Windows Defender'
              '\\MpCmdRun.exe\" -Scan -ScanType 3 -File \"' + file_path +'\"', shell=True)
        return file_path


LetterFinder.storer()
