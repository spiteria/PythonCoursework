'''
Created on Nov 17, 2014

@author: AndrewSpiteri
'''
import sqlite3

def main():
    dbconn = sqlite3.connect('mydatabase.db', isolation_level=None)
    
    c = dbconn.cursor()
    
    c.execute("DELETE FROM CLASSES WHERE NAME='Jane Smith'" )
    c.execute("DELETE FROM CLASSES WHERE NAME='Sallie Mae'" )
    c.execute("DELETE FROM CLASSES WHERE NAME='Freddie Mac'" )
    c.execute("""INSERT INTO CLASSES (CLASSID, NAME, INSTRUCTOR, SEMESTER)
        VALUES(?,?,?,?)""",['Statistics','Jane Smith', 'Qu', 'FALL'])
    c.execute("""INSERT INTO CLASSES (CLASSID, NAME, INSTRUCTOR, SEMESTER)
        VALUES(?,?,?,?)""",['Statistics','John Smith', 'Qu', 'FALL'])
    c.execute("""INSERT INTO CLASSES (CLASSID, NAME, INSTRUCTOR, SEMESTER)
        VALUES(?,?,?,?)""",['Python','Sallie Mae', 'Popovici', 'FALL'])
    c.execute("""INSERT INTO CLASSES (CLASSID, NAME, INSTRUCTOR, SEMESTER)
        VALUES(?,?,?,?)""",['Python','Freddie Mac', 'Popovici', 'FALL'])
    c.execute("UPDATE CLASSES SET CLASSID='Calculus 2' where Name='Freddie Mac'")
    c.execute("UPDATE CLASSES SET INSTRUCTOR='Bruce Wayne' where Name='Freddie Mac'")
    c.execute("UPDATE CLASSES SET CLASSID='Linear Algebra' where Name='John Smith'")
    c.execute("UPDATE CLASSES SET INSTRUCTOR='Clark Kent' where Name='John Smith'")
    c.execute("DELETE FROM CLASSES WHERE NAME='John Smith'" )
    c.execute("SELECT * FROM CLASSES")
    while True:
        v=c.fetchone()
        if v is None:
            break
        print (v,"\n")
    c.close()
    dbconn.close
    
main()
