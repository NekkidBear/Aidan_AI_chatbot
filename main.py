import tkinter as tk
from chatbot_engine import ChatbotEngine
from display_screen import DisplayScreen


class MainApp:
    def __init__(self, root_window):
        self.display_screen = DisplayScreen(root)
        self.chatbot_engine = ChatbotEngine()
        self.root = root_window
        self.root.geometry('800x600')

        # Create frames for the image, web browser, and chat transcript with MS Teams dark mode colors
        self.web_frame = tk.Frame(root, bg="#201f1f", highlightbackground="#464775", highlightthickness=1)
        self.chat_frame = tk.Frame(root, bg="#201f1f", highlightbackground="#464775", highlightthickness=1)
        self.image_frame1 = tk.Frame(root, bg="#201f1f", highlightbackground="#464775", highlightthickness=1)
        self.image_frame2 = tk.Frame(root, bg="#201f1f", highlightbackground="#464775", highlightthickness=1)

        # Position the frames in the grid
        self.web_frame.grid(row=0, column=0, sticky='nsew')
        self.chat_frame.grid(row=1, column=0, sticky='nsew')
        self.image_frame1.grid(row=0, column=1, sticky='nsew')
        self.image_frame2.grid(row=1, column=1, sticky='nsew')

        # Configure the grid to distribute space between frames
        for i in range(2):
            root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(0, weight=2)  # web and chat frames take up 2/3 of the width
        root.grid_columnconfigure(1, weight=1)  # image frames take up 1/3 of the width

    def start(self):
        # Start the chatbot engine and tkinter display
        self.display_screen.start()
        self.root.update()  # update the tkinter window
        self.display_screen.load_image("assets\\graphics\\Aidan Interactive AI avatar.png", self.image_frame1)
        # Start the chatbot engine and tkinter display
        recognized_text, generated_text = self.chatbot_engine.start()
        self.display_screen.display_text(f"You: {recognized_text}", self.display_screen.bottom_frame)
        self.display_screen.display_text(f"Aidan: {generated_text}", self.display_screen.bottom_frame)

    def update(self):
        # Update the chatbot engine and tkinter display
        recognized_text, generated_text = self.chatbot_engine.update()
        self.display_screen.display_text(f"You: {recognized_text}", self.display_screen.bottom_frame)
        self.display_screen.display_text(f"Aidan: {generated_text}", self.display_screen.bottom_frame)

        # Schedule the next update
        self.root.after(1000, self.update)  # Update every second


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    app.start()
    root.mainloop()
