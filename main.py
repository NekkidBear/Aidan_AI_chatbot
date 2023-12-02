import tkinter as tk
# from chatbot_engine import chatbot_engine
from display_screen import DisplayScreen


class MainApp:
    def __init__(self, root_window):
        self.root = root_window
        self.display_screen = DisplayScreen(root)

        # Create frames for the image, web browser, and chat transcript
        self.image_frame = tk.Frame(root)
        self.web_frame = tk.Frame(root)
        self.chat_frame = tk.Frame(root)

        # Position the frames in the grid
        self.image_frame.grid(row=0, column=0, rowspan=4, sticky='nsew')
        self.web_frame.grid(row=0, column=1, columnspan=3, rowspan=3, sticky='nsew')
        self.chat_frame.grid(row=3, column=1, columnspan=3, sticky='nsew')

        # Configure the grid to distribute space between frames
        for i in range(4):
            root.grid_rowconfigure(i, weight=1)
            if i > 0:
                root.grid_columnconfigure(i, weight=1)

    def start(self):
        # Start the chatbot engine and tkinter display
        # self.chatbot_engine.start()
        self.display_screen.start()
        self.display_screen.load_image("assets\\graphics\\Aidan Interactive AI avatar.png", self.image_frame)

    def update(self):
        # Update the chatbot engine and tkinter display
        # self.chatbot_engine.update()
        self.display_screen.update()

        # Schedule the next update
        self.root.after(1000, self.update)  # Update every second


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    app.start()
    root.mainloop()
