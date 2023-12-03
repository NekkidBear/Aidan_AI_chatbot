import tkinter as tk
# from chatbot_engine import chatbot_engine
from display_screen import DisplayScreen


class MainApp:
    def __init__(self, root_window):
        self.root = root_window
        self.root.geometry('800x600')
        self.display_screen = DisplayScreen(root)

        # Create frames for the image, web browser, and chat transcript with MS Teams dark mode colors
        self.image_frame = tk.Frame(root, bg="#201f1f", highlightbackground="#464775", highlightthickness=1)
        self.web_frame = tk.Frame(root, bg="#201f1f", highlightbackground="#464775", highlightthickness=1)
        self.chat_frame = tk.Frame(root, bg="#201f1f", highlightbackground="#464775", highlightthickness=1)

        # create a label widget with white text inside the image frame
        character_label = tk.Label(self.image_frame, text="Character Image", fg="white")
        character_label.grid()
        web_label = tk.Label(self.web_frame, text="Web browser", fg="white")
        web_label.grid()
        chat_label = tk.Label(self.chat_frame, text="Text Transcript", fg="White")
        chat_label.grid()

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
        self.root.update()  # update the tkinter window
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
