from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkmacosx import Button
from tkinter import messagebox
import mysql.connector

class hospital():
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management system")
        self.root.geometry("1540x800+0+0")

        lbltitle=Label(self.root,text="+ HOSPITAL MANAGEMENT SYSTEM",relief=RIDGE,bd=20,fg="red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        #=====================data frame===========================
        dataframe=Frame(self.root,bd=20 ,relief=RIDGE)
        dataframe.place(x=0,y=130,width=1530,height=400)

        dataframeleft=LabelFrame(dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",15,"bold"),text="Patient Information")
        dataframeleft.place(x=0,y=5,width=980,height=350)

        dataframeright= LabelFrame(dataframe, bd=10, relief=RIDGE, padx=10, font=("times new roman", 15, "bold"),text="Prescription")
        dataframeright.place(x=990, y=5 , width=490, height=350)

        #=================buttonframe=======================

        buttonframe= Frame(self.root, bd=20, relief=RIDGE)
        buttonframe.place(x=0, y=530, width=1530, height=70)
         #=============details frame =======================

        detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        detailsframe.place(x=0, y=600, width=1530, height=190)

        # =====================data frame left===========================

        lblnametablet=Label(dataframeleft,text="Names of Tablet",font=("times new roman",15,"bold"),padx=2 ,pady=6)
        lblnametablet.grid(row=0,column=0)
        comnametablet=ttk.Combobox(dataframeleft,font=("times new roman",15,"bold"),width=33)
        comnametablet["values"]=("Nice","Corona Vacacine","Acetaminophen","Adderall","Amlodipine","Ativan")
        comnametablet.grid(row=0,column=1)

        lblref=Label(dataframeleft,text="Reference number",font=("times new roman",15,"bold"),padx=2 ,pady=6)
        lblref.grid(row=1,column=0)
        txtref=Entry(dataframeleft,font=("times new roman",15,"bold"),width=35)
        txtref.grid(row=1,column=1)

        lbld = Label(dataframeleft, text="Dose", font=("times new roman", 15, "bold"), padx=2, pady=6)
        lbld.grid(row=2, column=0)
        txtd = Entry(dataframeleft, font=("times new roman", 15, "bold"), width=35)
        txtd.grid(row=2, column=1)

        lbltablet = Label(dataframeleft, text="No of Tablets", font=("times new roman", 15, "bold"), padx=2, pady=6)
        lbltablet.grid(row=3, column=0)
        txttablet = Entry(dataframeleft, font=("times new roman", 15, "bold"), width=35)
        txttablet.grid(row=3, column=1)

        lbll = Label(dataframeleft, text="Lot", font=("times new roman", 15, "bold"), padx=2, pady=6)
        lbll.grid(row=4, column=0)
        txtl = Entry(dataframeleft, font=("times new roman", 15, "bold"), width=35)
        txtl.grid(row=4, column=1)

        lblissue = Label(dataframeleft, text="Issue Date", font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblissue.grid(row=5, column=0)
        txtissue = Entry(dataframeleft, font=("times new roman", 15, "bold"), width=35)
        txtissue.grid(row=5, column=1)

        lblexpiry = Label(dataframeleft, text="Expiry Date", font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblexpiry.grid(row=6
                    , column=0)
        txtexpiry = Entry(dataframeleft, font=("times new roman", 15, "bold"), width=35)
        txtexpiry.grid(row=6, column=1)

        lbldaily = Label(dataframeleft, text="Daily dose", font=("times new roman", 15, "bold"), padx=2, pady=6)
        lbldaily.grid(row=7, column=0)
        txtdaily = Entry(dataframeleft, font=("times new roman", 15, "bold"), width=35)
        txtdaily.grid(row=7, column=1)

        lblSide = Label(dataframeleft, text="Side Effect", font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblSide.grid(row=8, column=0)
        txtSide = Entry(dataframeleft, font=("times new roman", 15, "bold"), width=35)
        txtSide.grid(row=8, column=1)

        lblFurther = Label(dataframeleft, text="Further Information", font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblFurther.grid(row=0, column=2)
        txtFurther= Entry(dataframeleft, font=("times new roman", 15, "bold"), width=35)
        txtFurther.grid(row=0, column=3)

        lblBlood = Label(dataframeleft, text="Blood Pressure", font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblBlood.grid(row=1, column=2)
        txtBlood = Entry(dataframeleft, font=("times new roman", 15, "bold"), width=35)
        txtBlood.grid(row=1, column=3)

        lblStorage= Label(dataframeleft, text="Storage Device", font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblStorage.grid(row=2, column=2)
        txtStorage= Entry(dataframeleft, font=("times new roman", 15, "bold"), width=35)
        txtStorage.grid(row=2, column=3)

        lblMedication= Label(dataframeleft, text="Medication", font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblMedication.grid(row=3, column=2)
        txtMedication= Entry(dataframeleft, font=("times new roman", 15, "bold"), width=35)
        txtMedication.grid(row=3, column=3)

        lblPatient = Label(dataframeleft, text="Patient id", font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblPatient.grid(row=4, column=2)
        txtPatient= Entry(dataframeleft, font=("times new roman", 15, "bold"), width=35)
        txtPatient.grid(row=4, column=3)

        lblNHS = Label(dataframeleft, text="NHS number", font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblNHS .grid(row=5, column=2)
        txtNHS  = Entry(dataframeleft, font=("times new roman", 15, "bold"), width=35)
        txtNHS .grid(row=5, column=3)

        lblpa= Label(dataframeleft, text="Patient Name", font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblpa.grid(row=6, column=2)
        txtpa = Entry(dataframeleft, font=("times new roman", 15, "bold"), width=35)
        txtpa.grid(row=6, column=3)

        lblBirth = Label(dataframeleft, text="Date of Birth", font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblBirth.grid(row=7, column=2)
        txtBirth = Entry(dataframeleft, font=("times new roman", 15, "bold"), width=35)
        txtBirth.grid(row=7, column=3)

        lblAddress= Label(dataframeleft, text="Patient Address", font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblAddress.grid(row=8, column=2)
        txtAddress = Entry(dataframeleft, font=("times new roman", 15, "bold"), width=35)
        txtAddress.grid(row=8, column=3)

        #====================== data frame right====================================
        self.txtprescription=Text(dataframeright,font=("times new roman", 15, "bold"),width=55,height=17,padx=2,pady=6)
        self.txtprescription.grid(row=0,column=0)


        #=======================buttons in data frame right================================
        btnprescription=Button(buttonframe,text="Prescription",bg="black",fg="white",font=("times new roman", 15, "bold"),width=88,height=26,padx=2,pady=6)
        btnprescription.grid(row=0,column=0)

        btnprescriptiondata = Button(buttonframe, text="Prescription Data",bg="black",fg="white", font=("times new roman", 15, "bold"),width=88,height=26,padx=2,pady=6)
        btnprescriptiondata.grid(row=0, column=2)

        btnUpdate= Button(buttonframe, text="Update", bg="black",fg="white",font=("times new roman", 15, "bold"), width=88, height=26, padx=2, pady=6)
        btnUpdate.grid(row=0, column=2)

        btnDelete= Button(buttonframe, text="Delete", bg="black", fg="white",font=("times new roman", 15, "bold"), width=88, height=26, padx=2, pady=6)
        btnDelete.grid(row=0, column=3)

        btnclear = Button(buttonframe, text="Clear", bg="black", fg="white",font=("times new roman", 15, "bold"), width=88, height=26, padx=2, pady=6)
        btnclear.grid(row=0, column=4)

        btnexit = Button(buttonframe, text="Exit", bg="black", fg="white",font=("times new roman", 15, "bold"), width=88, height=26, padx=2, pady=6)
        btnexit.grid(row=0, column=5)


    #============================table=================================
    #========================scroll bar================================

        scroll_x = ttk.Scrollbar(detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(detailsframe, orient=VERTICAL)
        self.hospital_table = ttk.Treeview(detailsframe, column=("nameoftable", "ref", "dose", "nooftablets", "lot", "issuedate","expdate", "dailydose", "storage", "nhsnumber", "pname", "dob",  "address"), xscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=BOTTOM,fill=Y)
        self.hospital_table.heading("nameoftable", text="Name OF HOSPITAL")
        self.hospital_table.heading("ref", text="Reference No.")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablets", text="No Of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Date")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("address", text=" ")
        self.hospital_table["show"] = "headings"
        self.hospital_table.pack(fill=BOTH)

        self.hospital_table.column("nameoftable", width=100)



            #================================functionality==================
        def PrescriptionData(self):

            if self.Nameoftablets.get() == "":
                messagebox.showerror("Error", "All fields are required")
            else:
                conn = mysql.connector.connect(host="localhost", username="root", password="Patiala@123", database="hospital")
                ""
                my_cursor = conn.cursor()
                my_cursor.execute("insert into hospital values (%s,%,%s,%s,%s,%s,%s,%s,%s ,%s,%s ,%s ,%s)",(self.Nameoftablets.get(),self.ref.get(),self.Dose.get(),self.Lot.get(),self.Issuedate.get(), self.ExpDate.get(),self.DailyDose.get(),self.StorageAdvice.get(),self.nhsNumber.get(),self.PatientName.get()),self.DateOfBirth.get(),self.PatientAddress.get())
                conn.commit()
                conn.close()


root=Tk()
object=hospital(root)
root.mainloop()
