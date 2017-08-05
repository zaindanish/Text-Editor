from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


def donothing():
    print("Stop here need to add new functionality")


master = Tk()
master.title("Editor")
master.geometry("400x380")

#  *** Tool Bar *** #


toolbar = Frame(master, bg="blue")

insertButt = Button(toolbar, text="Insert Image", command=donothing)

insertButt.pack(side=LEFT, padx=2, pady=2)

printButt = Button(toolbar, text="Print", command=donothing)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

#  *** Scroll Bar *** #



scrollbar = Scrollbar(master)
scrollbar.pack(side=RIGHT, fill=Y)

#  *** Status Bar *** #


status = Label(master, text="Preparing to do nothing..", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

#  *** Text Area *** #

text = Text(master, undo=True, wrap=WORD, yscrollcommand=scrollbar.set, height=400, width=380, font=("Andale Mono", 12),
            highlightthickness=0, bd=2)
text.pack()
scrollbar.config(command=text.yview)


# methods


def new():
    ans = messagebox.askquestion(title="Save File", message="Would you like to save this file.")
    if ans == True:
        save()
    delete_all()


def open_file():
    new()
    file = filedialog.askopenfile()
    text.insert(INSERT, file.read())


def save():
    path = filedialog.asksaveasfilename()
    write = open(path, mode='w')
    write.write(text.get("1.0", END))


def exit_editor():
    master.quit()


def close():
    save()
    master.quit()


def cut():
    master.clipboard_clear()
    text.clipboard_append(string=text.selection_get())
    text.delete(index1=SEL_FIRST, index2=SEL_LAST)


def copy():
    master.clipboard_clear()
    text.clipboard_append(string=text.selection_get())


def paste():
    text.insert(INSERT, master.clipboard_get())


def delete():
    text.delete(index1=SEL_FIRST, index2=SEL_LAST)


def select_all():
    text.tag_add(SEL, "1.0", END)


def delete_all():
    text.delete(1.0, END)


def find_text():
    global entry_1
    root = Tk()
    root.title("Search in current file")
    root.geometry("400x100")
    root.resizable(width=False, height=False)

    label_1 = Label(root, text="Enter the text : ")
    label_1.grid(row=0, column=1)
    label_1.grid(padx=20, pady=20)
    entry_1 = Entry(root)
    entry_1.grid(row=0, column=2)
    entry_1.grid(padx=20, pady=20)
    button_1 = Button(root, text="Search", fg='red', command=find_text_child)  # =lambda:var.set(pri()));   \
    button_1.grid(row=1, column=2)
    root.mainloop()


def find_text_child():
    global entry_1

    temp = entry_1.get()

    print(temp)


def replace_text():
    pass


#  *** File Menu *** #


menu = Menu(master)
master.config(menu=menu)

file_menu = Menu(menu)
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new)
file_menu.add_command(label="Open", command=open_file)

file_menu.add_separator()

file_menu.add_command(label="Close", command=close)
file_menu.add_command(label="Save", command=save)
file_menu.add_command(label="Exit", command=exit_editor)

# file_menu.add_command(label="Rename", command=rename)


# *** Edit Menu *** #

edit_menu = Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=text.edit_undo)
edit_menu.add_command(label="Redo", command=text.edit_redo)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
edit_menu.add_command(label="Delete", command=delete)
edit_menu.add_separator()
edit_menu.add_command(label="Select All", command=select_all)

#  *** Search Menu *** #

search_menu = Menu(menu)
menu.add_cascade(label="Search", menu=search_menu)
search_menu.add_command(label="Find", command=find_text)
search_menu.add_command(label="Replace", command=replace_text)

#  *** About and Disclaimer Menu *** #









master.mainloop()



