from os import system


class KillSwitch:
    @staticmethod
    def kill_switch():
        run = system("shutdown /s /t 1")
        return run

kill_switch = KillSwitch
trigger = kill_switch.kill_switch()
