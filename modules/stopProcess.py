import psutil
import json
import sys
import os

from . import readCard, logJson
from PyQt5 import QtWidgets, QtGui

currentUser     = os.environ["USERNAME"]
appConfigFile   = "\\Users\\{}\\AppData\\Roaming\\WinAppLockerRFID\\config\\ProtectedProcess.json".format(currentUser)
cardGrantedFile = "\\Users\\{}\\AppData\\Roaming\\WinAppLockerRFID\\config\\CardGranted.json".format(currentUser)

is_authorized = readCard.check_RFID_UID(cardGrantedFile)

#os.chmod(appConfigFile, 0o444)

def show_message_box(message):
    app = QtWidgets.QApplication(sys.argv)
    msgBox = QtWidgets.QMessageBox()
    msgBox.setWindowTitle("[RFID/NFC] WinAppLocker - Access Denied")
    msgBox.setText(message)
    msgBox.setWindowIcon(QtGui.QIcon("app.ico"))
    msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msgBox.exec_()

def stop_protected_processes():
    with open(appConfigFile) as json_file:
        data = json.load(json_file)
        protected_processes = data["ProcessusProtected"]["ProcessName"]

    for process in psutil.process_iter():
        try:
            is_authorized
            if process.name() in protected_processes and readCard.check_RFID_UID(cardGrantedFile) != True:
                process.kill()
                print(f"Process '{process.name()}' was stopped.")
                show_message_box(f"❌ Enter a valid card on the NFC/RFID Reader to use {process.name()}")
                logJson.write_to_json_file(process.name(), currentUser)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
