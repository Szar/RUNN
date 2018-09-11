#!"C:\Python27\python.exe"
import win32gui, win32con, win32api, time, ctypes
from Tkinter import *

running = True
hwndMain = win32gui.FindWindowEx(None, None, None, "SCUM  ")
hwndChild = win32gui.GetWindow(hwndMain, win32con.GW_CHILD)
hwndChild = hwndMain
pad = 15
running = False
def run():
	global running
	if running:
		win32api.PostMessage(hwndChild, win32con.WM_KEYUP, 0x57, 0)
		win32api.PostMessage(hwndChild, win32con.WM_KEYDOWN, 0x57, 0)
	root.after(1000, run)

def start():
	global running
	running = True
	display.configure(fg="red")

def stop():
	global running
	running = False
	win32api.PostMessage(hwndChild, win32con.WM_KEYUP, 0x57, 0)
	display.configure(fg="#ececec")

root = Tk()
root.title("Autorun")
root.configure(bg='#ececec')
app = Frame(root)
app.rowconfigure(0, weight=1)
app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=1)
app.grid(row=1, column=1)

display = Label(app, text="Autorun is active", fg="#ececec")
display.grid(padx=pad, pady=(pad,0))
display.configure(anchor="center")

start = Button(app, text="Start", command=start)
start.grid(row=1, column=0, padx=pad, pady=pad, sticky="NSW")
stop = Button(app, text="Stop", command=stop)
stop.grid(row=1, column=1, padx=(0,pad), pady=pad, sticky="NSE")

app.pack(expand=True)
root.after(1000, run)
root.mainloop()