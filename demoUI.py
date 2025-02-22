import customtkinter as ctk  # Added CustomTkinter
import tkinter as tk
from tkinter import Entry, Button

# Create main window
root = tk.Tk()
root.title("FRIADAY 2.O")
root.attributes('-fullscreen', True)  # Fullscreen mode
root.configure(bg="#181D28")  # Background color

# Configure grid for responsiveness
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

# Output Display (CTkTextbox) - Rounded Corners using CTk
output_box = ctk.CTkTextbox(root, wrap="word", fg_color="#000000", text_color="white", font=("Arial", 14), corner_radius=15, border_width=0)
output_box.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=300, pady=(10, 30))

# Frame to hold Copy Button inside output box
display_frame = tk.Frame(root, bg="#101112")
display_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=300, pady=(10, 30))  # Bottom padding 30

# Copy Button (Moved to the top right of output box)
copy_button = Button(display_frame, text="Copy", bg="#2e2f30", fg="white", relief="flat", padx=10, pady=5)
copy_button.place(relx=1.0, rely=0, anchor="ne", x=-10, y=10)  # Placed inside output box at top right

# Search Bar Container with adjusted bottom padding
search_frame = tk.Frame(root, bg="#181D28")
search_frame.grid(row=2, column=0, columnspan=2, sticky="ew", padx=300, pady=(20, 30))  # Bottom padding 30

# Search Entry (Styled Like Image) - Rounded Corners Added
search_entry = ctk.CTkEntry(search_frame, fg_color="#2e2f30", text_color="white", font=("Arial", 14),height=50, corner_radius=15, border_width=0)
search_entry.pack(side="left", expand=True, fill="both", padx=40, pady=10)  # Adjusted padding

# Search Button (Styled Like Image) - Added corner radius and reduced size
search_button = ctk.CTkButton(search_frame, text="🎤", fg_color="#2e2f30", text_color="white", corner_radius=10, width=45, height=50)
search_button.pack(side="right", padx=5)  # Extra spacing on right

# Make sure search box does not expand unnecessarily
root.grid_rowconfigure(2, weight=0)

root.mainloop()
