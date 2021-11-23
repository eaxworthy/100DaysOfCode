import tkinter as tk

WINDOW_HEIGHT = 310
WINDOW_WIDTH = 290
PINK = '#e2979c'
RED = '#e7305b'
GREEN = '#9bdeac'
YELLOW = '#f7f5dd'
FONT_NAME = 'clean'
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


window = tk.Tk()
window.title('Pomodoro Timer')
window.minsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
window.config(bg=GREEN)
tomato_img = tk.PhotoImage(file='images/tomato.png')
canvas = tk.Canvas(width=WINDOW_WIDTH, height=tomato_img.height()+30, bg=GREEN, highlightthickness=0)

canvas.create_image(WINDOW_WIDTH//2-4, ((tomato_img.height()//2)+20), image=tomato_img)
canvas.create_text(WINDOW_WIDTH//2, 158, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))

start_button = tk.Button(window, text='Start', font=('Arial',12, "normal"))
pause_button = tk.Button(window, text='Pause', font=('Arial',12, "normal"))

counter = tk.Label(window, text='T', bg=GREEN, font=('Arial', 14, "normal"))

canvas.grid(column=1, row=0, columnspan=3, rowspan=2)
start_button.grid(column=0, row=2, columnspan=2, rowspan=1, pady=5, padx=20, sticky="W")
pause_button.grid(column=3, row=2, columnspan=2, rowspan=1, pady=5, padx=20, sticky="E")
counter.grid(column=2, row=2)

window.mainloop()
