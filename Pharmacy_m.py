from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


class PharmacyManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1300x600+0+0")


        #addMed variable
        self.addmed_var=StringVar()
        self.refMed_var=StringVar()

        #main variable
        self.ref_var=StringVar()
        self.cmpName_var=StringVar()
        self.typeMed_var=StringVar()
        self.medName_var=StringVar()
        self.lot_var=StringVar()
        self.issuedate_var=StringVar()
        self.expdate_var=StringVar()
        self.uses_var=StringVar()
        self.sideEffect_var=StringVar()
        self.warning_var=StringVar()
        self.dosage_var=StringVar()
        self.price_var=StringVar()
        self.product_var=StringVar()


        lbltitle = Label(self.root,text=" PHARMACY MANAGEMENT SYSTEM",bd=10,relief=RIDGE,
                         bg="white",fg="darkgreen",font=("times new roman",45,"bold"),padx=2,pady=4)
        
        lbltitle.pack(side=TOP,fill=X)


        img1=Image.open("logo.jpg")
        img1 = img1.resize((70, 70), Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=30,y=12)

        #datafram
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=1350,height=380)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",fg="darkgreen",
                                 font=("arial",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=800,height=335)

        

        #buuton frame
        ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=500,width=1350,height=65)

        #main button
        btnAddData=Button(ButtonFrame,command=self.add_data,text="Medicine Add",font=("arial",10,"bold"),width=14,bg="darkgreen",fg="white")
        btnAddData.grid(row=0,column=0)

        btnUpdateMed=Button(ButtonFrame,command=self.update_data,text="UPDATE",font=("arial",10,"bold"),width=14,bg="darkgreen",fg="white")
        btnUpdateMed.grid(row=0,column=1)

        btnDeleteMed=Button(ButtonFrame,command=self.delete,text="DELETE",font=("arial",10,"bold"),width=14,bg="red",fg="white")
        btnDeleteMed.grid(row=0,column=2)

        btnRestMed=Button(ButtonFrame,command=self.reset,text="RESET",font=("arial",10,"bold"),width=14,bg="darkgreen",fg="white")
        btnRestMed.grid(row=0,column=3)

        btnExitMed=Button(ButtonFrame,text="EXIT",font=("arial",10,"bold"),width=14,bg="darkgreen",fg="white")
        btnExitMed.grid(row=0,column=4)

        #search By
        lblSearch=Label(ButtonFrame,font=("arial",15,"bold"),text="Search By",padx=12,bg="red",fg="white")
        lblSearch.grid(row=0,column=5,sticky=W)

        #Variable
        self.search_var=StringVar()

        search_combo=ttk.Combobox(ButtonFrame,textvariable=self.search_var,width=12,font=("arial",10,"bold"),state="readonly")
        search_combo["values"]=("Ref_No","MedName")
        search_combo.grid(row=0,column=6)
        search_combo.current(0)

        self.searchTxt_var=StringVar()
        txtSearch=Entry(ButtonFrame,textvariable=self.searchTxt_var,bd=3,relief=RIDGE,width=12,font=("arial",17,"bold"))
        txtSearch.grid(row=0,column=7)

        searchbtn=Button(ButtonFrame,command=self.search_data,text="SEARCH",font=("arial",10,"bold"),width=13,bg="darkgreen",fg="white")
        searchbtn.grid(row=0,column=8)

        showAll=Button(ButtonFrame,command=self.fetch_data,text="SHOW ALL",font=("arial",10,"bold"),width=13,bg="darkgreen",fg="white")
        showAll.grid(row=0,column=9)

        #label and entry
        
        conn=mysql.connector.connect(host="localhost",username="root",password="Razaq087088",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select Ref from pharma")
        row = my_cursor.fetchall()

        lblrefno=Label(DataFrameLeft,font=("arial",12,"bold"),text="Reference No",padx=2)
        lblrefno.grid(row=0,column=0,sticky=W)

        comrefno=ttk.Combobox(DataFrameLeft,textvariable=self.ref_var,width=27,font=("arial",10,"bold"),state="readonly")
        comrefno["values"]=row
        comrefno.grid(row=0,column=1)
        comrefno.current(0)

        lblCmpName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Company Name:",padx=2,pady=6)
        lblCmpName.grid(row=1,column=0,sticky=W)
        txtCmpName=Entry(DataFrameLeft,textvariable=self.cmpName_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=23)
        txtCmpName.grid(row=1,column=1)

        lblTypeOfMedicine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Type Of Medicine",padx=2,pady=6)
        lblTypeOfMedicine.grid(row=2,column=0,sticky=W)

        comboTypeOfMedicine=ttk.Combobox(DataFrameLeft,textvariable=self.typeMed_var,state="readonly",font=("arial",10,"bold"),width=27)
        comboTypeOfMedicine["values"]=("Tablet","Liquid","Syrup","Capsule","Drops","Inhales","Injection")
        comboTypeOfMedicine.grid(row=2,column=1)
        comboTypeOfMedicine.current(0)

        #add midicine
        lblMedicineName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Medicine Name",padx=2,pady=6)
        lblMedicineName.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="Razaq087088",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select MedName from pharma")
        med = my_cursor.fetchall()

        comboMedicineName=ttk.Combobox(DataFrameLeft,textvariable=self.medName_var,state="readonly",font=("arial",10,"bold"),width=27)
        comboMedicineName["values"]=med
        comboMedicineName.grid(row=3,column=1)
        comboMedicineName.current(0)
        

        lblLotNo=Label(DataFrameLeft,font=("arial",12,"bold"),text="Lot No:",padx=2,pady=6)
        lblLotNo.grid(row=4,column=0,sticky=W)
        txtLotNo=Entry(DataFrameLeft,textvariable=self.lot_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=23)
        txtLotNo.grid(row=4,column=1)

        lblIssueDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataFrameLeft,textvariable=self.issuedate_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=23)
        txtIssueDate.grid(row=5,column=1)

        lblExpDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataFrameLeft,textvariable=self.expdate_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=23)
        txtExpDate.grid(row=6,column=1)

        lblUses=Label(DataFrameLeft,font=("arial",12,"bold"),text="Uses:",padx=2,pady=4)
        lblUses.grid(row=7,column=0,sticky=W)
        txtUses=Entry(DataFrameLeft,textvariable=self.uses_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=23)
        txtUses.grid(row=7,column=1)

        lblSideEffect=Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataFrameLeft,textvariable=self.sideEffect_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=23)
        txtSideEffect.grid(row=8,column=1)

        lblPrecWarning=Label(DataFrameLeft,font=("arial",12,"bold"),text="Prec&Warning:",padx=15)
        lblPrecWarning.grid(row=0,column=2,sticky=W)
        txtPrecWarning=Entry(DataFrameLeft,textvariable=self.warning_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtPrecWarning.grid(row=0,column=3)

        lblDosage=Label(DataFrameLeft,font=("arial",12,"bold"),text="Dosage:",padx=15)
        lblDosage.grid(row=1,column=2,sticky=W)
        txtDosage=Entry(DataFrameLeft,textvariable=self.dosage_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtDosage.grid(row=1,column=3)

        lblPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Tablet Price:",padx=15)
        lblPrice.grid(row=2,column=2,sticky=W)
        txtPrice=Entry(DataFrameLeft,textvariable=self.price_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtPrice.grid(row=2,column=3)

        lblProductQT=Label(DataFrameLeft,font=("arial",12,"bold"),text="Product QT:",padx=15)
        lblProductQT.grid(row=3,column=2,sticky=W)
        txtProductQT=Entry(DataFrameLeft,textvariable=self.product_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtProductQT.grid(row=3,column=3)

        #Data frame right
        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add Department",fg="darkgreen",
                                 font=("arial",12,"bold"))
        DataFrameRight.place(x=810,y=5,width=450,height=335)

        lblrefno=Label(DataFrameRight,font=("arial",12,"bold"),text="Refrence No:",padx=15,pady=6)
        lblrefno.grid(row=3,column=2,sticky=W)
        txtrefno=Entry(DataFrameRight,textvariable=self.refMed_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtrefno.grid(row=3,column=3)

        lblmedName=Label(DataFrameRight,font=("arial",12,"bold"),text="Medicine Name:",padx=15,pady=6)
        lblmedName.grid(row=4,column=2,sticky=W)
        txtmedName=Entry(DataFrameRight,textvariable=self.addmed_var,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=20)
        txtmedName.grid(row=4,column=3)

        #side frame
        side_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=0,y=120,width=250,height=160)

        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.medicine_table=ttk.Treeview(side_frame,columns=("ref","medname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref",text="Ref")
        self.medicine_table.heading("medname",text="Medicine Name")

        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)

        self.medicine_table.column("ref",width=100)
        self.medicine_table.column("medname",width=100)

        self.medicine_table.bind("<ButtonRelease-1>",self.Medget_cursor)

        #medicine add buttons
        down_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="darkgreen")
        down_frame.place(x=260,y=120,width=135,height=145)

        btnAddmed=Button(down_frame,command=self.AddMed,text="Add",font=("arial",10,"bold"),width=15,bg="lime",fg="white",pady=4)
        btnAddmed.grid(row=0,column=0)

        btnUpdatemed=Button(down_frame,command=self.UpdateMed,text="UPDATE",font=("arial",10,"bold"),width=15,bg="purple",fg="white",pady=4)
        btnUpdatemed.grid(row=1,column=0)

        btnDeleltemed=Button(down_frame,command=self.DeleteMed,text="DELETE",font=("arial",10,"bold"),width=15,bg="red",fg="white",pady=4)
        btnDeleltemed.grid(row=2,column=0)


        btnclearmed=Button(down_frame,command=self.ClearMed,text="CLEAR",font=("arial",10,"bold"),width=15,bg="orange",fg="white",pady=4)
        btnclearmed.grid(row=3,column=0)


        #frame details
        Framedetails=Frame(self.root,bd=15,relief=RIDGE)
        Framedetails.place(x=0,y=560,width=1350,height=165)

        #main  table and scroll bar
        Table_frame=Frame(Framedetails,bd=15,relief=RIDGE,padx=20)
        Table_frame.place(x=0,y=1,width=1400,height=150)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        

        self.pharmacy_table=ttk.Treeview(Table_frame,columns=("reg","companyname","type","tablename","lotno","issuedata","expdate","uses"
                                                              ,"sideeffect","warning","dosage","price","productqt")
                                                              ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table["show"]="headings"

        self.pharmacy_table.heading("reg", text="Reference No")
        self.pharmacy_table.heading("companyname", text="Company Name")
        self.pharmacy_table.heading("type", text="Type of Medicine")
        self.pharmacy_table.heading("tablename", text="Medicine Name")
        self.pharmacy_table.heading("lotno", text="Lot No")
        self.pharmacy_table.heading("issuedata", text="Issue Date")
        self.pharmacy_table.heading("expdate", text="Exp Date")
        self.pharmacy_table.heading("uses", text="Uses")
        self.pharmacy_table.heading("sideeffect", text="Side Effect")
        self.pharmacy_table.heading("warning", text="Price & Warning")
        self.pharmacy_table.heading("dosage", text="Dosage")
        self.pharmacy_table.heading("price", text="Price")
        self.pharmacy_table.heading("productqt", text="Product Qts")
        self.pharmacy_table.pack(fill=BOTH,expand=1)

        
        self.pharmacy_table.column("reg",width=100)
        self.pharmacy_table.column("companyname",width=100)
        self.pharmacy_table.column("type",width=100)
        self.pharmacy_table.column("tablename",width=100)
        self.pharmacy_table.column("lotno",width=100)
        self.pharmacy_table.column("issuedata",width=100)
        self.pharmacy_table.column("expdate",width=100)
        self.pharmacy_table.column("uses",width=100)
        self.pharmacy_table.column("sideeffect",width=100)
        self.pharmacy_table.column("warning",width=100)
        self.pharmacy_table.column("dosage",width=100)
        self.pharmacy_table.column("price",width=100)
        self.pharmacy_table.column("productqt",width=100)
        
        self.fetch_dataMed()
        self.fetch_data()
        self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        



    #add medicine fumctionality declaration

    def AddMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Razaq087088",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into pharma(Ref,MedName) values(%s,%s)",(
                                                                             self.refMed_var.get(),
                                                                             self.addmed_var.get(),


                                                                 ))
        conn.commit()
        self.fetch_dataMed()
        self.Medget_cursor()
        conn.close()
        messagebox.showinfo("Success","Medicine Added")


    def fetch_dataMed(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Razaq087088",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharma")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in rows:
                self.medicine_table.insert("",END,values=i)
            conn.commit() 
        conn.close()   
        
        #MedGetCursor
    def Medget_cursor(self,event=""):
        cursor_row=self.medicine_table.focus()
        content=self.medicine_table.item(cursor_row)
        row=content["values"]
        self.refMed_var.set(row[0])
        self.addmed_var.set(row[1])

    
    def UpdateMed(self):
        if self.refMed_var.get()=="" or self.addmed_var.get()=="":
            messagebox.showerror("error","all fields are requird")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Razaq087088",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("update pharma set MedName=%s where Ref=%s",(
                                                                            self.addmed_var.get(),
                                                                            self.refMed_var.get(),
                                                                        ))
            conn.commit()
            self.fetch_dataMed()
            conn.close()
            messagebox.showinfo("success","Medicine has been updated")



    def DeleteMed(self):
        
        conn=mysql.connector.connect(host="localhost",username="root",password="Razaq087088",database="mydata")
        my_cursor=conn.cursor()

        sql="delete from pharma where Ref=%s"
        val=(self.refMed_var.get(),)
        my_cursor.execute(sql,val)
        conn.commit()
        self.fetch_dataMed()
        conn.close()
        messagebox.showinfo("success","Medicine has been Delete")


    def ClearMed(self):
        self.refMed_var.set("")
        self.addmed_var.set("")

        #main table

    def add_data(self):
        if self.ref_var.get()=="" or self.lot_var.get()=="":
            messagebox.showerror("Error","All fields are required.")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Razaq087088",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into pharmacy values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                
                                                                                                self.ref_var.get(),
                                                                                                self.cmpName_var.get(),
                                                                                                self.typeMed_var.get(),
                                                                                                self.medName_var.get(),
                                                                                                self.lot_var.get(),
                                                                                                self.issuedate_var.get(),
                                                                                                self.expdate_var.get(),
                                                                                                self.uses_var.get(),
                                                                                                self.sideEffect_var.get(),
                                                                                                self.warning_var.get(),
                                                                                                self.dosage_var.get(),
                                                                                                self.price_var.get(),
                                                                                                self.product_var.get(),
                                                                                                ))  
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","data has been inserted.")

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Razaq087088",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharmacy")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in rows:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    
    def get_cursor(self, ev=""):
        cursor_row=self.pharmacy_table.focus()
        content=self.pharmacy_table.item(cursor_row)
        row=content['values']
    
        self.ref_var.set(row[0]),
        self.cmpName_var.set(row[1]),
        self.typeMed_var.set(row[2]),
        self.medName_var.set(row[3]),
        self.lot_var.set(row[4]),
        self.issuedate_var.set(row[5]),
        self.expdate_var.set(row[6]),
        self.uses_var.set(row[7]),
        self.sideEffect_var.set(row[8]),
        self.warning_var.set(row[9]),
        self.dosage_var.set(row[10]),
        self.price_var.set(row[11]),
        self.product_var.set(row[12])
     
        
    def update_data(self):
        if self.ref_var.get()=="" or self.lot_var.get()=="":
            messagebox.showerror("error","all fields are requird")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Razaq087088",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("update pharmacy set cmpName=%s,Type=%s,medname=%s,lot=%s,issuedate=%s,expdate=%s,uses=%s,sideeffect=%s,warning=%s,dosage=%s,price=%s,product=%s where Ref_No=%s",(
                                                                            
                                                                                                                                                                                                self.cmpName_var.get(),
                                                                                                                                                                                                self.typeMed_var.get(),
                                                                                                                                                                                                self.medName_var.get(),
                                                                                                                                                                                                self.lot_var.get(),
                                                                                                                                                                                                self.issuedate_var.get(),
                                                                                                                                                                                                self.expdate_var.get(),
                                                                                                                                                                                                self.uses_var.get(),
                                                                                                                                                                                                self.sideEffect_var.get(),
                                                                                                                                                                                                self.warning_var.get(),
                                                                                                                                                                                                self.dosage_var.get(),
                                                                                                                                                                                                self.price_var.get(),
                                                                                                                                                                                                self.product_var.get(),
                                                                                                                                                                                                self.ref_var.get()
                                                                                                                                                                                                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Record has been updated successfully")
        
        

    def delete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Razaq087088",database="mydata")
        my_cursor=conn.cursor()

        sql="delete from pharmacy where Ref_No=%s"
        val=(self.ref_var.get(),)
        my_cursor.execute(sql,val)

        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("deleted","Info deleted successfully")

    def reset(self):
        #self.ref_var.set(""),
        self.cmpName_var.set(""),
        #self.typeMed_var.set(""),
        #self.medName_var.set(""),
        self.lot_var.set(""),
        self.issuedate_var.set(""),
        self.expdate_var.set(""),
        self.uses_var.set(""),
        self.sideEffect_var.set(""),
        self.warning_var.set(""),
        self.dosage_var.set(r""),
        self.price_var.set(r""),
        self.product_var.set(r"")


    def search_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Razaq087088",database="mydata")
        my_cursor=conn.cursor()
        query = "SELECT * FROM pharmacy WHERE {} LIKE %s".format(self.search_var.get())  
        my_cursor.execute(query, ('%' + self.searchTxt_var.get() + '%',)) 
        #my_cursor.execute("select * from pharmacy where "+str(self.search_var.get())+" LIKE '%"+str(self.searchTxt_var.get())+"%")

        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in rows:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close()



if __name__ =="__main__":
    root=Tk()
    obj=PharmacyManagementSystem(root)
    root.mainloop()
