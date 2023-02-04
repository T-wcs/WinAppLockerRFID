#!/usr/env/python3
#coding:utf-8

import os, time
from modules import logJson, stopProcess, readCard

currentUser     = os.environ["USERNAME"]
cardGrantedFile = "\\Users\\{}\\AppData\\Roaming\\WinAppLockerRFID\\config\\CardGranted.json".format(currentUser)


while True:
    try:
        readCard.check_RFID_UID(cardGrantedFile)
        time.sleep(1)
        stopProcess.stop_protected_processes()
    except KeyboardInterrupt:
        exit()
