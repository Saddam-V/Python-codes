import sqlite3
#BackEnd

def studentdata():
    con=sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY, StdID text, Fname text, Lname text, Dob text, Age text, Gender text, Adress text, \
                Mobile text, Roomno text, Blkno text, Course text )")
    con.commit()
    con.close()

def addStdRec(StdID, Fname , Lname , Dob , Age , Gender , Adress ,Mobile, Roomno, Blkno , Course):
    studentdata()
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("INSERT INTO student VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?)", (StdID, Fname , Lname , Dob , Age , Gender , Adress ,Mobile, Roomno, Blkno , Course))
    con.commit()
    con.close()

def Viewdata():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    row=cur.fetchall()
    con.close()
    return row

def deletRec(id):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE id=?",(id,))
    con.commit()
    con.close()

def searchdata(StdID="", Fname="" , Lname="" , Dob="" , Age="" , Gender="" , Adress="" , Mobile="" , Roomno="", Blkno="" , Course=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student WHERE StdID=? OR Fname=? OR Lname=? OR Dob=? OR Age=? OR Gender=? OR Adress=? OR Mobile=? OR Roomno=? OR Blkno=? OR Course=?",\
                (StdID, Fname , Lname , Dob , Age , Gender , Adress ,Mobile, Roomno, Blkno , Course))
    row = cur.fetchall()
    con.close()
    return row

def dataUpdate(id,StdID="", Fname="" , Lname="" , Dob="" , Age="" , Gender="" , Adress="" , Mobile="" , Roomno="", Blkno="" , Course=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("UPDATE student SET StdID=? OR Fname=? OR Lname=? OR Dob=? OR Age=? OR Gender=? OR Adress=? OR Mobile=? OR Roomno=? OR Blkno=? or Course=? WHERE id=?",\
    (StdID, Fname , Lname , Dob , Age , Gender , Adress ,Mobile, Roomno, Blkno , Course,id))
    con.commit()
    con.close()
