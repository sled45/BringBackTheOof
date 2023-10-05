import os
from sys import exit as scriptEnd
from win32api import CopyFile
from win32gui import MessageBox
from win32con import *

#coded by sled45

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
def allSubsOf(b='.'):
  result = []
  for d in os.listdir(b):
    bd = os.path.join(b, d)
    if os.path.isdir(bd): result.append(bd)
  return result

def ReplaceWithOof(s):
    robloxDir = os.path.expandvars(r'%LOCALAPPDATA%\Roblox\Versions')
    if os.path.isdir(robloxDir) == False:
        MessageBox(None, "ERROR: bruh you dont even have Roblox installed", "BringBackTheOof", MB_ICONSTOP | MB_OK | MB_DEFBUTTON1)
    else:
        print(robloxDir)
        allVers = allSubsOf(robloxDir)
        print(allVers)
        latestVer = max(allVers, key=os.path.getmtime, default=0)
        print(latestVer)
        ouchPath = os.path.join(latestVer, r"content\sounds\ouch.ogg")
        print(ouchPath)
        if os.path.exists(ouchPath) == False:
            MessageBox(None, "ERROR: it seems your client might be outdated\nIt's also possible you may be using the MS Store version, which is not supported.", "BringBackTheOof", MB_ICONSTOP | MB_OK | MB_DEFBUTTON1)
        else:
            CopyFile(ouchPath, ouchPath + ".bak")
            if s == 0:
                CopyFile(resource_path("ouch.ogg"), ouchPath)
                MessageBox(None, "Success! The previous death sound has been backed up in case you change your mind.", "BringBackTheOof", MB_ICONINFORMATION | MB_OK | MB_DEFBUTTON1)
            else:
                CopyFile(resource_path("bruh.ogg"), ouchPath)
                MessageBox(None, "Success! The previous death sound has been backed up in case you change your mind.", "BringBackTheOof", MB_ICONINFORMATION | MB_OK | MB_DEFBUTTON1)
        
startMsg = MessageBox(None, "Do you want to replace the death sound?\n(Yes = Roblox OOF, No = bruh sfx)\nMake sure the most recently modified folder in the Roblox Versions folder is the client and not Roblox Studio!", "BringBackTheOof (Coded by @bluesled45 on Roblox)", MB_ICONQUESTION | MB_YESNOCANCEL | MB_DEFBUTTON1)
if startMsg == 6:
    print("epic duck!!!!!!!11!!!")
    ReplaceWithOof(0)
elif startMsg == 7:
    print("bruh sfx #2")
    ReplaceWithOof(1)
else:
    MessageBox(None, ":(", "BringBackTheOof", MB_ICONINFORMATION | MB_OK | MB_DEFBUTTON1)

