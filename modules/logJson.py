import json, os
from datetime import datetime

currentUser = os.environ["USERNAME"]
logFilePath = "\\Users\\{}\\AppData\\Roaming\\WinAppLockerRFID\\data\\StartingAppBlocked.json".format(currentUser)
#os.chmod(logFilePath, 0o444)

def write_to_json_file(process_name, username):
    data = {}
    try:
        with open(logFilePath, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {
            "AppBlocked": {}
        }

    data["AppBlocked"][process_name] = {
        "User": username,
        "Date": str(datetime.now())
    }

    with open(logFilePath, "w") as file:
        json.dump(data, file, indent=4)
