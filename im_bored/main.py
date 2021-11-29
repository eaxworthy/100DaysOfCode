import requests as rq
import tkinter as tk
from tkinter import ttk

BASE_URL = "http://www.boredapi.com/api/activity?"

PRICE_OPTIONS = {'Any':( 0.0, 1.0),'Any':('0.0', '1.0'), 'Free':('0', '0'), 'Inexpensive':('0.01', '0.33'), 'Moderate':('0.34', '0.66'), 'Expensive':('0.67', '1.0')}

DIFFICULTY_OPTIONS = {'Any':('0.0', '1.0'),'Any':('0.0', '1.0'), 'Easy':('0', '0.2'), 'Medium':('0.21','0.74'), 'Hard':('0.75', '1.0')}

CATEGORY_OPTIONS =["Any", "Any", "Busywork", "Charity", "Cooking", "DIY", "Education", "Music", "Recreation", "Relaxation", "Social"] 

PARTICIPANT_OPTIONS = ['Any', 'Any', '1', '2', '3', '4', '5']

class WideOptionMenu(ttk.OptionMenu):
    def __init__(self, master, variable, *options):
        ttk.OptionMenu.__init__(self, master, variable, *options)
        self.config(width=11)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.minsize(500, 175)
        self.maxsize(500, 175)
        self.title('Activity Generator')

        self.price_var = tk.StringVar()
        self.diff_var = tk.StringVar()
        self.cat_var = tk.StringVar()
        self.par_var = tk.StringVar()
        
        self.add_widgets()
        self.get_activity()

    def add_widgets(self):
        
        frame_paddings = {'padx':10, 'pady':10, 'sticky':'NSEW'}
        paddings = {'padx':5, 'pady':5, 'sticky':'W'}

        options_frame = tk.Frame(self)
        activity_frame = tk.Frame(self, relief='sunken', borderwidth=2)
       
        #Add options labels and selector menus
        cat_label = ttk.Label(options_frame, text='Category: ')
        cat_menu= WideOptionMenu(options_frame, self.cat_var, *CATEGORY_OPTIONS)

        price_label = ttk.Label(options_frame, text='Price: ')
        price_menu = WideOptionMenu(options_frame, self.price_var, *PRICE_OPTIONS.keys())

        diff_label = ttk.Label(options_frame, text='Difficulty: ')
        diff_menu=WideOptionMenu(options_frame, self.diff_var, *DIFFICULTY_OPTIONS.keys())

        par_label = ttk.Label(options_frame, text='Paricipants: ')
        par_menu = WideOptionMenu(options_frame, self.par_var, *PARTICIPANT_OPTIONS)
        
        #Add generator button
        button = ttk.Button(options_frame, text='Get Activity', command=self.get_activity)

        #Create text box to hold activity response
        self.activity_text = tk.Label(activity_frame, wraplength=200, justify=tk.LEFT)
       
        #Configure grid
        self.columnconfigure(1, weight=2)
    
        #Add widgets to grid
        options_frame.grid(row=0, column=0, **frame_paddings)
        cat_label.grid(row=0, column=0, **paddings)
        cat_menu.grid(row=0, column=1, **paddings)
        price_label.grid(row=1, column=0, **paddings)
        price_menu.grid(row=1, column=1, **paddings)
        diff_label.grid(row=2, column=0, **paddings)
        diff_menu.grid(row=2, column=1, **paddings)
        par_label.grid(row=3, column=0, **paddings)
        par_menu.grid(row=3, column=1, **paddings)
        button.grid(row=4, column = 0, columnspan=2, **paddings)
        
        activity_frame.grid(row=0,rowspan=5, column=1, **frame_paddings)
        self.activity_text.grid(row=0, rowspan=5, column =0, **paddings)
        
    def get_activity(self):
        price_min, price_max = PRICE_OPTIONS[self.price_var.get()]
        price_range = f'minprice={price_min}&maxprice={price_max}&'
        
        diff_min, diff_max = DIFFICULTY_OPTIONS[self.diff_var.get()]
        diff_range = f'minaccessibility={diff_min}&maxaccessibility={diff_max}'
        
        category = self.cat_var.get().lower()
        category = '&type='+category if category != 'any' else '' 
        participants = self.par_var.get().lower()
        participants = '&participants='+participants if participants != 'any' else ''

        response = rq.get(BASE_URL+price_range+diff_range+category+participants)
        try: 
            self.activity_text['text'] = response.json()['activity']
        except:
            self.activity_text['text'] = "No activities matching chosen parameters found"

if __name__ == '__main__':
    app = App()
    app.mainloop()

