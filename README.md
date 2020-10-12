# TadoAssistant

Python script to check for open window state from Tado, and disables heating when detected.

Upon first run configure your account with -c option. 
Prior to the first run create a ./data and ./log directory. So far did not invest in auto creation of directories...

ToDo: Make script fail proof.

dependencies:
* PyTado
* Fernet (Cryptography)
* Python >3.6
