import tkinter as tk
import time

WINDOW_HEIGHT = 360
WINDOW_WIDTH = 290
PINK = '#e2979c'
RED = '#e7305b'
GREEN = '#9bdeac'
YELLOW = '#f1ffc4'
FONT_NAME = 'clean'
BUTTON_FONT = ('Arial',12, "normal")

WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 30
MODES = ["Work", "Rest", "Long Rest"]
START_TIMES = [WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN]

class Pomo:
    def __init__(self):

        self.pom_count = 0
        self.current_mode = 0
        self.minutes = WORK_MIN
        self.seconds = 0
        self.running = False

        #setup window
        self.root = tk.Tk()
        self.root.title('Pomodoro Timer')
        self.root.minsize( width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.root.config(bg=YELLOW)

        #Setup tomato image
        tomato_img = tk.PhotoImage(file='images/tomato.png')
        self.canvas = tk.Canvas(width=WINDOW_WIDTH, height=tomato_img.height(), \
                                bg=YELLOW, highlightthickness=0)
        self.canvas.create_image(WINDOW_WIDTH//2, tomato_img.height()//2, image=tomato_img)
        self.timer_display = self.canvas.create_text(WINDOW_WIDTH//2, 140, text=str(self.minutes).zfill(2)+':'+str(self.seconds).zfill(2), fill="white",
                                font=(FONT_NAME, 28, "bold"))

        #Setup text displays
        self.counter = tk.Label(self.root, text=str(self.pom_count), fg=RED, bg=YELLOW, font=('Arial', 14, "bold"))
        self.mode_display = tk.Label(self.root, text = MODES[self.current_mode], bg=YELLOW, fg=RED, font=('Arial', 20, "bold"))

        #Setup buttons
        self.start_button = tk.Button(self.root, command=self.start_timer, text='Start', width=6, bg=GREEN,  font=BUTTON_FONT)
        self.pause_button = tk.Button(self.root, command=self.pause_timer, text='Pause', width=6, bg=RED, font=BUTTON_FONT)
       # self.start_button.bind("<Button>", start_timer)
       # self.pause_button.bind("<Button>", pause_timer)


        #Layout with grid
        self.mode_display.grid(column=0, row = 0, pady=20, sticky='S', columnspan=5)
        self.canvas.grid(column=0, row=1, columnspan=5, rowspan=2, sticky='N')
        self.start_button.grid(column=0, row=3, columnspan=1, rowspan=1, pady=10, padx=20, sticky="W")
        self.pause_button.grid(column=4, row=3, columnspan=1, rowspan=1, pady=10, padx=20, sticky="E")
        self.counter.grid(column=1, row=3, columnspan=3)
        
        #Start window
        self.root.mainloop()

    #Define button functions
    def start_timer(self):
        if not self.running:
            self.running = True
            self.run_timer()

    def pause_timer(self):
        if self.running:
            self.root.after_cancel(self.after_id)
            self.running = False

    def run_timer(self):

        #Check to see if paused
        if not self.running:
            return

        #update display
        if not self.seconds and not self.minutes:
            #update mode
            if not self.current_mode:
                self.pom_count += 1
                if not self.pom_count % 4:
                    self.current_mode = 2
                else:
                    self.current_mode = 1

            else:
                self.current_mode = 0
                
            self.mode_display['text'] = MODES[self.current_mode]
            self.minutes = START_TIMES[self.current_mode] 
        
        elif not self.seconds:  
            self.minutes = self.minutes-1
            self.seconds = 59       
        
        else: 
            self.seconds = self.seconds - 1
        
        self.canvas.itemconfigure(self.timer_display, text=str(self.minutes).zfill(2)+':'+str(self.seconds).zfill(2))
        self.counter['text'] = str(self.pom_count)
        self.after_id = self.root.after(1000, self.run_timer)
    

if __name__ ==  "__main__":
    pomo = Pomo()




