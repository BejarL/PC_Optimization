import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from scripts.delete_temp_files import delete_temp_files
from scripts.delete_log_files import delete_log_files
from scripts.clear_dns_cache import clear_dns_cache

def run_script(script_func):
    """
    Runs the given script function and displays a message box with the result.
    """
    try:
        status_label.config(text=f"Running {script_func.__name__.replace('_', ' ').capitalize()}...")  # Update status
        root.update_idletasks()  # Refresh the window
        script_func()  # Execute the selected script function
        messagebox.showinfo("Success", f"{script_func.__name__.replace('_', ' ').capitalize()} executed successfully.")  # Show success message
    except Exception as e:
        messagebox.showerror("Error", f"Error running {script_func.__name__}: {e}")  # Show error message
    finally:
        status_label.config(text="Ready")  # Reset status

# Initialize the main window
root = tk.Tk()
root.title("PC Optimization Tool")

# Set window size and make it non-resizable
root.geometry("400x300")
root.resizable(False, False)

# Load icons
# icon_delete_temp = ImageTk.PhotoImage(Image.open("icons/delete_temp.png").resize((40, 40)))
# icon_delete_log = ImageTk.PhotoImage(Image.open("icons/delete_log.png").resize((40, 40)))
# icon_clear_dns = ImageTk.PhotoImage(Image.open("icons/clear_dns.png").resize((40, 40)))
# Uncomment the next line if you have an icon for disable_hpet
# icon_disable_hpet = ImageTk.PhotoImage(Image.open("icons/disable_hpet.png").resize((40, 40)))

# Add descriptive labels
description_label = tk.Label(root, text="Select an action to optimize your PC:", font=("Arial", 12))
description_label.pack(pady=10)

# Create frames for better layout
frame = tk.Frame(root)
frame.pack(pady=10)

# Create buttons for each script with icons and descriptions
btn_delete_temp = tk.Button(frame, text="Delete Temporary Files",compound=tk.LEFT, command=lambda: run_script(delete_temp_files))
btn_delete_temp.grid(row=0, column=0, padx=10, pady=10)

btn_delete_log = tk.Button(frame, text="Delete Log Files", compound=tk.LEFT, command=lambda: run_script(delete_log_files))
btn_delete_log.grid(row=1, column=0, padx=10, pady=10)

btn_clear_dns= tk.Button(frame, text="Clear DNS Cache", compound=tk.LEFT, command=lambda: run_script(clear_dns_cache))
btn_clear_dns.grid(row=2, column=0, padx=10, pady=10)

# Uncomment the next lines if you have defined the disable_hpet function and icon
# btn_disable_hpet = tk.Button(frame, text="Disable HPET", image=icon_disable_hpet, compound=tk.LEFT, command=lambda: run_script(disable_hpet))
# btn_disable_hpet.grid(row=3, column=0, padx=10, pady=10)

# Add a status bar
status_label = tk.Label(root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_label.pack(fill=tk.X, side=tk.BOTTOM, ipady=2)

# Run the main event loop
root.mainloop()
