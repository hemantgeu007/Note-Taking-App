import pymysql as mysql
from note import Note

class NoteDB:

    #Establishing connection with Database
    def __init__(self):
        try:
            NoteDB.db=mysql.connect(host = "localhost",user = 'root',password = 'hemant252',db = "tk")
            # Add Your Database username, password and database name here
            NoteDB.cursor=NoteDB.db.cursor()
        except Exception as e:
            raise

    #method to insert new note in database
    def add_note(self,note):
        q="insert into tb(msg) values('%s')"%(note.get_msg())
        try:
            NoteDB.cursor.execute(q)
            NoteDB.db.commit()
        except Exception as e:
            print(e)
            NoteDB.db.rollback()
            raise

    #method to view a note from database
    def get_one_note(self,idt):
        q="select * from tb where id=%d"%(idt)
        try:
            NoteDB.cursor.execute(q)
            result=NoteDB.cursor.fetchall()
            obj=Note(idt=result[0],msg=result[1],time=result[2])
            return obj
        except Exception as e:
            raise

    #method to view all notes from database
    def get_all_notes(self):
        q="select * from tb order by time desc;"
        try:
            NoteDB.cursor.execute(q)
            notes=[]
            results=NoteDB.cursor.fetchall()
            for result in results:
                obj=Note(idt=result[0],msg=result[1],time=result[2])
                notes.append(obj)
            return notes
        except Exception as e:
            raise

    #method to update notes in database
    def update_note(self,note):
        q="update tb set msg='%s' where id=%d"%(note.get_msg(),note.get_idt())
        try:
            NoteDB.cursor.execute(q)
            NoteDB.db.commit()
        except Exception as e:
            
            NoteDB.db.rollback()
            raise

    # method to search notes in database
    def search_notes(self,query):
        q="select * from tb where msg like '%{0}%' order by time desc".format(query)
        try:
            NoteDB.cursor.execute(q)
            notes=[]
            results=NoteDB.cursor.fetchall()
            for result in results:
                obj=Note(idt=result[0],msg=result[1],time=result[2])
                notes.append(obj)
            return notes
        except Exception as e:
            raise

    # method to delete note in database
    def delete_note(self,note):
        q="delete from tb where id=%d"%(note.get_idt())
        try:
            NoteDB.cursor.execute(q)
            NoteDB.db.commit()
        except Exception as e:
            NoteDB.db.rollback()
            raise