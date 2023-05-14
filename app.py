from tkinter import *
from chat import get_response, BOT_NAME
import time

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
        head_label = Label(self.window, bg = BG_COLOR, fg = TEXT_COLOR, text = "Coffee Shop", font = FONT_BOLD, pady = 10)
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

        # Message entry box
        self.message_entry = Entry(bottom_label, bg = "#2C3E50", fg = TEXT_COLOR, font = FONT)
        self.message_entry.place(relwidth = 0.74, relheight = 0.06, rely = 0.008, relx = 0.011)
        # When application starts, it already is in focus
        self.message_entry.focus()
        self.message_entry.bind("<Return>", self._on_enter_pressed)

        # Send button
        send_button = Button(bottom_label, text = "Send", font = FONT_BOLD, width = 20, bg = BG_GRAY, command = lambda: self._on_enter_pressed(None))
        send_button.place(relx = 0.77, rely = 0.008, relheight = 0.06, relwidth = 0.22)

    def _on_enter_pressed(self, event):
        message = self.message_entry.get()
        self._insert_message(message, "You")

    def _insert_message(self, message, sender):
        # Hit enter without putting any text in it
        if not message:
            return
        
        self.message_entry.delete(0, END)
        message_1 = f"{sender}: {message}\n\n"
        # Once user can type in and sends a message, disable it again
        self.text_widget.configure(state = NORMAL)
        self.text_widget.insert(END, message_1)
        self.text_widget.configure(state = DISABLED)

        self.window.after(1500, self._send_response, message)

    def _send_response(self, message):
        message_2 = f"{BOT_NAME}: {get_response(message)}\n\n"
        # Once user can type in and sends a message, disable it again
        self.text_widget.configure(state = NORMAL)
        self.text_widget.insert(END, message_2)
        self.text_widget.configure(state = DISABLED)

        # Scroll to the end to see the last message
        self.text_widget.see(END)
    
if __name__ == '__main__':
    app = ChatApplication()
    app.run()