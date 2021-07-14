from tkinter import *

WINDOW_WIDTH = 450
WINDOW_HEIGHT = 100

convertions = {1: lambda:  str(round(float(input_entry.get())* 1.60934 ,2)) + ' Kilometers', 
        2: lambda: str(round(float(input_entry.get())* 3.78541 ,2)) + ' Liters', 
        3: lambda: str(round(float(input_entry.get())*0.45359 ,2)) + ' Kilograms'}


window = Tk()
window.title('Imperial/Metric Conversion')
window.minsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

parent_frame = Frame(window, height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
parent_frame.pack()

#Option Frame

option_frame = LabelFrame(parent_frame, text='Choose Conversion')
option_frame.grid(row=1,column=1, sticky=W, padx=10, pady=10, ipadx=5, ipady=10, rowspan=4)

mode = IntVar()
mode.set(1)

def set_output(name):
    input_label.config(text=name)
    output_label.config(text=convertions[mode.get()]())

Radiobutton(option_frame, text='Miles/Kilometers', variable=mode, value=1, command= lambda: set_output(' Miles')).pack(padx=2, pady=2)
Radiobutton(option_frame, text='Gallons/Liters', variable=mode, value=2, command=lambda: set_output(' Gallons')).pack(padx=2, pady=2)
Radiobutton(option_frame, text='Pounds/Kilograms', variable=mode, value=3, command=lambda: set_output(' Pounds')).pack(padx=2, pady=2)

#Input/Output Framw
text_frame = LabelFrame(parent_frame, text='Enter Values')
text_frame.grid(row=1, column=2, sticky=N, padx=10, pady=10, ipady=5, ipadx=5)

input_entry = Entry(text_frame, width=5)
input_entry.insert(END, '3.1')
input_entry.grid(row=1, column=1, padx=2, pady=12 )

input_label = Label(text_frame, text = 'Miles')
input_label.grid(row=1, column=2, padx=2, pady=2 )

equal_sign = Label(text_frame, text = ' = ')
equal_sign.grid(row=1, column=3, padx=2, pady=2 )

output_label = Label(text_frame, text=convertions[1]())
output_label.grid(row=1, column=4, padx=2, pady=2 )

button = Button(text_frame, text='Convert', command=lambda: output_label.config(text=convertions[mode.get()]()))
button.grid(row=2, column=1, columnspan=4, padx=2, pady=2)




window.mainloop()
