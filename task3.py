import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Calculator")

        self.entry_var = tk.StringVar()
        self.entry_var.set("0")

        self.entry = tk.Entry(master, textvariable=self.entry_var, font=("Arial", 20), bd=5, justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we")

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0)
        ]

        for (text, row, column) in buttons:
            button = tk.Button(master, text=text, font=("Arial", 16), padx=20, pady=20, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column, padx=5, pady=5, sticky="we")

            if text.isdigit() or text == ".":
                button.config(bg="white", fg="black")
            elif text == "=":
                button.config(bg="orange", fg="white")
            elif text == "C":
                button.config(bg="red", fg="white")
            else:
                button.config(bg="lightgray")

    def on_button_click(self, value):
        current_value = self.entry_var.get()

        if value == "=":
            try:
                result = eval(current_value)
                self.entry_var.set(str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid input")
                self.entry_var.set("0")
        elif value == "C":
            self.entry_var.set("0")
        elif value == ".":
            if "." not in current_value:
                self.entry_var.set(current_value + ".")
        else:
            if current_value == "0":
                self.entry_var.set(value)
            else:
                self.entry_var.set(current_value + value)

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
