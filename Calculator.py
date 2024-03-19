#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.result = tk.Entry(master, width=30, justify='right')
        self.result.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # create buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # create and add buttons to the grid
        row, col = 1, 0
        for button in buttons:
            command = lambda x=button: self.calculate(x)
            tk.Button(master, text=button, width=5, height=2, command=command).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def calculate(self, button):
        if button == 'C':
            self.result.delete(0, 'end')
        elif button == '=':
            try:
                result = str(eval(self.result.get()))
                self.result.delete(0, 'end')
                self.result.insert(0, result)
            except:
                self.result.delete(0, 'end')
                self.result.insert(0, "Error")
        else:
            self.result.insert('end', button)

root = tk.Tk()
calc = Calculator(root)
root.mainloop()


# In[ ]:




