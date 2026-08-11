import tkinter as tk

from dice import roll, is_lucky


def on_click():
    value = roll()
    result_label.config(text=f"{value} → {is_lucky(value)}")


root = tk.Tk()
root.title("サイコロ")

tk.Button(root, text="サイコロを振る", font=("", 16), command=on_click).pack(padx=40, pady=20)

result_label = tk.Label(root, text="", font=("", 24))
result_label.pack(pady=(0, 20))

root.mainloop()