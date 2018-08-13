import cx_Freeze
import sys


base = None
if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("Speech_Recognizer.py", base=base, icon = "icon.ico")]

cx_Freeze.setup(
    name = "Speech Recognizer",
    author = "Mayank Kumar Giri",
    options = {"build_exe":{"packages":["tkinter", "speech_recognition", "threading", "time"], "include_files":["icon.ico", "wait.ico", "mic.ico", "save.ico"]}},
    version = "1.0",
    description = "Speech Recognizer cum Text Editor that facilitates voice typing using Google Speech Recognition API",
    executables = executables
)