from tkinter import *
from tkinter import messagebox, font
from editnote import EditNote
from addnewnote import AddNewNote

class Dashboard:
    #initializing dashboard
    def __init__(self):
        pass

    #method to show notes
    def show_notes(self,notes):
        i=0
        self.curr_notes=notes
        self.listbox.delete(0,self.listbox.size())
        for note in notes:
            self.listbox.insert(i,str(note.get_msg()))
            if i%2==0:
                self.listbox.itemconfig(i,bg="#d3d3d3")
            i+=1

    #method when search button is clicked
    def search_callback(self):
        if len(self.var.get())<=0:
             messagebox.showinfo("Invalid Action","Please Enter Search Entry")
             return
        notes=self.db.search_notes(self.var.get())
        if len(notes) ==0:
              messagebox.showinfo("Info","No match Found")
        else:
              self.show_notes(notes)

    def list_all_callback(self):
        try:
            notes=self.db.get_all_notes()
            self.show_notes(notes) 
        except Exception as e:
            print(e)
            messagebox.showinfo("Error","Could Not Fetch Notes")

    #method to call editnote when a note is clicked
    def edit_callback(self):
        try:
            EditNote().initUI(self,self.db,self.curr_notes[self.listbox.curselection()[0]])
        except Exception as e:
            pass

    # method to call addnewnote when a add new note>>> button is clicked is clicked
    def add_callback(self):
        AddNewNote().initUI(self,self.db)

    #method when about in help menu is clicked
    def about(self):
        messagebox.showinfo('About',"This app is a Note taking app.In this app you can add new notes,edit notes,delete notes etc.You can simply add new note by clicking the 'Add New Note>>>' button."
                                    "You can edit a note by clicking on the note.You can also delete the note from there\n\n"
                            "This app is created by Hemant Singh Pawnar.\nHope you liked the application.")

    #Interface of the application
    def initUI(self,db):
        self.db=db
        self.root = Tk()
        self.menubar = Menu(self.root)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Exit", command=self.root.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About", command=self.about)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        self.root.config(menu=self.menubar)
        self.root.geometry("1000x800")
        self.root.configure(background = 'black')
        self.root.title("Note Taking App")
        self.Font = font.Font(family='Helvetica', size='24', weight='bold', slant='italic')
        self.Font_search_text = font.Font(family='Helvetica', size=15)
        self.Font_search_btn = font.Font(family='Helvetica', size=10, weight='bold')
        self.Font_note = font.Font(family='Helvetica', size=15)
        self.add_button=Button(self.root,width=20,bg="#ffae42",fg="white",text="Add New Note>>",font=self.Font,command=lambda:self.add_callback())
        self.add_button.place(x=40,y=100)
        self.list_all_btn=Button(self.root,width=20,bg="#ffae42",fg="white",text="List All Notes",font=self.Font,command=lambda:self.list_all_callback())
        self.list_all_btn.place(x=540,y=100)
        self.var=StringVar()
        self.search_box=Entry(self.root,width=40,textvariable=self.var,font=self.Font_search_text)
        self.search_box.place(x=200,y=200)
        self.search_button=Button(self.root,fg="white",text="Search",font=self.Font_search_btn,width=25,height=22,command=lambda:self.search_callback())
        self.search_button.place(x=650,y=200)
        self.icon=PhotoImage(file='search.png')
        self.search_button.config(image=self.icon)
        self.note_label=Label(self.root,text="-- Notes --",font=self.Font,background='black',fg='#ffae42')
        self.note_label.place(x=410,y=300)
        self.listbox = Listbox(self.root,selectmode=SINGLE,width=80,font=self.Font_note,height=12,)
        self.scroll = Scrollbar(self.root, orient=VERTICAL, command=self.listbox.yview)
        self.listbox['yscroll'] = self.scroll.set
        self.scroll.place(x=900,y=350,height=292)
        self.list_all_callback()
        self.listbox.bind('<<ListboxSelect>>', lambda l:self.edit_callback())
        self.listbox.place(x=30,y=350)
        self.root.mainloop()