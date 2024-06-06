import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Abhishek Jaiswal\AppData\Local\Programs\Python\Python38\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Abhishek Jaiswal\AppData\Local\Programs\Python\Python38\tcl\tk8.6"

executables = [cx_Freeze.Executable("index.py", base=base, icon="neel.ico")]


cx_Freeze.setup(
    name = "Face Recognition Attendance System",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":[r"C:\Users\Abhishek Jaiswal\OneDrive\Desktop\FRAS Project\Images\neel.ico",'tcl86t.dll','database','tk86t.dll', 'Images','data','attendance_report']}},
    version = "1.0",
    description = "Face Recognition Automatic Attendace System | Developed By Jaiswal Abhishek M.,Kushal,Vikash Tripathi",
    executables = executables
    )
