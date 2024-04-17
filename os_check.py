import os
import platform
import subprocess as sub


# Function to start the installation process of "Defender" on Windows machine
class SoftInstallCaller:
    @staticmethod
    def soft_install_caller():
        sub.Popen("soft_install.py")  # Calling the soft_install.py


# Class to stop the installation process and delete all related files (Except Windows)
class DeleteMeCaller:
    @staticmethod
    def delete_me_caller():
        sub.run(["python3", "delete_me.py"])


# Checking the operating system using the 'if-elif-else' statement
if (os.name == 'nt') and (platform.system() == 'Windows'):  # Checking if matches the "windows" OS
    print("Windows OS detected. Installing. Please wait...")
    # Calling the soft_install_caller() function to install the software on "Windows" machine
    SoftInstallCaller.soft_install_caller()

# Checking if the OS matches to any Linux or Mac distro
elif (os.name == 'posix') or (platform.system() == 'Linux' or platform.system() == 'Darwin'):
    if platform.system() == 'Linux':  # Checking if matches any Linux distro
        print("\"Linux\" OS detected. Can't install here. Rolling back the installation process...")

        # Calling the delete_me_caller() function from the DeleteMeCaller class
        # noinspection PyArgumentList
        DeleteMeCaller.delete_me_caller()

    elif platform.system() == 'Darwin':  # Checking if matches any Mac distro
        print("\"Mac\" OS detected. Can't install here. Rolling back the installation process...")

        # Calling the delete_me_caller() function from the DeleteMeCaller class
        # noinspection PyArgumentList
        DeleteMeCaller.delete_me_caller()

else:  # If doesn't matches any known distro then showing the below message
    print("Can't detect any known OS. Rolling back the installation process...")

    # Calling the delete_me_caller() function from the DeleteMeCaller class
    # noinspection PyArgumentList
    DeleteMeCaller.delete_me_caller()
