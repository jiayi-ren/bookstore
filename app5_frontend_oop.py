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
from app5_backend_oop import Database

database=Database("books.db")

class Window(object):

    def __init__(self,window):
        
        self.window=window
        self.window.title("Booksotre")

        l1=Label(window,text="Title")
        l1.grid(row=0,column=0)

        l2=Label(window,text="Year")
        l2.grid(row=1,column=0)

        l3=Label(window,text="Author")
        l3.grid(row=0,column=2)

        l4=Label(window,text="ISBN")
        l4.grid(row=1,column=2)


        self.title_text=StringVar()
        self.title=Entry(window,textvariable=self.title_text)
        self.title.grid(row=0,column=1)

        self.year_text=StringVar()
        self.year=Entry(window,textvariable=self.year_text)
        self.year.grid(row=1,column=1)

        self.author_text=StringVar()
        self.author=Entry(window,textvariable=self.author_text)
        self.author.grid(row=0,column=3)

        self.isbn_text=StringVar()
        self.isbn=Entry(window,textvariable=self.isbn_text)
        self.isbn.grid(row=1,column=3)

        self.list1=Listbox(window,height=6,width=35)
        self.list1.grid(row=2,column=0, rowspan=6, columnspan=2)

        sb1=Scrollbar(window)
        sb1.grid(row=2,column=2,rowspan=6)

        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>',self.get_selected_row)

        b1=Button(window,text="View all", width=12, command=self.view_command)
        b1.grid(row=2,column=3)

        b2=Button(window,text="Search entry", width=12, command=self.search_command)
        b2.grid(row=3,column=3)

        b3=Button(window,text="Add entry", width=12, command=self.add_command)
        b3.grid(row=4,column=3)

        b4=Button(window,text="Update selected", width=12, command=self.update_command)
        b4.grid(row=5,column=3)

        b5=Button(window,text="Delete selected", width=12, command=self.delete_command)
        b5.grid(row=6,column=3)

        b6=Button(window,text="Close", width=12, command=window.destroy)
        b6.grid(row=7,column=3)

    def get_selected_row(self,event):
        try:
            #self.selected_tuple
            index=self.list1.curselection()[0]
            self.selected_tuple=self.list1.get(index)
            self.title.delete(0,END)
            self.title.insert(END,self.selected_tuple[1])
            self.year.delete(0,END)
            self.year.insert(END,self.selected_tuple[3])
            self.author.delete(0,END)
            self.author.insert(END,self.selected_tuple[2])
            self.isbn.delete(0,END)
            self.isbn.insert(END,self.selected_tuple[4])
        except IndexError:
            pass

    def view_command(self):
        self.list1.delete(0,END)
        for row in database.view():
            self.list1.insert(END,row)

    def search_command(self):
        self.list1.delete(0,END)
        for row in database.search(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()):
            self.list1.insert(END,row)

    def add_command(self):
        if (not self.title_text.get()) and (not self.author_text.get()) and (not self.year_text.get()) and (not self.isbn_text.get()):
            pass
        else:
            database.insert(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
            self.list1.insert(END,(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()))

    def delete_command(self):
        try:
            database.delete(self.selected_tuple[0])
            self.list1.delete(self.list1.curselection()[0],self.list1.curselection()[0])
        except NameError:
            pass
        except IndexError:
            pass

    def update_command(self):
        try:
            database.update(self.selected_tuple[0],self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
        except NameError:
            pass

window = Tk()
Window(window)
window.mainloop()
