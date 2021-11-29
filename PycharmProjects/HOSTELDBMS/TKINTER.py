#FrontEnd

from tkinter import *
import tkinter.messagebox
import stdDatabase_BackEnd

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student database system")
        self.root.config(bg="snow3")
        self.root.geometry("1350x720+0+0")

        StdID = StringVar()
        Firstname = StringVar()
        Lastname = StringVar()
        Dob = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Adress = StringVar()
        Mobile = StringVar()
        Roomno = StringVar()
        Blockno = StringVar()
        Course = StringVar()
        # =============================================================Functions===============================================================
        def iExit():
            iExit = tkinter.messagebox.askyesno("Hostel Database Management System","Do you want to Exit the program?")
            if iExit>0:
                root.destroy()
                return


        def Stdrec(event):
            global sd
            searchstd = studentlist.curselection()[0]
            sd = studentlist.get(searchstd)

            self.txtStdID.delete(0, END)
            self.txtStdID.insert(END,sd[1])
            self.txtFna.delete(0, END)
            self.txtFna.insert(END, sd[2])
            self.txtLna.delete(0, END)
            self.txtLna.insert(END, sd[3])
            self.txtDob.delete(0, END)
            self.txtDob.insert(END, sd[4])
            self.txtAge.delete(0, END)
            self.txtAge.insert(END, sd[5])
            self.txtGender.delete(0, END)
            self.txtGender.insert(END, sd[6])
            self.txtAdress.delete(0, END)
            self.txtAdress.insert(END, sd[7])
            self.txtMobile.delete(0, END)
            self.txtMobile.insert(END, sd[8])
            self.txtroomno.delete(0, END)
            self.txtroomno.insert(END, sd[9])
            self.txtBlkno.delete(0, END)
            self.txtBlkno.insert(END, sd[10])
            self.txtCrs.delete(0, END)
            self.txtCrs.insert(END, sd[11])


        def cleardata():
            self.txtStdID.delete(0,END)
            self.txtFna.delete(0, END)
            self.txtLna.delete(0, END)
            self.txtDob.delete(0, END)
            self.txtAge.delete(0, END)
            self.txtGender.delete(0, END)
            self.txtAdress.delete(0, END)
            self.txtMobile.delete(0, END)
            self.txtroomno.delete(0, END)
            self.txtBlkno.delete(0, END)
            self.txtCrs.delete(0, END)

        def addData():
            if(len(StdID.get())!=0):
                stdDatabase_BackEnd.addStdRec(StdID.get(), Firstname.get() , Lastname.get() , Dob.get() , Age.get() , Gender.get() , Adress.get() ,Mobile.get(), \
                                                Roomno.get(), Blockno.get() , Course.get())
                studentlist.delete(0,END)
                studentlist.insert(END,(StdID.get(), Firstname.get() , Lastname.get() , Dob.get() , Age.get() , Gender.get() , Adress.get() ,Mobile.get(), \
                                                Roomno.get(), Blockno.get() , Course.get()))

        def DisplayData():
            studentlist.delete(0, END)
            for row in stdDatabase_BackEnd.Viewdata():
                studentlist.insert(END,row,str(""))

        def deleteData():
            if(len(StdID.get())!=0):
                stdDatabase_BackEnd.deletRec(sd[0])
                cleardata()
                DisplayData()

        def Searchdatabase():
            studentlist.delete(0,END)
            for row in stdDatabase_BackEnd.searchdata(StdID.get(), Firstname.get() , Lastname.get() , Dob.get() , Age.get() , Gender.get() , Adress.get()\
                    , Mobile.get(),Roomno.get(), Blockno.get() , Course.get()):
                studentlist.insert(END, row, str(""))
        def UpdateDatabase():
            if(len(StdID.get())!=0):
                stdDatabase_BackEnd.deletRec(sd[0])

            if (len(StdID.get()) != 0):
                stdDatabase_BackEnd.addStdRec(StdID.get(), Firstname.get(), Lastname.get(), Dob.get(), Age.get(), Gender.get(), Adress.get(), Mobile.get(), \
                                              Roomno.get(), Blockno.get(), Course.get())
                studentlist.delete(0, END)
                studentlist.insert(END, (StdID.get(), Firstname.get(), Lastname.get(), Dob.get(), Age.get(), Gender.get(), Adress.get(), Mobile.get(), \
                Roomno.get(), Blockno.get(), Course.get()))




        #=============================================================FRAMES===================================================================

        MainFrame = Frame(self.root, bg="snow3")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, padx=0, pady=0, bg="snow3", relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.canv = Canvas(TitFrame, width=250, height=70, bg='white')
        self.canv.grid(row=0,column=0)


        self.lblTit = Label(TitFrame,font= ('arial',25,'bold'),text="HOSTEL DATABASE MANAGEMENT SYSTEM", bg="snow")
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, width=1200, height=90, padx=1, pady=1, bg="snow3" ,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=18, bg="snow3", relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=500, height=500, padx=20, bg="aquamarine", relief=RIDGE,
                                   font=('arial',20,'bold'),text="Student info\n")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=500, height=600, padx=20, bg="lightgoldenrod1", relief=RIDGE,
                                   font=('arial', 20, 'bold'), text="Student Details\n")
        DataFrameRIGHT.pack(side=RIGHT)

        # ========================================================Labels and Entry Widget===================================================================

        self.lblStdID = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="SRN:", padx=1, pady=1, bg="aquamarine")
        self.lblStdID.grid( row = 0, column = 0, sticky = W)
        self.txtStdID = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=StdID, width=39)
        self.txtStdID.grid(row=0, column=1)


        self.lblFna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Name:", padx=2, pady=2,
                              bg="aquamarine")
        self.lblFna.grid(row=1, column=0, sticky=W)
        self.txtFna = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Firstname, width=39)
        self.txtFna.grid(row=1, column=1)


        self.lblLna = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Course", padx=2, pady=2,
                              bg="aquamarine")
        self.lblLna.grid(row=2, column=0, sticky=W)
        self.txtLna = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Lastname, width=39)
        self.txtLna.grid(row=2, column=1)


        self.lblDob = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="DOB:", padx=2, pady=2,
                            bg="aquamarine")
        self.lblDob.grid(row=3, column=0, sticky=W)
        self.txtDob = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Dob, width=39)
        self.txtDob.grid(row=3, column=1)


        self.lblAge = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Adress:", padx=2, pady=2,
                            bg="aquamarine")
        self.lblAge.grid(row=4, column=0, sticky=W)
        self.txtAge = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Age, width=39)
        self.txtAge.grid(row=4, column=1)


        self.lblGender = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Year:", padx=2, pady=2,
                            bg="aquamarine")
        self.lblGender.grid(row=5, column=0, sticky=W)
        self.txtGender = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Gender, width=39)
        self.txtGender.grid(row=5, column=1)


        self.lblAdress = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Parents Mobile:", padx=2, pady=2,
                            bg="aquamarine")
        self.lblAdress.grid(row=6, column=0, sticky=W)
        self.txtAdress = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Adress, width=39)
        self.txtAdress.grid(row=6, column=1)


        self.lblMobile = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Student Mobile:", padx=2, pady=2,
                            bg="aquamarine")
        self.lblMobile.grid(row=7, column=0, sticky=W)
        self.txtMobile = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Mobile, width=39)
        self.txtMobile.grid(row=7, column=1)


        self.lblroomno = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Room no:", padx=2, pady=2,
                            bg="aquamarine")
        self.lblroomno.grid(row=8, column=0, sticky=W)
        self.txtroomno = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Roomno, width=39)
        self.txtroomno.grid(row=8, column=1)


        self.lblBlkno = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Block:", padx=2, pady=2,
                            bg="aquamarine")
        self.lblBlkno.grid(row=9, column=0, sticky=W)
        self.txtBlkno = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Blockno, width=39)
        self.txtBlkno.grid(row=9, column=1)

        self.lblCrs = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Warden name:", padx=2, pady=2,
                              bg="aquamarine")
        self.lblCrs.grid(row=10, column=0, sticky=W)
        self.txtCrs = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Course, width=39)
        self.txtCrs.grid(row=10, column=1)

        # ========================================================ScrollBar and ListBox===================================================================
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')

        studentlist = Listbox(DataFrameRIGHT, width = 41 ,height = 22 , font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect>>',Stdrec)
        studentlist.grid(row=0, column=0, padx=8)
        scrollbar.config( command = studentlist.yview)

        # ========================================================Button Widget===================================================================
        self.btnAddData = Button(ButtonFrame, text="Add new", font= ('arial',12,'bold') , fg="white", bg="grey", width = 10 ,height = 1, bd=4, command = addData)
        self.btnAddData.grid(row=0, column=0, padx=10, pady=10)

        self.btnDispay = Button(ButtonFrame, text="Display", font=('arial', 12, 'bold'), fg="white", bg="grey",width=10, height=1, bd=4, command = DisplayData)
        self.btnDispay.grid(row=0, column=1, padx=10, pady=10)

        self.btnClear = Button(ButtonFrame, text="Clear", font=('arial', 12, 'bold'),fg="white", bg="grey", width=10, height=1, bd=4, command=cleardata)
        self.btnClear.grid(row=0, column=2, padx=10, pady=10)

        self.btnDelete = Button(ButtonFrame, text="Delete", font=('arial', 12, 'bold'), fg="white", bg="grey",width=10, height=1, bd=4, command =deleteData)
        self.btnDelete.grid(row=0, column=3, padx=10, pady=10)

        self.btnSearch = Button(ButtonFrame, text="Search", font=('arial', 12, 'bold'), fg="white", bg="grey",width=10, height=1, bd=4, command= Searchdatabase)
        self.btnSearch.grid(row=0, column=4, padx=10, pady=10)

        self.btnUpdate = Button(ButtonFrame, text="Update", font=('arial', 12, 'bold'),fg="white", bg="grey", width=10, height=1, bd=4, command = UpdateDatabase)
        self.btnUpdate.grid(row=0, column=5, padx=10, pady=10)

        self.btnExit = Button(ButtonFrame, text="Exit", font=('arial', 12, 'bold'), fg="white", bg="grey", width=10, height=1, bd=4 , command=iExit)
        self.btnExit.grid(row=0, column=6, padx=10, pady=10)

if __name__ =='__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()







