from tkinter import *
from tkinter import messagebox, font
from note import Note

class EditNote:
    def __init__(self):
        pass

    # method when update button is clicked
    def update_callback(self,note):
        msg=self.text.get("1.0",'end-1c')
        if len(msg) <=0:
            messagebox.showinfo("Invalid Action","Please Enter Note..")
            return
        try:
            obj=Note(idt=note.get_idt(),msg=msg)
            self.db.update_note(obj)
            self.dash.list_all_callback()
            self.dash.root.attributes('-disabled', False)
            self.root.destroy()
            messagebox.showinfo("Success","Note Updated..")
        except Exception as e:
            self.dash.root.attributes('-disabled', False)
            self.root.destroy()
            messagebox.showinfo("Error","Failed To Update Note.Try Again")

    # method when cancel button is clicked
    def cancel_callback(self):
        self.dash.root.attributes('-disabled', False)
        self.root.destroy()

    # method when delete button is clicked
    def delete_callback(self,note):
        try:
            self.db.delete_note(note)
            self.dash.list_all_callback()
            self.dash.root.attributes('-disabled', False)
            self.root.destroy()
            messagebox.showinfo("Success","Note Deleted!")
        except Exception as e:
            self.dash.root.attributes('-disabled', False)
            self.root.destroy()
            messagebox.showinfo("Error","Failed To Delete Note.Try Again")

    # method to create GUI for View/Edit Note
    def initUI(self,dash,db,note):
        self.dash=dash
        self.dash.root.attributes('-disabled', True)
        self.db=db
        self.root = Tk()
        self.root.geometry("500x500")
        self.root.configure(background='black')
        self.root.protocol("WM_DELETE_WINDOW", self.cancel_callback)
        self.root.title("Edit Note")
        self.Font = font.Font(family='Helvetica', size=15, weight='bold')
        self.Font_search_text = font.Font(family='Helvetica', size=15)
        self.Font_search_btn = font.Font(family='Helvetica', size=10, weight='bold')
        self.Font_note = font.Font(family='Helvetica', size=12)
        self.add_label=Label(self.root,text="View\Edit Note",font=self.Font,background='black',fg='#ffae42')
        self.add_label.place(x=170,y=15)
        self.text = Text(self.root,font=self.Font_note,width=50,height=18)
        self.text.insert('1.0',note.get_msg())
        self.text.place(x=15,y=40)
        self.scroll = Scrollbar(self.root, orient=VERTICAL, command=self.text.yview)
        self.text['yscroll'] = self.scroll.set
        self.scroll.place(x=465,y=40,height=330)
        time="Created At : "+str(note.get_time())
        self.time_label=Label(self.root,text=time,font=self.Font_note,background='black',fg='#ffae42')
        self.time_label.place(x=140,y=385)
        self.save_button=Button(self.root,bg="#ffae42",text="Update",command=lambda:self.update_callback(note),font=self.Font_search_btn,width=13)
        self.save_button.place(x=330,y=430)
        self.delete_button=Button(self.root,bg="#ffae42",text="Delete",command=lambda:self.delete_callback(note),font=self.Font_search_btn,width=13)
        self.delete_button.place(x=180,y=430)
        self.cancel_button=Button(self.root,bg="#ffae42",text="Cancel",command=lambda:self.cancel_callback(),font=self.Font_search_btn,width=13)
        self.cancel_button.place(x=40,y=430)
        self.root.mainloop()