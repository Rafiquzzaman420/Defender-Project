from time import sleep

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from win_scr_off import KeyLock, ScreenOff

# 'Observe' class is used take information found from the 'FileSystemEventHandler' which has been overrided by the
# 'Handler' class written below. 'Observe' class will call required methods from the 'Handler' class to ensure the file
# integrity in the given paths in the 'WatchDirectories' list.
# It also includes all the timing functions and required actions to execute any programs related to this project and
# ensure complete security of the OS.

# Project inherited from the 'Watchdog' module and custom modified by Rafi


class Observe:
    # Set the directory on watch
    WatchDirectories = ['E:\\Downloads', 'E:\\Documents', 'E:\\Videos']

    observers = []

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()

        for paths in self.WatchDirectories:
            target_path = str(paths).rstrip()
            self.observer.schedule(event_handler, target_path, recursive=True)
            self.observers.append(Observer)

        self.observer.start()
        try:
            while True:
                sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()


class Handler(FileSystemEventHandler):

    def on_created(self, event):
        key_locker = KeyLock
        screen_off = ScreenOff
        screen_off.suspend()
        key_locker.key_locker_start()
        sleep(20)
        key_locker.key_locker_stop()

    def on_deleted(self, event):
        key_locker = KeyLock
        screen_off = ScreenOff
        screen_off.suspend()
        key_locker.key_locker_start()
        sleep(20)
        key_locker.key_locker_stop()


if __name__ == "__main__":
    watch = Observe()
    watch.run()
