import tkinter as tk

WINDOW_HEIGHT = 360
WINDOW_WIDTH = 290
PINK = '#e2979c'
RED = '#e7305b'
GREEN = '#9bdeac'
YELLOW = '#f1ffc4'
FONT_NAME = 'clean'
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
POM_COUNT = 0
MODE = 'WORK'

class Pomo:
    def __init__(self):
        #setup window
        self.window = tk.Tk()
        self.window.title('Pomodoro Timer')
        self.window.minsize( width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.window.config(bg=YELLOW)

        #setup tomato image
        tomato_img = tk.PhotoImage(file='images/tomato.png')
        self.canvas = tk.Canvas(width=WINDOW_WIDTH, height=tomato_img.height(), \
                                bg=YELLOW, highlightthickness=0)
        self.canvas.create_image(WINDOW_WIDTH//2, tomato_img.height()//2, image=tomato_img)
        self.canvas.create_text(WINDOW_WIDTH//2, 140, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
        self.mode = tk.Label(self.window, text = 'Work', bg=YELLOW, fg=RED, font=('Arial', 20, "bold"))


        self.start_button = tk.Button(self.window, text='Start', width=6, bg=GREEN,  font=('Arial',12, "normal"))
        self.pause_button = tk.Button(self.window, text='Pause', width=6, bg=RED, font=('Arial',12, "normal"))

        self.counter = tk.Label(self.window, text=str(POM_COUNT), fg=RED, bg=YELLOW, font=('Arial', 14, "bold"))

        self.mode.grid(column=0, row = 0, pady=20, sticky='S', columnspan=5)
        self.canvas.grid(column=0, row=1, columnspan=5, rowspan=2, sticky='N')
        self.start_button.grid(column=0, row=3, columnspan=2, rowspan=1, pady=10, padx=20, sticky="W")
        self.pause_button.grid(column=3, row=3, columnspan=2, rowspan=1, pady=10, padx=20, sticky="E")
        self.counter.grid(column=2, row=3)
        
        self.window.mainloop()

        def switch_mode():
            pass

if __name__ ==  "__main__":
    pomo = Pomo()




