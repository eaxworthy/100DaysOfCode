import tkinter as tk
import time
from playsound import playsound

#Display settings
WINDOW_HEIGHT = 360
WINDOW_WIDTH = 290
RED = '#f26849'
GREEN = '#379b46'
YELLOW = '#f1ffc4'
FONT_NAME = 'clean'
BUTTON_FONT = ('Arial',12, "normal")

#Time Settings
#Adjust however best fits you
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30

#Sound Settings
MODES = [("Work", WORK_MIN), ("Break", SHORT_BREAK_MIN), ("Long Break", LONG_BREAK_MIN)]


# //TODO: Have app grab attention at end of period, make a timer ding

class Pomo:
    def __init__(self):

        #state management variables
        self.pom_count = 0
        self.current_mode = 0
        self.minutes = WORK_MIN
        self.seconds = 0
        self.running = False

        #setup app window
        self.root = tk.Tk()
        self.root.title('Pomodoro Timer')
        self.root.minsize( width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.root.config(bg=YELLOW)

        #setup tomato image
        tomato_img = tk.PhotoImage(file='resources/images/tomato.png')
        self.canvas = tk.Canvas(width=WINDOW_WIDTH, height=tomato_img.height(), \
                                bg=YELLOW, highlightthickness=0)
        self.canvas.create_image(WINDOW_WIDTH//2, tomato_img.height()//2, \
                                image=tomato_img)

        #create timer
        self.timer_display = self.canvas.create_text(WINDOW_WIDTH//2, 140, \
                                text=str(self.minutes).zfill(2)+':'+str(self.seconds).zfill(2),
                                fill="white", font=(FONT_NAME, 28, "bold"))

        #setup text displays
        self.counter = tk.Label(self.root, text=str(self.pom_count), fg=RED, \
                                bg=YELLOW, font=('Arial', 14, "bold"))
        self.mode_display = tk.Label(self.root, text = MODES[self.current_mode][0], \
                                    bg=YELLOW, fg=RED, font=('Arial', 20, "bold"))

        #Setup buttons
        self.start_button = tk.Button(self.root, command=self.start_timer, \
                                      text='Start', width=6, bg=GREEN,  font=BUTTON_FONT)
        self.pause_button = tk.Button(self.root, command=self.pause_timer, \
                                      text='Pause', width=6, bg=RED, font=BUTTON_FONT)

        #Layout with grid
        self.mode_display.grid(column=0, row = 0, pady=20, sticky='S', columnspan=5)
        self.canvas.grid(column=0, row=1, columnspan=5, rowspan=2, sticky='N')
        self.start_button.grid(column=0, row=3, columnspan=1, rowspan=1, pady=10, padx=20, sticky="W")
        self.pause_button.grid(column=4, row=3, columnspan=1, rowspan=1, pady=10, padx=20, sticky="E")
        self.counter.grid(column=1, row=3, columnspan=3)

        #Start window
        self.root.mainloop()

    #Define button functions
    #start timer running
    def start_timer(self):
        if not self.running:
            self.running = True
            self.run_timer()

    #pause timer, kill running process
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
            #end of period, update mode
            self.root.focus_force()
            self.root.lift()

            #if last period was a work period, see what kind of break is next
            if not self.current_mode:
                self.mode_display['fg'] = GREEN
                self.pom_count += 1
                if not self.pom_count % 4:
                    self.current_mode = 2
                else:
                    self.current_mode = 1

            #set back to work mode
            else:
                self.mode_display['fg'] = RED
                self.current_mode = 0

            #update display
            self.mode_display['text'] = MODES[self.current_mode][0]
            self.minutes = MODES[self.current_mode][1]

        elif not self.seconds:
            #Start new minute
            self.minutes = self.minutes-1
            self.seconds = 59

        else:
            #normal second deprecation
            self.seconds = self.seconds - 1

        #update display
        self.canvas.itemconfigure(self.timer_display, text=str(self.minutes).zfill(2)+':'+str(self.seconds).zfill(2))
        self.counter['text'] = str(self.pom_count)

        #continue timer
        self.after_id = self.root.after(1000, self.run_timer)


if __name__ ==  "__main__":
    pomo = Pomo()
