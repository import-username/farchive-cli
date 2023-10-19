import psutil
import json
from settings import app_settings

def getRunningExecList():
    return [process.name() for process in psutil.process_iter()]

def getWhitelistedExecutableList():
    return [i.programExecutable for i in app_settings["running_program_backup_paths"]]

