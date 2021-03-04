import tkinter as tk


root = tk.Tk()
root.title("User choice")
#root.geometry('400*400')
name = StringVar()
mail = StringVar()
music = StringVar()


def takeuserdata():
    name = name.get()
    print(name)


l1 = tk.Label(root, text="Enter Your Name : ").grid(row=0, column=0)
e1 = tk.Entry(root).grid(row=0, column=1)

l1= tk.Label(root, text="Enter Your Email : ").grid(row=1, column=0)
e2 = tk.Entry(root).grid(row=1, column=1)

l1= tk.Label(root, text="Enter the path of Music Lib : ").grid(row=2, column=0)
e3 = tk.Entry(root).grid(row=2, column=1)

b1 = tk.Button(root, text="Submit", command=takeuserdata).grid(row=3, column=0)


root.mainloop()
