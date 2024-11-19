import tkinter as tk
import pyautogui
import time
import threading

# Flags for pausing and stopping
is_paused = False
is_stopped = False

# Function to type text with a delay for the typing effect
def type_text(input_text, delay):
    global is_paused, is_stopped
    for char in input_text:
        if is_stopped:  # Check if typing should stop
            break
        while is_paused:  # Check if typing should pause
            time.sleep(0.1)  # Pause check interval
        pyautogui.write(char)  # Types the character
        time.sleep(delay)       # Delay to mimic typing effect

# Function to start the typing process in a separate thread
def start_typing():
    global is_paused, is_stopped
    is_paused = False
    is_stopped = False
    input_text = text_entry.get("1.0", tk.END).strip()  # Get text from the textbox
    try:
        delay = float(delay_entry.get())  # Get delay between characters
    except ValueError:
        delay = 0.1  # Default delay if input is invalid
    time.sleep(5)  # Gives user 5 seconds to switch to Google Docs
    threading.Thread(target=type_text, args=(input_text, delay)).start()

# Function to pause/resume typing
def pause_typing():
    global is_paused
    is_paused = not is_paused  # Toggle pause state
    pause_button.config(text="Resume Typing" if is_paused else "Pause Typing")

# Function to stop typing
def stop_typing():
    global is_stopped
    is_stopped = True  # Set the stop flag to True

# Set up the Tkinter window
root = tk.Tk()
root.title("Auto Typing Application")

# Textbox for user to paste text
tk.Label(root, text="Paste your text here:").pack()
text_entry = tk.Text(root, height=10, width=50)
text_entry.pack()

# Entry box for typing speed
tk.Label(root, text="Typing delay (seconds per character):").pack()
delay_entry = tk.Entry(root)
delay_entry.insert(0, "0.1")  # Default delay
delay_entry.pack()

# Start button
start_button = tk.Button(root, text="Start Typing", command=start_typing)
start_button.pack()

# Pause/Resume button
pause_button = tk.Button(root, text="Pause Typing", command=pause_typing)
pause_button.pack()

# Stop button
stop_button = tk.Button(root, text="Stop Typing", command=stop_typing)
stop_button.pack()

# Instructions
instructions = tk.Label(root, text="Place your cursor in Google Docs within 5 seconds after clicking 'Start Typing'.")
instructions.pack()

# Run the Tkinter event loop
root.mainloop()
