import tkinter as tk

def add_one_item(entry, listbox):
    item = entry.get()
    if item:
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)

def add_item():
    add_one_item(entry, listbox)

if __name__ == "__main__":
    app = tk.Tk()
    entry = tk.Entry(app)
    entry.pack()
    button = tk.Button(app, text='Add Item', command=add_item)
    button.pack()
    listbox = tk.Listbox(app)
    listbox.pack()
    app.mainloop()