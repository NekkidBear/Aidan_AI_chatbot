import tkinter as tk
from PIL import Image, ImageTk


class DisplayScreen:
    def __init__(self, root):
        self.root = root
        self.paned_window = tk.PanedWindow(root, orient=tk.HORIZONTAL)
        self.paned_window.grid(sticky='nsew')

        # Create the browser frame (3/4 of the window)
        self.browser_frame = tk.Frame(self.paned_window, bg="#201f1f", highlightbackground="#464775", highlightthickness=1)
        self.paned_window.add(self.browser_frame)

        # Create the side panel frame (1/4 of the window)
        self.side_panel = tk.PanedWindow(self.paned_window, orient=tk.VERTICAL)
        self.paned_window.add(self.side_panel)

        # Create the top and bottom frames inside the side panel
        self.top_frame = tk.Frame(self.side_panel, bg="#201f1f", highlightbackground="#464775", highlightthickness=1)
        self.bottom_frame = tk.Frame(self.side_panel, bg="#201f1f", highlightbackground="#464775", highlightthickness=1)
        self.side_panel.add(self.top_frame)
        self.side_panel.add(self.bottom_frame)

        self.image_label = None
        self.text_widget = None
        self.photo_img = None

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

    def display_text(self, text, frame):
        if self.text_widget is None:
            self.text_widget = tk.Text(frame)
            self.text_widget.grid(sticky='nsew')
        self.text_widget.insert(tk.END, text)

    def start(self):
        # Start the tkinter display
        # Set the initial size of the panes
        self.browser_frame.config(width=self.root.winfo_width() * 3 // 4)
        self.side_panel.config(width=self.root.winfo_width() // 4)

    def update(self):
        # Update the tkinter display
        pass
