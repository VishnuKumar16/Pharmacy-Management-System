from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
# import mysql.connector

class PharmacyManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management System") 
        self.root.geometry("1600x800")

 #======================AddMed variable=====================================================
        # self.addmed_var=StringVar()
        # self.addmed_var=StringVar()        new






        lbltitle = Label(self.root, text="PHARMACY MANAGEMENT SYSTEM", bd=15, relief=RIDGE, bg='white', fg='darkgreen', font=('times new roman', 50, 'bold'), padx=2,pady=4)
        lbltitle.pack(side=TOP, fill=X)

        img1=Image.open("C:/Users/Acer/Desktop/p.folder/TKinter/Pharmacy Management System/logo.jpg")
        img1=img1.resize((80,80), Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1 = Button(self.root, image = self.photoimg1, borderwidth=0)
        b1.place(x=50,y=20)

        #=================Data Frame==================================
        DataFrame = Frame(self.root, bd=15,relief=RIDGE, padx=20)
        DataFrame.place(x=0,y=120, width=1540, height=400)

        DataFrameLeft=LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20, text="Medicine Information", fg="darkgreen", font=('arial', 12, 'bold') )
        DataFrameLeft.place(x=0,y=5,width=900,height=350)



        


        #================Buttons Frame=====================================

        ButtonFrame = Frame(self.root, bd=15,relief=RIDGE, padx=20)
        ButtonFrame.place(x=0,y=520, width=1530, height=65)

        #=================Main Button============================================

        btnAddData = Button(ButtonFrame, text="Medicine Add", font=('arial', 12, 'bold') , bg="darkgreen", fg="white")
        btnAddData.grid(row=0, column=0)

        btnUpdateMed = Button(ButtonFrame, text="UPDATE", font=('arial', 13, 'bold'),width=14 , bg="darkgreen", fg="white")
        btnUpdateMed.grid(row=0, column=1)

        btnDeleteMed = Button(ButtonFrame, text="DELETE", font=('arial', 13, 'bold'),width=14 , bg="red", fg="white")
        btnDeleteMed.grid(row=0, column=2)

        btnRestMed = Button(ButtonFrame, text=" REST", font=('arial', 13, 'bold'),width=14 , bg="darkgreen", fg="white")
        btnRestMed.grid(row=0, column=3)

        btnExitMed = Button(ButtonFrame, text=" EXIT", font=('arial', 13, 'bold'),width=14 , bg="darkgreen", fg="white")
        btnExitMed.grid(row=0, column=4)

        #==================Search By============================================

        lblSearch = Label (ButtonFrame, font=("arial", 17, "bold"), text="Search By", padx=2, bg="red", fg="white")
        lblSearch.grid(row=0, column=5, sticky=W)

        search_combo= ttk.Combobox(ButtonFrame, width=12, font=("arial", 17, "bold"), state="readonly")
        search_combo["values"]=("Ref", "Medname", "Lot")
        search_combo.grid(row=0,column=6)
        search_combo.current(0)

        texSerch = Entry(ButtonFrame, bd=3, relief=RIDGE, width=12, font=("arial", 17, "bold"))
        texSerch.grid(row=0, column=7)


        searchBtn = Button(ButtonFrame, text=" SEARCH ", font=('arial', 13, 'bold'),width=13 , bg="darkgreen", fg="white")
        searchBtn.grid(row=0, column=8)

        showAll = Button(ButtonFrame, text=" SHOW ", font=('arial', 13, 'bold'),width=13 , bg="darkgreen", fg="white")
        showAll.grid(row=0, column=9)


        #=======================Label and Entry==================================================

        lblrefno = Label (DataFrameLeft, font=("arial", 12, "bold"), text="Reference No.", padx=2)
        lblrefno.grid(row=0, column=0, sticky=W)

        ref_combo= ttk.Combobox(DataFrameLeft, width=27, font=("arial", 12, "bold"), state="readonly")
        ref_combo ["values"]=("Ref", "Medname", "Lot")
        ref_combo.grid(row=0,column=1)
        ref_combo.current(0)


        lblCmpName = Label (DataFrameLeft, font=("arial", 12, "bold"), text="Company Name", padx=2)
        lblCmpName.grid(row=1, column=0, sticky=W)
        txtCmpName=Entry(DataFrameLeft, font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE,width=29)
        txtCmpName.grid(row=1,column=1)

        lblTypeofMedicine = Label (DataFrameLeft, font=("arial", 12, "bold"), text="Type of Medicine", padx=2, pady=6)
        lblTypeofMedicine.grid(row=2, column=0, sticky=W)

        comTypeofMedicine = ttk.Combobox(DataFrameLeft, width=27, font=("arial", 12, "bold"), state="readonly")
        comTypeofMedicine ["values"]=("Tablet", "Liquid", "Capsules", "Topical Medicines", "Drops", "Inhales", "Injection")
        comTypeofMedicine.grid(row=2,column=1)
        comTypeofMedicine.current(0)

        #===========================Add Medicine===============================================

        lblMedicineName = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Medicine Name", padx=2, pady=1 )
        lblMedicineName.grid(row=3, column=0, sticky=W)

        comMedicineName=ttk.Combobox(DataFrameLeft,state="readonly", font=("arial",12,"bold"),width=27)
        comMedicineName['value']=("Nice","Novel")
        comMedicineName.current(0)
        comMedicineName.grid(row=3, column=1)

        lblLotNo = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Lot No:", padx=2, pady=1 )
        lblLotNo.grid(row=4, column=0, sticky=W)
        txtLotNo = Entry(DataFrameLeft, font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE,width=29)
        txtLotNo.grid(row=4,column=1)

        lblIssueData = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Issue Date:", padx=2, pady=1 )
        lblIssueData.grid(row=5, column=0, sticky=W)
        txtIssueData = Entry(DataFrameLeft, font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE,width=29)
        txtIssueData.grid(row=5,column=1)

        lblExData = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Exp Date:", padx=2, pady=1 )
        lblExData.grid(row=6, column=0, sticky=W)
        txtExData = Entry(DataFrameLeft, font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE,width=29)
        txtExData.grid(row=6,column=1)

        lblUses = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Uses:", padx=2, pady=1 )
        lblUses.grid(row=7, column=0, sticky=W)
        txtUses = Entry(DataFrameLeft, font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE,width=29)
        txtUses.grid(row=7,column=1)

        lblSideEffect = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Side Effect:", padx=2, pady=1 )
        lblSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect = Entry(DataFrameLeft, font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE,width=29)
        txtSideEffect.grid(row=8,column=1)

        lblPrecWarning = Label(DataFrameLeft, font=("arial", 12, "bold"), text="Prec&Warning:", padx=15, pady=16 )
        lblPrecWarning.grid(row=0, column=2, sticky=W)
        txtPrecWarning = Entry(DataFrameLeft, font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE,width=29)
        txtPrecWarning.grid(row=0,column=3)

        lblDosage=Label(DataFrameLeft, font=("arial", 13, "bold"), text="Dosage:", padx=15, pady=6)
        lblDosage.grid(row=1, column=2, sticky=W)
        txtlblDosage = Entry(DataFrameLeft, font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE,width=29)
        txtlblDosage.grid(row=1,column=3)

        lblPrice=Label(DataFrameLeft, font=("arial", 13, "bold"), text="Tablets Price:", padx=15, pady=6)
        lblPrice.grid(row=2, column=2, sticky=W)
        txtlblPrice = Entry(DataFrameLeft, font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE,width=29)
        txtlblPrice.grid(row=2,column=3)

        lblProductQt=Label(DataFrameLeft, font=("arial", 13, "bold"), text="Product QT:", padx=15, pady=6)
        lblProductQt.grid(row=3, column=2, sticky=W)
        txtProductQt = Entry(DataFrameLeft, font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE,width=29)
        txtProductQt.grid(row=3,column=3)





#=========================Image=========================================================


        img2=Image.open("C:/Users/Acer/Desktop/p.folder/TKinter/Pharmacy Management System/p2.jpg")
        img2=img2.resize((140,135), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1 = Button(self.root, image = self.photoimg2, borderwidth=0)
        b1.place(x=475,y=330)

        img3=Image.open("C:/Users/Acer/Desktop/p.folder/TKinter/Pharmacy Management System/p4.jpg")
        img3=img3.resize((140,135), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b1 = Button(self.root, image = self.photoimg3, borderwidth=0)
        b1.place(x=625,y=330)

        img4=Image.open("C:/Users/Acer/Desktop/p.folder/TKinter/Pharmacy Management System/p5.jpg")
        img4=img4.resize((140,135), Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1 = Button(self.root, image = self.photoimg4, borderwidth=0)
        b1.place(x=773,y=330)



#===========================Data Frame Right==================================================


        DataFrameRight=LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20, text="Medicine Add Department", fg="darkgreen", font=('arial', 12, 'bold') )
        DataFrameRight.place(x=910,y=5,width=550,height=350)

        img5=Image.open("C:/Users/Acer/Desktop/p.folder/TKinter/Pharmacy Management System/p3.jpg")
        img5=img5.resize((180,85), Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1 = Button(self.root, image = self.photoimg5, borderwidth=0)
        b1.place(x=960,y=160)

        img6=Image.open("C:/Users/Acer/Desktop/p.folder/TKinter/Pharmacy Management System/p5.jpg")
        img6=img6.resize((180,85), Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b1 = Button(self.root, image = self.photoimg6, borderwidth=0)
        b1.place(x=1135,y=160)

        img7=Image.open("C:/Users/Acer/Desktop/p.folder/TKinter/Pharmacy Management System/p1.jpg")
        img7=img7.resize((180,85), Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        b1 = Button(self.root, image = self.photoimg7, borderwidth=0)
        b1.place(x=1300,y=160)



#===========================Lavel Entry====================================================


        lblrefno=Label(DataFrameRight, font=("arial", 13, "bold"), text="Referance No:", padx=15, pady=6)
        lblrefno.place(x=0, y=90)
        lblrefno = Entry(DataFrameRight, font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE,width=29)
        lblrefno.place(x=138,y=92)

        lblmedName=Label(DataFrameRight, font=("arial", 12, "bold"), text="Medicine Name:", padx=15, pady=6)
        lblmedName.place(x=0, y=120)
        lblmedName = Entry(DataFrameRight, font=("arial", 13, "bold"), bg="white", bd=2, relief=RIDGE,width=29)
        lblmedName.place(x=138,y=122)



#================================Side Frame==========================================


        side_frame=Frame(DataFrameRight,bd=4, relief=RIDGE, bg="white")
        side_frame.place(x=14, y=150, width=310, height=160)

        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.medicine_table=ttk.Treeview(side_frame,column=("ref","medname"), xscrollcommand=sc_x.set, yscrollcommand=sc_y.set)

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref", text="Ref")
        self.medicine_table.heading("medname", text="Medicine Name")

        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH, expand=1)

        self.medicine_table.column("ref",width=100)
        self.medicine_table.column("medname",width=100)



#===============================Medivine add Button=================================================



        down_frame=Frame(DataFrameRight,bd=4, relief=RIDGE,bg="darkgreen")
        down_frame.place(x=335, y=150, width=155, height=160)

        btnAddmed = Button(down_frame, text="Add", font=('arial', 12, 'bold') , bg="lime", fg="white", width=14, pady=4)
        btnAddmed.grid(row=0, column=0)

        btnUpdatemed = Button(down_frame, text="UPDATE", font=('arial', 12, 'bold') , bg="pink", fg="white", width=14, pady=4)
        btnUpdatemed.grid(row=1, column=0)

        btnDeletemed = Button(down_frame, text="DELETE", font=('arial', 12, 'bold') , bg="red", fg="white", width=14, pady=3)
        btnDeletemed.grid(row=2, column=0)

        btnClearmed = Button(down_frame, text="CLEAR", font=('arial', 12, 'bold') , bg="orange", fg="white", width=14, pady=4)
        btnClearmed.grid(row=3, column=0)



#==============================Frame Details===========================================================


        Framedeatils=Frame(self.root,bd=15, relief=RIDGE)
        Framedeatils.place(x=0, y=590, width=1530, height=210)


#============================Main Table & scrollbar======================================================


        Table_frame=Frame(self.root,bd=15, relief=RIDGE)
        Table_frame.place(x=0, y=590, width=1540, height=200)


        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.pharmacy_table=ttk.Treeview(Table_frame, column=("ref", "companyname", "type", "tabletname", "lotno", "issuedate", "expdate", "uses", "sideeffect", "warning", "dosage", "price", "productqt"),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table["show"]="headings"
        
        # self.pharmacy_table.heading("reg", text="Reference")
        # self.pharmacy_table.heading("companyname", text="Company Name")
        # self.pharmacy_table.heading("type", text="Type of Medicine")
        # self.pharmacy_table.heading("tabletname", text="Tablet Name")
        # self.pharmacy_table.heading("lotno", text="Lot No")
        # self.pharmacy_table.heading("issuedate", text="Issue Date")
        # self.pharmacy_table.heading("expdate", text="Exp Date")
        # self.pharmacy_table.heading("uses", text="Uses")
        # self.pharmacy_table.heading("sideeffect", text="Side Effect")
        # self.pharmacy_table.heading("warning", text="Prec&Warning")
        # self.pharmacy_table.heading("dosage", text="Dosage")
        # self.pharmacy_table.heading("price", text="Price")
        # self.pharmacy_table.heading("productqt", text="Product Qts")
        # self.pharmacy_table.pack(fill=BOTH, expand=1)

        # self.pharmacy_table.column("reg", width=100)
        # self.pharmacy_table.column("companyname", width=100)
        # self.pharmacy_table.column("type", width=100)
        # self.pharmacy_table.column("tabletname", width=100)
        # self.pharmacy_table.column("lotno", width=100)
        # self.pharmacy_table.column("issuedate", width=100)
        # self.pharmacy_table.column("expdate", width=100)
        # self.pharmacy_table.column("uses", width=100)
        # self.pharmacy_table.column("sideeffect", width=100)
        # self.pharmacy_table.column("warning", width=100)
        # self.pharmacy_table.column("dosage", width=100)
        # self.pharmacy_table.column("price", width=100)
        # self.pharmacy_table.column("productqt", width=100)



#======================Add Medicine Functionality Decleration============================================

# def AddMed(self):
#     conn=mysql.connector.connect(hoost="localhost", username="root," password="VishnuMySQL@321", database="mydata")
#     my_cursor=conn.cursor()
#     my_cursor.execute("insert into pharma(Ref, MedName) values(%s, %s)")


        
















if __name__ == "__main__":
    root = Tk()
    obj= PharmacyManagementSystem(root)
    root.mainloop()