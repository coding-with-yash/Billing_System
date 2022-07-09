from tkinter import*
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Design Billing Software Module")
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg="#074463",fg="white",font=("time new roman",30,"bold"),pady=2).pack(fill=X)

        #======== variable ===========
        
             #======== Customer Detail ===========
        self.c_name=StringVar()
        self.pho_number=StringVar()
        
        self.bill_number=StringVar()
        x=random.randint(1000,9999)
        self.bill_number.set(str(x))

        self.search_bill=StringVar()
            #======== Cosmetics ===========
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.hair_gell=IntVar()
            #======== Grocery ===========
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
            #======== Cold Drink ===========
        self.maza=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()
        self.frooti=IntVar()
            #======== Billing Menu ===========
        self.cosmetics_price=StringVar()
        self.glocery_price=StringVar()
        self.cold_drink_price=StringVar()

        self.cosmetics_tax=StringVar()
        self.glocery_tax=StringVar()
        self.cold_drink_tax=StringVar()
            

        #Customer Details.........

        F1=LabelFrame(self.root,text="Customer Detail",font=("time new roman",15,"bold"),fg="gold",bg="#074463")
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg="#074463",fg="white",font=("time new roman",14,"bold")).grid(row=0,column=0,padx=5,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=2,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=10)

        cphn_lbl=Label(F1,text="Phone Number",bg="#074463",fg="white",font=("time new roman",14,"bold")).grid(row=0,column=2,padx=5,pady=5)
        cphn_txt=Entry(F1,width=15,textvariable=self.pho_number,font="arial 15",bd=2,relief=SUNKEN).grid(row=0,column=3,padx=5,pady=10)

        c_bill_lbl=Label(F1,text="Bill Number",bg="#074463",fg="white",font=("time new roman",14,"bold")).grid(row=0,column=4,padx=5,pady=5)
        c_bill_txt=Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=2,relief=SUNKEN).grid(row=0,column=5,padx=5,pady=10)

        search_btn=Button(F1,command=self.find_bill,bg="cadetblue",text="Search",fg="white",width=10,bd=2,font="arial,12,bold").grid(row=0,column=6,padx=30,pady=10)

        exit_btn=Button(F1,command=self.Exit,text="Exit",bg="cadetblue",fg="white",width=7,bd=2,font="arial,12,bold").grid(row=0,column=7,padx=0,pady=10)

        #Cosmetic Product...........
        
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics Product",font=("time new roman",15,"bold"),fg="gold",bg="#074463")
        F2.place(x=1,y=170,width=325,height=280)

        bath_lbl=Label(F2,text="Bath Soap",font=("time new roman",16,"bold"),bg="#074463",fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)  

        face_cream_lbl=Label(F2,text="Face Cream",font=("time new roman",16,"bold"),bg="#074463",fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_cream_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        
        face_wash_lbl=Label(F2,text="Face Wash",font=("time new roman",16,"bold"),bg="#074463",fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_wash_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)  
        
        hair_gell_lbl=Label(F2,text="Hair Gell",font=("time new roman",16,"bold"),bg="#074463",fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hair_gell_txt=Entry(F2,width=10,textvariable=self.hair_gell,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)  

        #Grocery Product...........
        
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery Product",font=("time new roman",15,"bold"),fg="gold",bg="#074463")
        F3.place(x=330,y=170,width=300,height=280)

        rice_lbl=Label(F3,text="Rice",font=("time new roman",16,"bold"),bg="#074463",fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        rice_txt=Entry(F3,width=10,textvariable=self.rice,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)  

        food_oil_lbl=Label(F3,text="Food Oil",font=("time new roman",16,"bold"),bg="#074463",fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        food_oil_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        
        sugar_lbl=Label(F3,text="Sugar",font=("time new roman",16,"bold"),bg="#074463",fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        sugar_txt=Entry(F3,width=10,textvariable=self.sugar,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)  
        
        tea_lbl=Label(F3,text="Tea",font=("time new roman",16,"bold"),bg="#074463",fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        tea_txt=Entry(F3,width=10,textvariable=self.tea,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        #Cold Drink...........
        
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drink",font=("time new roman",15,"bold"),fg="gold",bg="#074463")
        F4.place(x=633,y=170,width=300,height=280)

        maza_lbl=Label(F4,text="Maza",font=("time new roman",16,"bold"),bg="#074463",fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        maza_txt=Entry(F4,width=10,textvariable=self.maza,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)  

        limca_lbl=Label(F4,text="Limca",font=("time new roman",16,"bold"),bg="#074463",fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        limca_txt=Entry(F4,width=10,textvariable=self.limca,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        
        sprite_lbl=Label(F4,text="Sprite",font=("time new roman",16,"bold"),bg="#074463",fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        sprite_txt=Entry(F4,width=10,textvariable=self.sprite,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)  
        
        frooti_lbl=Label(F4,text="Frooti",font=("time new roman",16,"bold"),bg="#074463",fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        frooti_txt=Entry(F4,width=10,textvariable=self.frooti,font=("time new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)  
        
         #Billing Menus.........

        F5=LabelFrame(self.root,bd=3,text="Billing Menus",font=("time new roman",15,"bold"),fg="gold",bg="#074463")
        F5.place(x=0,y=453,width=940)

        cp_lbl=Label(F5,text="Total Cosmetics Price",bg="#074463",fg="white",font=("time new roman",14,"bold")).grid(row=0,column=0,padx=5,pady=5)
        cp_txt=Entry(F5,width=10,textvariable=self.cosmetics_price,font="arial 15",bd=2,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=10)

        ct_lbl=Label(F5,text="Cosmetics Tax",bg="#074463",fg="white",font=("time new roman",14,"bold")).grid(row=0,column=2,padx=5,pady=5)
        ct_txt=Entry(F5,width=10,textvariable=self.cosmetics_tax,font="arial 15",bd=2,relief=SUNKEN).grid(row=0,column=3,padx=5,pady=10)

        gp_lbl=Label(F5,text="Total Grocery Price",bg="#074463",fg="white",font=("time new roman",14,"bold")).grid(row=1,column=0,padx=5,pady=5)
        gp_txt=Entry(F5,width=10,textvariable=self.glocery_price,font="arial 15",bd=2,relief=SUNKEN).grid(row=1,column=1,padx=5,pady=10)

        gt_lbl=Label(F5,text="Grocery Tax",bg="#074463",fg="white",font=("time new roman",14,"bold")).grid(row=1,column=2,padx=5,pady=5)
        gt_txt=Entry(F5,width=10,textvariable=self.glocery_tax,font="arial 15",bd=2,relief=SUNKEN).grid(row=1,column=3,padx=5,pady=10)
        
        cdp_lbl=Label(F5,text="Total Cold Drink Price ",bg="#074463",fg="white",font=("time new roman",14,"bold")).grid(row=2,column=0,padx=5,pady=5)
        cdp_txt=Entry(F5,width=10,textvariable=self.cold_drink_price,font="arial 15",bd=2,relief=SUNKEN).grid(row=2,column=1,padx=5,pady=10)

        cdt_lbl=Label(F5,text="Cold Drink Tax",bg="#074463",fg="white",font=("time new roman",14,"bold")).grid(row=2,column=2,padx=5,pady=5)
        cdp_txt=Entry(F5,width=10,textvariable=self.cold_drink_tax,font="arial 15",bd=2,relief=SUNKEN).grid(row=2,column=3,padx=5,pady=10)

        #Bill Area................

        F6=Frame(self.root,bd=10,relief=GROOVE)
        F6.place(x=938,y=170,width=335,height=470)
        bill_title=Label(F6,text="Billing Area",bd=7,relief=GROOVE,bg="White",fg="black",font=("arial",15,"bold")).pack(fill=X)
        scrol_y=Scrollbar(F6,orient=VERTICAL)
        self.txtarea=Text(F6,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #Button..........

        total_btn=Button(F5,command=self.total,text="Total",bg="cadetblue",fg="white",width=11,bd=2,font="arial,12,bold").grid(row=0,column=6,padx=70,pady=10)

        generate_bill_btn=Button(F5,command=self.bill_area,bg="cadetblue",fg="white",text="Generate Bill",width=11,bd=2,font="arial,12,bold").grid(row=1,column=6,padx=70,pady=10)

        clear_btn=Button(F5,command=self.clear_data,bg="cadetblue",fg="white",text="Clear",width=11,bd=2,font="arial,12,bold").grid(row=2,column=6,padx=70,pady=10)

        #self.welcome_bill()
        

    def total(self):

        #Cosmetic calculation....
        self.soap_1=self.soap.get()*15
        self.face_cream_2=self.face_cream.get()*100
        self.face_wash_3=self.face_wash.get()*80
        self.hair_gell_4=self.hair_gell.get()*40          
        self.total_Cosmetic_price=round(float(self.soap_1+self.face_cream_2+self.face_wash_3+self.hair_gell_4),2)
                          
        self.cosmetics_price.set("Rs "+str(self.total_Cosmetic_price))
        self.t_c_p=round(self.total_Cosmetic_price*0.05,2)
        self.cosmetics_tax.set("Rs "+str(self.t_c_p))

        #Cosmetric calculation....
        self.rice_1=self.rice.get()*10
        self.food_oil_2=self.food_oil.get()*120
        self.sugar_3=self.sugar.get()*35
        self.tea_4=self.tea.get()*10          

        self.total_Grocery_price=round(float(self.rice_1+self.food_oil_2+self.sugar_3+self.tea_4),2)
                                        
        self.glocery_price.set("Rs "+str(self.total_Grocery_price))
        self.t_g_p=round(self.total_Grocery_price*0.05,2)
        self.glocery_tax.set("Rs "+str(self.t_g_p))

        #Cold Drink calculation....
        self.maza_1=self.maza.get()*25
        self.limca_2=self.limca.get()*20
        self.sprite_3=self.sprite.get()*38
        self.frooti_4=self.frooti.get()*15
        
        self.total_cold_drink_price=round(float(self.maza_1+self.limca_2+self.sprite_3+self.frooti_4),2)
    
        self.cold_drink_price.set("Rs "+str(self.total_cold_drink_price))
        self.t_c_d_p=round(self.total_cold_drink_price*0.05,2)
        self.cold_drink_tax.set("Rs "+str(self.t_c_d_p))

        
        self.total_tax=round(float(self.t_c_p+self.t_g_p+self.t_c_d_p),2)
        self.price_t=round(float(self.soap_1+self.face_cream_2+self.face_wash_3+self.hair_gell_4+
                                        self.rice_1+self.food_oil_2+self.sugar_3+self.tea_4+
                                        self.maza_1+self.limca_2+self.sprite_3+self.frooti_4),2)
        self.total_txt_area=round(float(self.total_Cosmetic_price+self.t_c_p+self.total_Grocery_price+self.t_g_p+self.total_cold_drink_price+self.t_c_d_p),2)

    def welcome_bill(self):
        self.txtarea.insert(END,"\t Welcome Yash Reatil \n")
        self.txtarea.insert(END,f"\n Bill Number:{self.bill_number.get()}")
        self.txtarea.insert(END,f"\n Customer Name: {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number: {self.pho_number.get()}")
        self.txtarea.insert(END,f"\n====================================")
        self.txtarea.insert(END,f"\n Product    Qty    Price   Total")
        self.txtarea.insert(END,f"\n  Name                     price")
        self.txtarea.insert(END,f"\n====================================")
    
    
    def bill_area(self):
        if self.c_name.get()=="" or self.pho_number.get()=="":
            messagebox.showerror("Error","Customer detail are must")
        else:
            self.welcome_bill()
            #Cosmetrics Bill........
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap   {self.soap.get()}      15        {self.soap_1}")
            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream  {self.face_cream.get()}      100       {self.face_cream_2}")
            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash   {self.face_wash.get()}      80        {self.face_wash_3}")
            if self.hair_gell.get()!=0:
                self.txtarea.insert(END,f"\n Hair Gell   {self.hair_gell.get()}      40        {self.hair_gell_4}")

            #Glocery Bill........
            if self.rice.get()!=0:
                 self.txtarea.insert(END,f"\n Rice        {self.rice.get()}      10        {self.rice_1}")
            if self.food_oil.get()!=0:   
                 self.txtarea.insert(END,f"\n Food Oil    {self.food_oil.get()}      120       {self.food_oil_2}")
            if self.sugar.get()!=0:
                 self.txtarea.insert(END,f"\n Sugar       {self.sugar.get()}      35        {self.sugar_3}")
            if self.tea.get()!=0:
                 self.txtarea.insert(END,f"\n Tea         {self.tea.get()}      10        {self.tea_4}")

             #Cosmetrics Bill........
            if self.maza.get()!=0:
                 self.txtarea.insert(END,f"\n Maza        {self.soap.get()}      25        {self.maza_1}")
            if self.limca.get()!=0:
                 self.txtarea.insert(END,f"\n Limca       {self.limca.get()}      20        {self.limca_2}")
            if self.sprite.get()!=0:
                 self.txtarea.insert(END,f"\n Sprite      {self.sprite.get()}      38        {self.sprite_3}")
            if self.frooti.get()!=0:
                 self.txtarea.insert(END,f"\n Frooti      {self.frooti.get()}      15        {self.frooti_4}")

            if self.t_c_p!=0 or self.t_g_p!=0 or self.t_c_d_p!=0:
                self.txtarea.insert(END,f"\n====================================")
                self.txtarea.insert(END,f"\n Cosmetics Tax:  {self.t_c_p}")
                self.txtarea.insert(END,f"\n Grocery Tax:    {self.t_g_p}")
                self.txtarea.insert(END,f"\n Cold Drink Tax: {self.t_c_d_p}")
                self.txtarea.insert(END,f"\n Total Tax:      {self.total_tax}")
                self.txtarea.insert(END,f"\n Total Price:    {self.price_t}")
                self.txtarea.insert(END,f"\n Total Amount:    {self.total_txt_area}")
               
                
            self.save_bill()
               

    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do You Want To Save The Bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_number.get())+".txt","w") #w means write file
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill Number: {self.bill_number.get()} Saved Successfully")
        else:
            return
        

    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")    #r means read file
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill Number")

    def clear_data(self):
        op=messagebox.askyesno("Clear","Do You Want To Clear Data?")
        if op>0:
            #======== Cosmetics ===========
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.hair_gell.set(0)
            #======== Grocery ===========
            self.rice.set(0)
            self.food_oil.set(0)
            self.sugar.set(0)
            self.tea.set(0)
            #======== Cold Drink ===========
            self.maza.set(0)
            self.limca.set(0)
            self.sprite.set(0)
            self.frooti.set(0)
            #======== Billing Menu ===========
            self.cosmetics_price.set("")
            self.glocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetics_tax.set("")
            self.glocery_tax.set("")
            self.cold_drink_tax.set("")

            #Customer Details.........
            self.c_name.set("")
            self.pho_number.set("")
        
            self.bill_number.set("")
            x=random.randint(1000,9999)
            self.bill_number.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    def Exit(self):
        op=messagebox.askyesno("Exit","Do You Want To Exit?")
        if op>0:
            self.root.destroy()
        
        
                

root=Tk()
obj=Bill_App(root)
root.mainloop()            

