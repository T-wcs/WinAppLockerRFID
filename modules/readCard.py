import json, os, time
from smartcard.System import readers
from smartcard.util import toHexString

def check_RFID_UID(file_path):
    try:
        r = readers()
        reader = r[1]
        connection = reader.createConnection()
        connection.connect()
        apdu = [0xFF, 0xCA, 0x00, 0x00, 0x00]
        response, sw1, sw2 = connection.transmit(apdu)
        uid = toHexString(response)
        #print("Card UID :", uid)
    except:
        pass

    with open(file_path, "r") as json_file:
        data = json.load(json_file)
    granted_uids = data["GrantedUID"]
    #print("Granted UID :", granted_uids)

    try:
        if uid in granted_uids:
            print(f"Card N°{uid} => Card Authorized")
            return True
        else:
            print(f"Card N°{uid} => Card Restricted")
            return False
    except:
        pass
