# Attention : This code is made to prevent installing this software on any linux or mac distributions
import os
import time
import subprocess as sub


# Defining a class to delete every related file
class DeleteMeCreate:
    @staticmethod
    def delete_me_creator():
        creator = open("delete_me_deleter.py", 'x')
        creator.write("import os\n"
                      "import time\n"
                      "os.remove(\"delete_me.py\")""\n"
                      "time.sleep(1)\n"
                      "os.remove(\"delete_me_deleter.py\")")
        creator.close()


# Creating an executable class to execute 'delete_me_deleter.py'
class DeleteOpener:
    @staticmethod
    def delete_me_opener():
        sub.run(["python3", "delete_me_deleter.py"])


class ScreenOff:
    @staticmethod
    def screen_off():
        sub.run(["xset", "-display", ":0.0", "dpms", "force", "off"])


class FileDelete:
    @staticmethod
    def file_delete():
        os.remove("install.py")
        os.remove("os_check.py")
        os.remove("win_scr_off.py")
        os.remove("file_scanner.py")


screen_off = ScreenOff
screen_off.screen_off()
# Removing all the related files
time.sleep(10)
if screen_off.screen_off() is True:
    file_delete = FileDelete
    file_delete.file_delete()
else:
    print("! Can't delete the relative files !")
time.sleep(1)
# Creating a child program to delete this one (delete_me.py)
delete_me_creator = DeleteMeCreate
delete_me_creator.delete_me_creator()
opener = DeleteOpener()
opener.delete_me_opener()
