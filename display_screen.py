import tkinter as tk
from PIL import Image, ImageTk


class DisplayScreen:
    def __init__(self, root):
        # Set the window title
        root.title("Chatbot")

        # Set the window size
        root.geometry("800x600")

        # Create the left pane for the character animation
        self.left_pane = tk.Frame(root, bg="white", highlightbackground="black", highlightthickness=1)
        self.left_pane.grid(row=0, column=0, rowspan=2, sticky='nsew')

        # Create the top right pane for the supplemental info
        self.top_right_pane = tk.Frame(root, bg="white", highlightbackground="black", highlightthickness=1)
        self.top_right_pane.grid(row=0, column=1, sticky='nsew')

        # Create the bottom right pane for the transcript of the heard and generated text
        self.bottom_right_pane = tk.Frame(root, bg="white", highlightbackground="black", highlightthickness=1)
        self.bottom_right_pane.grid(row=1, column=1, sticky='nsew')

        # Configure the columns to adjust their sizes as the window resizes
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=3)
        root.grid_rowconfigure(0, weight=3)
        root.grid_rowconfigure(1, weight=1)

        # Open an image file
        with Image.open("path_to_your_image.png") as img:
            # Convert the image to PhotoImage format
            photo = ImageTk.PhotoImage(img)

        # Create a label with the image in the left pane
        label = tk.Label(self.left_pane, image=photo)
        label.image = photo  # Keep a reference to the image to prevent it from being garbage collected
        label.pack()

    def start(self):
        # Start the display screen
        pass

    def update(self):
        # Update the display screen
        pass
