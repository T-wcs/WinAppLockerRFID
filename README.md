# WinAppLockerRFID
It is a program to prevent access to an application or a set, based on the presence of a RFID card or badge

## Program details

The program runs in the background, and will monitor the active processes with the process names it finds in the `ProtectedProcess.json` file in its installation directory. (Requires administrator rights to edit it)

If a process is started but no card is detected on the RFID/NFC reader, then the process will be automatically closed and a message indicating that a valid badge is required to run the program.

List of example of protected process :  

```json
{
  "ProcessusProtected": {
      "ProcessName": [
        "TaskManager.exe",
        "KeePass.exe"
      ]
  }
}
```

If you try to open a program without a detected or valid card, for example KeePass.exe the following message will be returned :  

![image](https://user-images.githubusercontent.com/70718793/216811554-3a464093-75e5-4974-b5ed-adb565ad4754.png)

Each attempt to open a process will also be noted in a file named `StartingAppBlocked.json` in this format :  

```json
{
  "AppBlocked":
    {
      "KeePass.exe": {
        "User":"John",
        "Date":"2023-02-04 19:56:40.314587"
      },
      "notepad.exe": {
        "User":"John",
        "Date":"2023-02-04 19:54:07.490138"
      }
    }
}
```

To configure the authorized UIDs you have to modify the `CardGranted.json` file into the installation directory :   
```json
{
  "GrantedUID": [
    "03 1E 7A A1", "02 2D 73 A2"
  ]
}
```
