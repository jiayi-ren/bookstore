"""
A program that stores this book information:
Title, Author
Year, ISBN

User can:

View all records
Search an entry
Update entry
Delete
Close

"""
# EXE pyinstaller --onefile --windowed app5_frontend.py

from tkinter import *
import app5_backend

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        title.delete(0,END)
        title.insert(END,selected_tuple[1])
        year.delete(0,END)
        year.insert(END,selected_tuple[3])
        author.delete(0,END)
        author.insert(END,selected_tuple[2])
        isbn.delete(0,END)
        isbn.insert(END,selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    for row in app5_backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in app5_backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def add_command():
    app5_backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def delete_command():
    app5_backend.delete(selected_tuple[0])
    list1.delete(list1.curselection(),list1.curselection())

def update_command():
    app5_backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())


window = Tk()

window.title("Booksotre")

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Year")
l2.grid(row=1,column=0)

l3=Label(window,text="Author")
l3.grid(row=0,column=2)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)


title_text=StringVar()
title=Entry(window,textvariable=title_text)
title.grid(row=0,column=1)

year_text=StringVar()
year=Entry(window,textvariable=year_text)
year.grid(row=1,column=1)

author_text=StringVar()
author=Entry(window,textvariable=author_text)
author.grid(row=0,column=3)

isbn_text=StringVar()
isbn=Entry(window,textvariable=isbn_text)
isbn.grid(row=1,column=3)

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0, rowspan=6, columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View all", width=12, command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search entry", width=12, command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add entry", width=12, command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update selected", width=12, command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete selected", width=12, command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close", width=12, command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()
