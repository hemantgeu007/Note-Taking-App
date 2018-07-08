from tkinter import messagebox, font
from tkinter import *
from note import Note

class AddNewNote:
    def __init__(self):
        pass

#method when save button is clicked
    def add_new_callback(self):
        msg=self.text.get("1.0",'end-1c')
        if len(msg) <=0:
            messagebox.showinfo("Invalid Action","Please Enter Note..")
            return
        try:
            obj=Note(msg=msg)
            self.db.add_note(obj)
            self.dash.list_all_callback()
            self.dash.root.attributes('-disabled', False)
            self.root.destroy()
            messagebox.showinfo("Success","Note Saved..")
        except Exception as e:
            self.dash.root.attributes('-disabled', False)
            self.root.destroy()
            messagebox.showinfo("Error","Failed To Save Note.Try Again")

#method when cancel button is
    def cancel_callback(self):
        self.dash.root.attributes('-disabled', False)
        self.root.destroy()

#method to create GUI for Add New Note>>>
    def initUI(self,dash,db):
        self.dash=dash
        self.dash.root.attributes('-disabled', True)
        self.db=db
        self.root = Tk()
        self.root.geometry("500x450")
        self.root.configure(background='black')
        self.root.protocol("WM_DELETE_WINDOW", self.cancel_callback)
        self.root.title("Create New Note")
        self.Font = font.Font(family='Helvetica', size=15, weight='bold')
        self.Font_search_text = font.Font(family='Helvetica', size=15)
        self.Font_search_btn = font.Font(family='Helvetica', size=10, weight='bold')
        self.Font_note = font.Font(family='Helvetica', size=12)
        self.add_label=Label(self.root,text="Add New Note Below",font=self.Font,background='black',fg='#ffae42')
        self.add_label.place(x=170,y=15)
        self.text = Text(self.root,font=self.Font_note,width=50,height=18)
        self.text.place(x=15,y=40)
        self.scroll = Scrollbar(self.root, orient=VERTICAL, command=self.text.yview)
        self.text['yscroll'] = self.scroll.set
        self.scroll.place(x=465,y=40,height=330)
        self.save_button=Button(self.root,bg="#ffae42",text="Save",command=lambda:self.add_new_callback(),font=self.Font_search_btn,width=13)
        self.save_button.place(x=300,y=390)
        self.cancel_button=Button(self.root,bg="#ffae42",text="Cancel",command=lambda:self.cancel_callback(),font=self.Font_search_btn,width=13)
        self.cancel_button.place(x=100,y=390)
        self.root.mainloop()