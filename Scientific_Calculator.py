import tkinter as tk
import math

class ScientificCalculator:
    def _init_(self, root):
        self.root = root
        self.root.title("Scientific Calculator")

        # Entry for showing calculations
        self.entry = tk.Entry(root, width=30, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'sin', 'cos', 'tan', 'log',
            '(', ')', 'C', '^'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            self.create_button(button, row_val, col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def create_button(self, text, row, column):
        button = tk.Button(self.root, text=text, padx=20, pady=20,
                           command=lambda: self.on_button_click(text))
        button.grid(row=row, column=column)

    def on_button_click(self, text):
        if text == '=':
            try:
                expression = self.entry.get()
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif text == 'C':
            self.entry.delete(0, tk.END)
        elif text in {'sin', 'cos', 'tan', 'log'}:
            self.entry.insert(tk.END, f"math.{text}(")
        elif text == '^':
            self.entry.insert(tk.END, '')
        else:
            self.entry.insert(tk.END, text)

if _name_ == "_main_":
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()
