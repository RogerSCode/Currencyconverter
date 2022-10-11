import tkinter as tk
from tkinter import ttk


from currency_converter import CurrencyConverter


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

current_var = tk.StringVar()
from_currency = ttk.Combobox(root, textvariable=current_var)
from_currency['values'] = ('value1', 'value2', 'value3')
from_currency.pack(fill=tk.X, padx=5, pady=5)



root.mainloop()