import tkinter as tk
import pyautogui
import threading

def take_screenshots():
    while not stop_flag.is_set():
        pyautogui.hotkey('command', 'shift', '3')
        stop_flag.wait(5)

def start_screenshots():
    global stop_flag
    stop_flag = threading.Event()
    threading.Thread(target=take_screenshots).start()
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)

def stop_screenshots():
    global stop_flag
    stop_flag.set()
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)

# Create the GUI window
window = tk.Tk()
window.title("Screenshot Taker")
window.geometry("300x100")

# Start button
start_button = tk.Button(window, text="START", command=start_screenshots)
start_button.pack(pady=10)

# Stop button
stop_button = tk.Button(window, text="STOP", command=stop_screenshots, state=tk.DISABLED)
stop_button.pack(pady=10)

# Run the GUI main loop
window.mainloop()