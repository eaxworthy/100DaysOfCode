import tkinter as tk

WINDOW_HEIGHT = 390
WINDOW_WIDTH = 410
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
window.config(padx=100, pady=40, bg=GREEN)
tomato_img = tk.PhotoImage(file='images/tomato.png')
canvas = tk.Canvas(width=(tomato_img.width())+2, height=tomato_img.height(), bg=GREEN, highlightthickness=0)

canvas.create_image((tomato_img.width()//2)+2, (tomato_img.height()//2), image=tomato_img)
canvas.create_text(103, 138, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.pack()


window.mainloop()
