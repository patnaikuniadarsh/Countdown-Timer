import tkinter as tk
from tkinter import messagebox
import winsound  # For sound alert

# Global variables
time_left = 0
paused = False

def initiate_timer():
    global time_left, paused
    
    try:
        hrs = int(hours_input.get())
        mins = int(minutes_input.get())
        secs = int(seconds_input.get())
    except ValueError:
        messagebox.showerror("Input Error", "Enter valid numbers only!")
        return

    time_left = hrs * 3600 + mins * 60 + secs
    paused = False
    
    start_btn.config(state="disabled")
    pause_btn.config(state="normal")
    reset_btn.config(state="normal")
    
    update_timer()

def pause_timer():
    global paused
    paused = True
    pause_btn.config(state="disabled")
    start_btn.config(state="normal")

def reset_timer():
    global time_left, paused
    time_left = 0
    paused = False
    countdown_label.config(text="00:00:00")
    start_btn.config(state="normal")
    pause_btn.config(state="disabled")
    reset_btn.config(state="disabled")
    
    # Clear input fields
    hours_input.delete(0, tk.END)
    minutes_input.delete(0, tk.END)
    seconds_input.delete(0, tk.END)

def update_timer():
    global time_left, paused
    
    if paused:
        return
        
    if time_left >= 0:
        display_hrs, remainder = divmod(time_left, 3600)
        display_mins, display_secs = divmod(remainder, 60)
        countdown_label.config(text=f"{display_hrs:02d}:{display_mins:02d}:{display_secs:02d}")
        
        if time_left == 0:
            messagebox.showinfo("Timer Finished", "Time's up!")
            winsound.Beep(1000, 500)  # Beep sound
            start_btn.config(state="normal")
            pause_btn.config(state="disabled")
            reset_btn.config(state="disabled")
            return
            
        time_left -= 1
        root.after(1000, update_timer)

def set_preset(seconds):
    hours_input.delete(0, tk.END)
    minutes_input.delete(0, tk.END)
    seconds_input.delete(0, tk.END)
    hours_input.insert(0, str(seconds // 3600))
    minutes_input.insert(0, str((seconds % 3600) // 60))
    seconds_input.insert(0, str(seconds % 60))

# Create main application window
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("500x550")
root.configure(bg="#FAF3E0")

container = tk.Frame(root, bg="#F7C59F", bd=4, relief="groove")
container.place(relx=0.5, rely=0.5, anchor="center")

header = tk.Label(container, text="Countdown Timer", font=("Verdana", 22, "bold"), bg="#F7C59F")
header.pack(pady=15)

countdown_label = tk.Label(container, text="00:00:00", font=("Verdana", 32, "bold"), bg="#F7C59F")
countdown_label.pack(pady=10)

# Preset buttons
preset_frame = tk.Frame(container, bg="#F7C59F")
preset_frame.pack(pady=5)

tk.Button(preset_frame, text="1 min", font=("Verdana", 10), bg="#FFB347", command=lambda: set_preset(60)).pack(side="left", padx=5)
tk.Button(preset_frame, text="5 min", font=("Verdana", 10), bg="#FFB347", command=lambda: set_preset(300)).pack(side="left", padx=5)
tk.Button(preset_frame, text="10 min", font=("Verdana", 10), bg="#FFB347", command=lambda: set_preset(600)).pack(side="left", padx=5)

input_section = tk.Frame(container, bg="#F7C59F")
input_section.pack(pady=10)

hours_input = tk.Entry(input_section, width=4, font=("Verdana", 18))
hours_input.grid(row=0, column=0, padx=5)
minutes_input = tk.Entry(input_section, width=4, font=("Verdana", 18))
minutes_input.grid(row=0, column=1, padx=5)
seconds_input = tk.Entry(input_section, width=4, font=("Verdana", 18))
seconds_input.grid(row=0, column=2, padx=5)

# Label for Hrs Mins Secs
label_frame = tk.Frame(container, bg="#F7C59F")
label_frame.pack()
tk.Label(label_frame, text="Hrs", font=("Verdana", 10), bg="#F7C59F").grid(row=0, column=0, padx=15)
tk.Label(label_frame, text="Mins", font=("Verdana", 10), bg="#F7C59F").grid(row=0, column=1, padx=15)
tk.Label(label_frame, text="Secs", font=("Verdana", 10), bg="#F7C59F").grid(row=0, column=2, padx=15)

# Button frame
button_frame = tk.Frame(container, bg="#F7C59F")
button_frame.pack(pady=20)

start_btn = tk.Button(button_frame, text="Start", font=("Verdana", 12), bg="#EC6E4C", fg="white", command=initiate_timer)
start_btn.pack(side="left", padx=10)

pause_btn = tk.Button(button_frame, text="Pause", font=("Verdana", 12), bg="#FFA500", fg="white", command=pause_timer, state="disabled")
pause_btn.pack(side="left", padx=10)

reset_btn = tk.Button(button_frame, text="Reset", font=("Verdana", 12), bg="#808080", fg="white", command=reset_timer, state="disabled")
reset_btn.pack(side="left", padx=10)

root.mainloop()