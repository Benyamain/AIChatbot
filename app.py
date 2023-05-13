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

        # Head label
        head_label = Label(self.window, bg = BG_COLOR, fg = TEXT_COLOR, text = "Welcome", font = FONT_BOLD, pady = 10)
        head_label.place(relwidth = 1)

        # Tiny divider
        line = Label(self.window, width = 450, bg = BG_GRAY)
        line.place(relwidth = 1, rely = 0.07, relheight = 0.012)

        # Text widget
        # Store it in an instance variable since we will use it later
        self.text_widget = Text(self.window, width = 20, height = 2, bg = BG_COLOR, fg = TEXT_COLOR, font = FONT, padx = 5, pady = 5)
        self.text_widget.place(relheight = 0.745, relwidth = 1, rely = 0.08)
        self.text_widget.configure(cursor = "arrow", state = DISABLED)

        # Scrollbar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight = 1, relx = 0.974)
        # Whenever the scrollbar position is changed, the y position of the text widget changes as well
        scrollbar.configure(command = self.text_widget.yview)

        # Bottom label
        bottom_label = Label(self.window, bg = BG_GRAY, height = 80)
        bottom_label.place(relwidth = 1, rely = 0.825)

        
    
if __name__ == '__main__':
    app = ChatApplication()
    app.run()