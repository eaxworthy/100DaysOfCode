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

def switch_mode():
    pass

window = tk.Tk()
window.title('Pomodoro Timer')
window.minsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
window.config(bg=YELLOW)
tomato_img = tk.PhotoImage(file='images/tomato.png')
canvas = tk.Canvas(width=WINDOW_WIDTH, height=tomato_img.height(), bg=YELLOW, highlightthickness=0)

canvas.create_image(WINDOW_WIDTH//2-24, tomato_img.height()//2, image=tomato_img)
canvas.create_text(WINDOW_WIDTH//2-24, 140, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
mode = tk.Label(window, text = 'Work', bg=YELLOW, fg=RED, font=('Arial', 20, "bold"))


start_button = tk.Button(window, text='Start', bg=GREEN,  font=('Arial',12, "normal"))
pause_button = tk.Button(window, text='Pause', bg=RED, font=('Arial',12, "normal"))

counter = tk.Label(window, text=str(POM_COUNT), fg=RED, bg=YELLOW, font=('Arial', 14, "bold"))

mode.grid(column=2, row = 0, pady=20, sticky='S')
canvas.grid(column=1, row=1, columnspan=3, rowspan=2, sticky='N')
start_button.grid(column=0, row=3, columnspan=2, rowspan=1, pady=10, padx=20, sticky="W")
pause_button.grid(column=3, row=3, columnspan=2, rowspan=1, pady=10, padx=20, sticky="E")
counter.grid(column=2, row=3)

window.mainloop()
