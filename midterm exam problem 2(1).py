import tkinter as tk

def show_full_name():
    full_name = f"{first_name.get()} {middle_name.get()} {last_name.get()}"
    full_name_entry.delete(0, tk.END)
    full_name_entry.insert(0, full_name)


root = tk.Tk()
root.title("Midterm exam problem 2")


first_name_label = tk.Label(root, text="First Name:")
first_name_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
first_name = tk.Entry(root)
first_name.grid(row=0, column=1, padx=5, pady=5)

middle_name_label = tk.Label(root, text="Enter Middle Name:")
middle_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
middle_name = tk.Entry(root)
middle_name.grid(row=1, column=1, padx=5, pady=5)

last_name_label = tk.Label(root, text="Enter Last Name:")
last_name_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
last_name = tk.Entry(root)
last_name.grid(row=2, column=1, padx=5, pady=5)

full_name_label = tk.Label(root, text="Enter Full Name:")
full_name_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
full_name_entry = tk.Entry(root)
full_name_entry.grid(row=4, column=1, padx=5, pady=5)

show_name_button = tk.Button(root, text="Show Full Name", command=show_full_name)
show_name_button.grid(row=5, column=0, columnspan=3, padx=6, pady=6)


root.mainloop()
