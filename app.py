from tkinter import *
from unit_converter import *

root = Tk()
root.title('Convert KM->CM')

# Label who show the result
result = StringVar()
result.set('None number are converted')

text = Label(root, textvariable=result)
text.pack()

# Entry
numentry = IntVar()
fentry = Entry(root, textvariable=numentry)
fentry.pack()

fromentry = StringVar()
froentry = Entry(root, textvariable=fromentry, text='From unit')
froentry.pack()

toentry = StringVar()
tentry = Entry(root, textvariable=toentry)
tentry.pack()

# calculating the results

def callback():
    print(f'{numentry.get()}{fromentry.get()} -> {toentry.get()}')
    
    f_entry = fromentry.get()
    t_entry = toentry.get()
    totalvar = 0
    
    # kilometers to ?
    if f_entry == 'kms' and t_entry == 'mts':
        totalvar = km_to_mts(numentry.get())
    if f_entry == 'kms' and t_entry == 'cms':
        totalvar = km_to_cms(numentry.get())
    

    result.set(str(totalvar) + t_entry)

# Button
fbutton = Button(root, text="CONVERT", width=10, command=callback)
fbutton.pack()

# starting the app
root.mainloop()
