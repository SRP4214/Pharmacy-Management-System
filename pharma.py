from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class PharmacyManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1440x1000+0+0")

        #pharma_table varibles

        self.addmed_varref=StringVar()
        self.addmed_varn=StringVar()

        #med_table varibles 

        self.ref_var=StringVar()
        self.cn_var=StringVar()
        self.tm_var=StringVar()
        self.mn_var=StringVar()
        self.ln_var=StringVar()
        self.id_var=StringVar()
        self.ed_var=StringVar()
        self.se_var=StringVar()
        self.do_var=StringVar()
        self.sp_var=StringVar()
        self.q_var=StringVar()

        # Main title

        lbltitle=Label(self.root,text="Pharmacy Management System",bd=10,relief=RIDGE,bg="darkgreen",fg="white",font=("times new roman",50,"bold"),pady=4);
        lbltitle.pack(side=TOP,fill=X)

        # Logo

        logoimg=Image.open("/Users/shivpatel/Desktop/SRP/DBMSIN/pharmalogo.png")
        logoimg=logoimg.resize((80,70),Image.ANTIALIAS)
        self.photologoimg=ImageTk.PhotoImage(logoimg)
        b1=Button(self.root,image=self.photologoimg,borderwidth=0)
        b1.place(x=10,y=10)

        # UpperDataFrame

        DataFrame=Frame(self.root,bd=5,relief=RIDGE,padx=5,bg="white")
        DataFrame.place(x=0,y=100,width=1440,height=400)

        # UpperLDataFrame

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",fg="darkgreen",font=("times new roman",20,"bold"),bg="white")
        DataFrameLeft.place(x=0,y=0,width=800,height=380)

        # Labels And Entry for data

        lblrno=Label(DataFrameLeft,font=("times new roman",20,"bold"),text="Reference No:",padx=5,bg="white",fg="black")
        lblrno.grid(row=0,column=0,sticky=W)

        conn = mysql.connector.connect(host='localhost', username='root', password='Shiv@1608', database='dbmsin')
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT refno from pharma_table")
        row=my_cursor.fetchall()


        ref_combo=ttk.Combobox(DataFrameLeft,width=25,textvariable=self.ref_var,font=("times new roman",12,"bold"),state="readonly")
        ref_combo["values"]=row
        ref_combo.grid(row=0,column=1)
        if (len(row)!=0):
            ref_combo.current(0)

        lblcn=Label(DataFrameLeft,font=("times new roman",20,"bold"),text="Company Name:",padx=5,bg="white",fg="black")
        lblcn.grid(row=1,column=0,sticky=W)

        txtcn=Entry(DataFrameLeft,textvariable=self.cn_var,relief=RIDGE,font=("times new roman",15,"bold"),width=21,borderwidth=0,bg="white",fg="black")
        txtcn.grid(row=1,column=1)

        lbltom=Label(DataFrameLeft,font=("times new roman",20,"bold"),text="Type of Medicine:",padx=5,bg="white",fg="black")
        lbltom.grid(row=2,column=0,sticky=W)

        tom_combo=ttk.Combobox(DataFrameLeft,textvariable=self.tm_var,width=25,font=("times new roman",12,"bold"),state="readonly")
        tom_combo["values"]=("Tablets","Injection","Capsules","Liquid","Drops")
        tom_combo.grid(row=2,column=1)
        tom_combo.current(0)

        lblmn=Label(DataFrameLeft,font=("times new roman",20,"bold"),text="Medicine Name:",padx=5,bg="white",fg="black")
        lblmn.grid(row=3,column=0,sticky=W)

        conn = mysql.connector.connect(host='localhost', username='root', password='Shiv@1608', database='dbmsin')
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT medname FROM pharma_table")
        row=my_cursor.fetchall()

        mn_combo=ttk.Combobox(DataFrameLeft,textvariable=self.mn_var,width=25,font=("times new roman",12,"bold"),state="readonly")
        mn_combo["values"]=row
        mn_combo.grid(row=3,column=1)
        if len(row)!=0:
            mn_combo.current(0)

        lblln=Label(DataFrameLeft,font=("times new roman",20,"bold"),text="Lot No:",padx=5,bg="white",fg="black")
        lblln.grid(row=4,column=0,sticky=W)

        txtln=Entry(DataFrameLeft,relief=RIDGE,textvariable=self.ln_var,font=("times new roman",15,"bold"),width=21,borderwidth=0,bg="white",fg="black")
        txtln.grid(row=4,column=1)

        lblisd=Label(DataFrameLeft,font=("times new roman",20,"bold"),text="Issue Date:",padx=5,bg="white",fg="black")
        lblisd.grid(row=5,column=0,sticky=W)

        txtisd=Entry(DataFrameLeft,relief=RIDGE,textvariable=self.id_var,font=("times new roman",15,"bold"),width=21,borderwidth=0,bg="white",fg="black")
        txtisd.grid(row=5,column=1)

        lblexd=Label(DataFrameLeft,font=("times new roman",20,"bold"),text="Expiry Date:",padx=5,bg="white",fg="black")
        lblexd.grid(row=6,column=0,sticky=W)

        txtexd=Entry(DataFrameLeft,relief=RIDGE,textvariable=self.ed_var,font=("times new roman",15,"bold"),width=21,borderwidth=0,bg="white",fg="black")
        txtexd.grid(row=6,column=1)

        # lblu=Label(DataFrameLeft,font=("times new roman",20,"bold"),text="Uses:",padx=5,bg="white",fg="black")
        # lblu.grid(row=7,column=0,sticky=W)

        # txtu=Entry(DataFrameLeft,relief=RIDGE,font=("times new roman",15,"bold"),width=21,borderwidth=0,bg="white",fg="black")
        # txtu.grid(row=8,column=1)

        lblse=Label(DataFrameLeft,font=("times new roman",20,"bold"),text="Side effects:",padx=5,bg="white",fg="black")
        lblse.grid(row=7,column=0,sticky=W)

        txtse=Entry(DataFrameLeft,relief=RIDGE,textvariable=self.se_var,font=("times new roman",15,"bold"),width=21,borderwidth=0,bg="white",fg="black")
        txtse.grid(row=7,column=1)

        lbldo=Label(DataFrameLeft,font=("times new roman",20,"bold"),text="Dosage:",padx=5,bg="white",fg="black")
        lbldo.grid(row=8,column=0,sticky=W)

        txtdo=Entry(DataFrameLeft,textvariable=self.do_var,relief=RIDGE,font=("times new roman",15,"bold"),width=21,borderwidth=0,bg="white",fg="black")
        txtdo.grid(row=8,column=1)

        lblsp=Label(DataFrameLeft,font=("times new roman",20,"bold"),text="Selling Price:",padx=5,bg="white",fg="black")
        lblsp.grid(row=9,column=0,sticky=W)

        txtsp=Entry(DataFrameLeft,textvariable=self.sp_var,relief=RIDGE,font=("times new roman",15,"bold"),width=21,borderwidth=0,bg="white",fg="black")
        txtsp.grid(row=9,column=1)


        lblq=Label(DataFrameLeft,font=("times new roman",20,"bold"),text="Quantity:",padx=5,bg="white",fg="black")
        lblq.grid(row=10,column=0,sticky=W)

        txtq=Entry(DataFrameLeft,relief=RIDGE,textvariable=self.q_var,font=("times new roman",15,"bold"),width=21,borderwidth=0,bg="white",fg="black")
        txtq.grid(row=10,column=1)

        img1=Image.open("/Users/shivpatel/Desktop/SRP/DBMSIN/img4.png")
        img1=img1.resize((330,330),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(DataFrameLeft,image=self.photoimg1,borderwidth=0)
        b1.place(x=410,y=0)

        # UpperRDataFrame

        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Addition",fg="darkgreen",font=("times new roman",20,"bold"),bg="white")
        DataFrameRight.place(x=810,y=0,width=600,height=380)

        lblrf1=Label(DataFrameRight,font=("times new roman",20,"bold"),text="Referance No:",padx=5,bg="white",fg="black")
        lblrf1.grid(row=0,column=0,sticky=W)
        lblrf2=Label(DataFrameRight,font=("times new roman",10),text="(Ref NOT req while adding medicine)",padx=5,bg="white",fg="black")
        lblrf2.grid(row=1,column=0,sticky=W)

        txtrf1=Entry(DataFrameRight,textvariable=self.addmed_varref,relief=RIDGE,font=("times new roman",15,"bold"),width=21,borderwidth=0,bg="white",fg="black")
        txtrf1.grid(row=0,column=1)
    
        lblmn1=Label(DataFrameRight,font=("times new roman",20,"bold"),text="Medicine Name:",padx=5,bg="white",fg="black")
        lblmn1.grid(row=2,column=0,sticky=W)

        txtmn1=Entry(DataFrameRight,textvariable=self.addmed_varn,relief=RIDGE,font=("times new roman",15,"bold"),width=21,borderwidth=0,bg="white",fg="black")
        txtmn1.grid(row=2,column=1)

        img2=Image.open("img3.jpg")
        img2=img2.resize((200,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(DataFrameRight,image=self.photoimg2,borderwidth=0)
        b1.place(x=350,y=5)
        
        #side_frame

        sideFrame=Frame(DataFrameRight,bd=5,relief=RIDGE);
        sideFrame.place(x=0,y=80,width=330,height=250)

        sc_x=ttk.Scrollbar(sideFrame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(sideFrame,orient=HORIZONTAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.medicine_table=ttk.Treeview(sideFrame,column=("refno","medname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("refno",text="Referance No.")
        self.medicine_table.heading("medname",text="Medicine Name")

        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)

        self.medicine_table.column("refno",width=100)
        self.medicine_table.column("medname",width=100)

        self.medicine_table.bind("<ButtonRelease-1>",self.medget)

        #Buttons in UpperRDataFrame
        ButtonFrame1=Frame(DataFrameRight,bd=5,relief=RIDGE,bg="darkgreen")
        ButtonFrame1.place(x=350,y=180,width=200,height=145)

        Addbtn1=Button(ButtonFrame1,text="ADD MEDICINE",font=("times new roman",15,"bold"),borderwidth=0,width=20,foreground="darkblue",pady=5)
        Addbtn1.grid(row=0,column=0)
        Addbtn1.config(command=self.Addmed)

        Updbtn1=Button(ButtonFrame1,text="UPDATE MEDICINE",font=("times new roman",15,"bold"),borderwidth=0,width=20,foreground="darkblue",pady=5)
        Updbtn1.grid(row=1,column=0)
        Updbtn1.config(command=self.Update)

        Delbtn1=Button(ButtonFrame1,text="DELETE MEDICINE",font=("times new roman",15,"bold"),borderwidth=0,width=20,foreground="darkblue",pady=5)
        Delbtn1.grid(row=2,column=0)
        Delbtn1.config(command=self.Deletem)

        Clrbtn1=Button(ButtonFrame1,text="CLEAR MEDICINE",font=("times new roman",15,"bold"),borderwidth=0,width=20,foreground="darkblue",pady=5)
        Clrbtn1.grid(row=4,column=0)
        Clrbtn1.config(command=self.Clrmed)

       
    
            
        # ButtonSection

        ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20,bg="darkgreen")
        ButtonFrame.place(x=0,y=500,width=1440,height=60)

        Addbtn=Button(ButtonFrame,text="ADD",font=("times new roman",15,"bold"),borderwidth=0,padx=5,width=12)
        Addbtn.grid(row=0,column=0)
        Addbtn.config(command=self.Add)
        Updbtn=Button(ButtonFrame,text="UPDATE",font=("times new roman",15,"bold"),width=12,borderwidth=0,padx=5)
        Updbtn.grid(row=0,column=1)
        Updbtn.config(command=self.Update1)
        Delbtn=Button(ButtonFrame,text="DELETE",font=("times new roman",15,"bold"),borderwidth=0,width=12,foreground="red")
        Delbtn.config(command=self.Delete)
        Delbtn.grid(row=0,column=2)
        Resbtn=Button(ButtonFrame,text="RESET",font=("times new roman",15,"bold"),borderwidth=0,width=12)
        Resbtn.grid(row=0,column=3)
        Resbtn.config(command=self.reset)
        Exibtn=Button(ButtonFrame,text="EXIT",command=self.exit,font=("times new roman",15,"bold"),borderwidth=0,width=12,foreground="red")
        Exibtn.grid(row=0,column=4)

        #variables
        self.search_var=StringVar()
        lblsearch=Label(ButtonFrame,text="Search By",bd=0,relief=RIDGE,fg="darkgreen",bg="white",font=("times new roman",18,"bold"),padx=20);
        lblsearch.grid(row=0,column=5,sticky=W)

        search_combo=ttk.Combobox(ButtonFrame,textvariable=self.search_var,width=15,font=("times new roman",15,"bold"),state="readonly")
        search_combo["values"]=("Refno","Medname","Lotno")
        search_combo.grid(row=0,column=6)
        search_combo.current(0);
        self.searchtxt_var=StringVar()
        txtsearch=Entry(ButtonFrame,textvariable=self.searchtxt_var,relief=RIDGE,width=15,font=("times new roman",15,"bold"))
        txtsearch.grid(row=0,column=7)

        Seabtn=Button(ButtonFrame,text="SEARCH",font=("times new roman",15,"bold"),width=15,borderwidth=0,padx=5)
        Seabtn.grid(row=0,column=8)
        Seabtn.config(command=self.search_data)
        shobtn=Button(ButtonFrame,text="SHOW ALL",font=("times new roman",15,"bold"),width=15,borderwidth=0,padx=5)
        shobtn.grid(row=0,column=9)
        shobtn.config(command=self.Fetch)

        #Bottom Frame

        DataFrameBottom=Frame(self.root,bd=5,relief=RIDGE,padx=5,bg="white")
        DataFrameBottom.place(x=0,y=570,width=1440,height=250)

        #maintable
        DataFrameTable=Frame(DataFrameBottom,bd=5,relief=RIDGE,padx=5,bg="white")
        DataFrameTable.place(x=0,y=0,width=1420,height=240)

        sc_x=ttk.Scrollbar(DataFrameTable,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(DataFrameTable,orient=HORIZONTAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.pharma_table=ttk.Treeview(DataFrameTable,column=("refno","companyname","type","medname","lotno","isd","exd","se","do","sp","q"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)

        sc_x.config(command=self.pharma_table.xview)
        sc_y.config(command=self.pharma_table.yview)

        self.pharma_table["show"]="headings"
        self.pharma_table.pack(fill=BOTH,expand=1)

        self.pharma_table.heading("refno",text="Referance No.")
        self.pharma_table.heading("companyname",text="Company Name")
        self.pharma_table.heading("type",text="Medicine Type")
        self.pharma_table.heading("medname",text="Medicine Name")
        self.pharma_table.heading("lotno",text="Lot No.")
        self.pharma_table.heading("isd",text="Issue Date")
        self.pharma_table.heading("exd",text="Expiry Date")
        self.pharma_table.heading("se",text="Side Effect")
        self.pharma_table.heading("do",text="Dosage")
        self.pharma_table.heading("sp",text="Selling price")
        self.pharma_table.heading("q",text="Quantity")

        self.pharma_table.column("refno",width=100)
        self.pharma_table.column("companyname",width=100)
        self.pharma_table.column("type",width=100)
        self.pharma_table.column("medname",width=100)
        self.pharma_table.column("lotno",width=100)
        self.pharma_table.column("isd",width=100)
        self.pharma_table.column("exd",width=100)
        self.pharma_table.column("se",width=100)
        self.pharma_table.column("do",width=100)
        self.pharma_table.column("sp",width=100)
        self.pharma_table.column("q",width=100)
        self.fetch_data()
        self.Fetch()
        self.pharma_table.bind("<ButtonRelease-1>",self.med_get)

    # medicine function in pharma_table
    def Addmed(self):
   
        conn = mysql.connector.connect(host='localhost', username='root', password='Shiv@1608', database='dbmsin')
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT MAX(refno) FROM pharma_table")
        max_refno = my_cursor.fetchone()[0]

        
        if max_refno:
            new_refno = max_refno + 1  
        else:
            new_refno = 1  
        
        try:
            my_cursor.execute("INSERT INTO pharma_table(refno, medname) VALUES (%s, %s)", (new_refno, self.addmed_varn.get()))
            conn.commit()
            self.fetch_data()
            self.medget()
            messagebox.showinfo("Success", "Successfully added medicine")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", "Failed to add medicine: {err}")
        finally:
            conn.close()

    def fetch_data(self):
   
        conn = mysql.connector.connect(host='localhost', username='root', password='Shiv@1608', database='dbmsin')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from pharma_table")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in rows:
                self.medicine_table.insert("",END,values=i)
            conn.commit
        conn.close()
    
    def medget(self,event=""):
        cursor_row=self.medicine_table.focus()
        content=self.medicine_table.item(cursor_row)
        row=content["values"]
        self.addmed_varref.set(row[0])
        self.addmed_varn.set(row[1])

    def Update(self):
        
        if self.addmed_varn.get() == "":
            messagebox.showerror("Error", "Fields are required")
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='Shiv@1608', database='dbmsin')
                my_cursor = conn.cursor()
                my_cursor.execute("UPDATE pharma_table SET medname=%s WHERE refno=%s", (self.addmed_varn.get(), self.addmed_varref.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Medicines are updated")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Failed to update medicine: {err}")

    def Deletem(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='Shiv@1608', database='dbmsin')
        my_cursor = conn.cursor()
        my_cursor.execute("DELETE FROM pharma_table WHERE refno=%s", ( self.addmed_varref.get(),)
                          )
        conn.commit()
        messagebox.showinfo("Success","Data Deleted Successfully")
        self.fetch_data()
        conn.close()

    def Clrmed(self):   
        self.addmed_varref.set("")
        self.addmed_varn.set("")

    # medicine function in med_table
    
    def Add(self):
        if self.ref_var.get()=="" or self.ln_var=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn = mysql.connector.connect(host='localhost', username='root', password='Shiv@1608', database='dbmsin')
            my_cursor = conn.cursor()

            my_cursor.execute("INSERT INTO med_table(Refno,Cmpname,Typemed,Medname,Lotno,IssueDate,ExpDate,SideEffect,Dosage,SellingPrice,Quantity) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.ref_var.get(),self.cn_var.get(),self.tm_var.get(),self.mn_var.get(),self.ln_var.get(),self.id_var.get(),self.ed_var.get(),self.se_var.get(),self.do_var.get(),self.sp_var.get(),self.q_var.get()
            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Data added")
            self.Fetch()

    def Fetch(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='Shiv@1608', database='dbmsin')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from med_table")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.pharma_table.delete(*self.pharma_table.get_children())
            for i in rows:
                self.pharma_table.insert("",END,values=i)
            conn.commit
        conn.close()

    def med_get(self,event=""):
        cursor_row=self.pharma_table.focus()
        content=self.pharma_table.item(cursor_row)
        row=content["values"]
        self.ref_var.set(row[0])
        self.cn_var.set(row[1])
        self.tm_var.set(row[2])
        self.mn_var.set(row[3])
        self.ln_var.set(row[4])
        self.id_var.set(row[5])
        self.ed_var.set(row[6])
        self.se_var.set(row[7])
        self.do_var.set(row[8])
        self.sp_var.set(row[9])
        self.q_var.set(row[10])

    def Update1(self):
        
        if self.ref_var.get() == "":
            messagebox.showerror("Error", "Fields are required")
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='Shiv@1608', database='dbmsin')
                my_cursor = conn.cursor()
                my_cursor.execute("UPDATE med_table SET Cmpname=%s,Typemed=%s,Medname=%s,Lotno=%s,IssueDate=%s,ExpDate=%s,SideEffect=%s,Dosage=%s,SellingPrice=%s,Quantity=%s WHERE Refno=%s", (
                    self.cn_var.get(),self.tm_var.get(),self.mn_var.get(),self.ln_var.get(),self.id_var.get(),self.ed_var.get(),self.se_var.get(),self.do_var.get(),self.sp_var.get(),self.q_var.get(),self.ref_var.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Medicines are updated")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Failed to update medicine: {err}")
        self.Fetch()

    def Delete(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='Shiv@1608', database='dbmsin')
        my_cursor = conn.cursor()
        my_cursor.execute("DELETE FROM med_table WHERE Refno=%s", ( self.ref_var.get(),)
                          )
        conn.commit()
        messagebox.showinfo("Success","Data Deleted Successfully")
        self.Fetch()
        conn.close()
    def exit(self):
        root.destroy()
    def reset(self):
        self.cn_var.set(""),
        self.ln_var.set(""),
        self.id_var.set(""),
        self.ed_var.set(""),
        self.se_var.set(""),
        self.do_var.set(""),
        self.sp_var.set(""),
        self.q_var.set("")

    def search_data(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='Shiv@1608', database='dbmsin')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from med_table where "+str(self.search_var.get())+" LIKE "+str(self.searchtxt_var.get()))

        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.pharma_table.delete(*self.pharma_table.get_children())
            for i in rows:
                self.pharma_table.insert("",END,values=i)
            conn.commit()
        conn.close()  


if __name__=="__main__":
    root=Tk()
    obj=PharmacyManagementSystem(root)
    root.mainloop()
