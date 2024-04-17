import ctypes
from ctypes import *


# Class to turn the screen off (Sleep)
class ScreenOff:
    @staticmethod
    def suspend():
        ctypes.windll.PowrProf.SetSuspendState(0, 1, 0)


class KeyLock:
    @staticmethod
    def key_locker_start():  # Needs administrative privilege
        start = windll.user32.BlockInput(True)  # enable block
        return start

    @staticmethod  # Needs administrative privilege
    def key_locker_stop():
        stop = windll.user32.BlockInput(False)
        return stop
