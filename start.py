from tkinter import messagebox
from notedb import NoteDB
from dashboard import Dashboard

if __name__=="__main__":
    try:
        db=NoteDB()             #initializing connection with database
        Dashboard().initUI(db)  #initializing Interface
    except Exception as e:
        messagebox.showinfo("Error","Unable to establish database connection.")