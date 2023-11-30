import tkinter as tk

# Create the main window
root = tk.Tk()

# Set the window title
root.title("Display Screen")

# Set the window size
root.geometry("800x600")

# Create the left pane for the character animation
left_pane = tk.Frame(root, width=400, height=600, bg="white")
left_pane.pack(side="left", fill="both")

# Create the middle pane for the chat text
middle_pane = tk.Frame(root, width=400, height=300, bg="white")
middle_pane.pack(side="top", fill="both")

# Create the right pane for links and other returned information
right_pane = tk.Frame(root, width=400, height=300, bg="white")
right_pane.pack(side="bottom", fill="both")

# Start the main event loop
root.mainloop()
