import tkinter as tk
from PIL import Image, ImageTk


class DisplayScreen:
    def __init__(self, root):
        self.image_label = None
        self.photo_img = None
        self.root = root

    def load_image(self, image_path, frame):
        frame.update_idletasks()  # Ensure that the frame has been displayed
        img = Image.open(image_path)
        img_width, img_height = img.size
        max_width, max_height = frame.winfo_width(), frame.winfo_height()
        scale = min(max_width / img_width, max_height / img_height)
        new_width, new_height = int(img_width * scale), int(img_height * scale)
        img = img.resize((new_width, new_height), Image.LANCZOS)
        self.photo_img = ImageTk.PhotoImage(img)
        self.image_label = tk.Label(frame, image=self.photo_img)
        self.image_label.grid(sticky='nsew')

    def start(self):
        # Start the tkinter display
        pass

    def update(self):
        # Update the tkinter display
        pass
