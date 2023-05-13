from tkinter import *
from chat import get_response, BOT_NAME

BG_GRAY, BG_COLOR, TEXT_COLOR, FONT, FONT_BOLD = "#ABB2B9", "#17202A", "#EAECEE", "Helvetica 14", "Helvetica 13 bold"

class ChatApplication:
    
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width = False, height = False)
        # That can take different attributes
        self.window.configure(width = 470, height = 550, bg = BG_COLOR)
    
if __name__ == '__main__':
    app = ChatApplication()
    app.run()