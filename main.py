import tkinter as tk
from chatbot_engine import chatbot_engine
from display_screen import display_screen


class MainApp:
    def __init__(self, root):
        self.root = root
        self.chatbot_engine = chatbot_engine()
        self.tkinter_display = display_screen(root)

    def start(self):
        # Start the chatbot engine and tkinter display
        self.chatbot_engine.start()
        self.tkinter_display.start()

    def update(self):
        # Update the chatbot engine and tkinter display
        self.chatbot_engine.update()
        self.tkinter_display.update()

        # Schedule the next update
        self.root.after(1000, self.update)  # Update every second


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    app.start()
    root.mainloop()
