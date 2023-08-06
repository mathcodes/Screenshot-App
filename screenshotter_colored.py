import tkinter as tk
import pyautogui
import threading
from tkinter import ttk



def take_screenshots():
    while not stop_flag.is_set():
        pyautogui.hotkey('shift', 'command', '3')
        stop_flag.wait(2)

def start_screenshots():
    global stop_flag
    stop_flag = threading.Event()
    threading.Thread(target=take_screenshots).start()
    start_button.state(['disabled'])
    stop_button.state(['!disabled'])

def stop_screenshots():
    global stop_flag
    stop_flag.set()
    start_button.state(['!disabled'])
    stop_button.state(['disabled'])

# Create the GUI window
window = tk.Tk()
window.title("Screenshot Taker")
# create window geometry that taktes up the middle of the screen with 1/2 width and height of the screen
window.geometry("300x100+{}+{}".format(int(window.winfo_screenwidth()/2 - 150), int(window.winfo_screenheight()/2 - 50)))

# Style for buttons
style = ttk.Style()
style.configure("Start.TButton", background="green", foreground="#00f7a3")
style.configure("Stop.TButton", background="red", foreground="#bf1819")

# Start button
start_button = ttk.Button(window, text="START", command=start_screenshots, style="Start.TButton")
start_button.pack(pady=10)

# Stop button
stop_button = ttk.Button(window, text="STOP", command=stop_screenshots, state=tk.DISABLED, style="Stop.TButton")
stop_button.pack(pady=10)

# Run the GUI main loop
window.mainloop()
