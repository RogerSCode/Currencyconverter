import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Label
from tkinter import Text
from currency_converter import CurrencyConverter



c = CurrencyConverter()
currencies = tuple(c.currencies)

root = tk.Tk()

root.title("Converter")

root.resizable(False, False)

window_width = 600
window_height = 400

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

label1 = Label(root, text='Convert from:')
label1.pack(ipadx=10, ipady=10)

from_current_var = tk.StringVar()
from_currency = ttk.Combobox(root, textvariable=from_current_var)
from_currency.set(currencies[0])
from_currency['values'] = currencies 
from_currency.pack(fill=tk.X, padx=250, pady=5)

value = Text(root, height=1,width=15)
value.insert('1.0','0')
value.pack()

label2 = Label(root, text='Convert to:')
label2.pack(ipadx=10, ipady=10)


to_current_var = tk.StringVar()
to_currency = ttk.Combobox(root, textvariable=to_current_var)
to_currency.set(currencies[1])
to_currency['values'] = currencies 
to_currency.pack(fill=tk.X, padx=250, pady=5)

output = Text(root, height=1,width=15)

output.pack()

ttk.Button(root, text='Convert', command=lambda: output.insert(1.0, c.convert(value.get('1.0','end'), from_currency.get(), to_currency.get()))).pack() #TODO replace dummyargs with real ones

root.mainloop()