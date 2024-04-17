from subprocess import Popen


class ProgramCall:
    @staticmethod
    def win_scr_off_call():
        win_scr_off = Popen('python win_scr_off.py', shell=False)
        return win_scr_off

win_scr_off_call = ProgramCall

# This function is going to call the 'win_scr_off.py' program without the terminal window (Background process)
# =========================================================^============================================================
# This 'ProgramCall' class is going to store all the important functions needed, to run all the programs which will be
# used when running this program 'Defender' on 'Windows' OS