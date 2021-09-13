from tkinter import *
from tkinter import Checkbutton
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import pymysql
from twilio.rest import Client


# ------------------------ login button function-------------------------
db1 = pymysql.connect(host='localhost', user='root', password='Death'#', database='hotelui')


def login():
    if Uname.get()=="" or Pass.get()=="":
       value= messagebox.askyesno("Registration","Do You Want To Register",parent = root)
       if value == True:
           register()
       else:
           pass
    else:
        try:
            db1 = pymysql.connect(host='localhost', user='root', password='Death@123', database='hotelui')
            cur = db1.cursor()
            cur.execute("select * from customerinformation where Email=%s and Password=%s ",(Uname.get(),Pass.get()))
            row = cur.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Credentials",parent =root)
            else:
                orderpage()
            db1.close()
        except Exception as es:
            messagebox.askyesnocancel("Error",f"Error{str(es)}",parent = root)
def orderpage():
    x = username
    root.destroy()
    cr1 = db1.cursor()
    cr1.execute("select * from menu")
    row = cr1.fetchall()
    cr1.execute("select * from menuoption")
    row2 = cr1.fetchall()

    # ------------------------validating  input details -------------------------
    def ordersms():
        global name, no, Address
        mail = Uname.get()
        cr5 = db1.cursor()
        cr6 = db1.cursor()
        cr7 = db1.cursor()
        command = ("select Address from customerinformation where Email = %s")
        command2 = ("select First_Name from customerinformation where Email = %s")
        command3 = ("select Phone_No from customerinformation where Email = %s")
        vals = (mail)
        cr5.execute(command,vals)
        cr6.execute(command2,vals)
        cr7.execute(command3,vals)
        row2 = cr5.fetchone()
        row3 = cr6.fetchone()
        row4 = cr7.fetchone()
        for i in row2:
            Address = i
        for j in row3:
            name = j
        for k in row4:
            no = k
        print("for "+name+"\n"+box3+"\n"+no+"\n"+Address)


    def validate():

        val1 = (var1.get())
        val2 = (var2.get())
        val3 = (var3.get())
        val4 = (var4.get())
        val5 = (var5.get())
        if val1.isdigit() and val2.isdigit() and val3.isdigit() and val4.isdigit() and val5.isdigit():
            if int(val1) > 15 or int(val1) < 0 or int(val3) > 3 or int(val3) < 0:
                messagebox.showerror("Error", "Please Enter The Correct value From menu ID", parent=root1)
            elif (int(val2) <= 20 and int(val2) >= 10) or (int(val5) <= 20 and int(val5) >= 10) or (
                    int(val4) >= 30 and int(val4) <= 50):
                messagebox.showinfo("Success", "Your Order Might Take Some Time", parent=root1)
            elif int(val2) > 20 or int(val5) > 20 or int(val4) > 50:
                messagebox.showinfo("Info", "Sorry We cant Deliver This Much Amount of food", parent=root1)
            else:
                showDetails()
                btn2 = Button(root1, text="Place Order", font=('Helvetica', 20), bg="#70AF20",command = ordersms)
                btn2.place(x=600, y=770, width=270)
        else:
            messagebox.showerror("failure", "Not int vals", parent=root1)

    # ------------------------fetching an combining details from database -------------------------


    def showDetails():
        box2.delete(0.0, 'end')
        global itemval, rotival, box3
        item = var1.get()
        roti = var3.get()
        cr2 = db1.cursor()
        cr3 = db1.cursor()
        cr4 = db1.cursor()
        cr5 = db1.cursor()
        command = "select item from menu where id=%s"
        command3 = "select price from menu where id=%s"
        vals = (item)
        command2 = "select item from menuoption where id=%s"
        command4 = "select price from menuoption where id=%s"
        vals2 = (roti)
        cr2.execute(command, vals)
        cr3.execute(command3, vals)
        cr4.execute(command2, vals2)
        cr5.execute(command4, vals2)
        row2 = cr2.fetchone()
        row3 = cr3.fetchone()
        row4 = cr4.fetchone()
        row5 = cr5.fetchone()
        str1 = " "
        str2 = " "
        for i in row3:
            itemval = i
        for j in row5:
            rotival = j
        itemprice = int(var2.get()) * int(itemval)
        rotiprice = int(var4.get()) * int(rotival)
        ricebowlprice = int(var5.get()) * 40

        box2vals = f'''Item : {str1.join(row2)}  Q : {var2.get()}  Price : ₹ {itemprice} /-\nRoti : {str2.join(row4)} Q : {var4.get()}  Price : ₹  {rotiprice} /-\nRiceBowl :{var5.get()}    Price : ₹  {ricebowlprice} /-\nYour Total is : ₹  {itemprice + rotiprice + ricebowlprice} /-\nExtras : {box1.get(1.0, "end-1c")}\n'''
        box2.insert(0.0, box2vals)
        box3 = f'''{var2.get()} {str1.join(row2)}\n{var4.get()} {str2.join(row4)}\n{var5.get()} RiceBowl '''
        return box3
    root1 = Tk()
    root1.geometry("963x860")
    root1.resizable(False, False)
    image = Image.open("Screenshot (29).png")
    photo = ImageTk.PhotoImage(image)
    photo_label = Label(image=photo).place(x=0, y=0)
    col = ("Id", "Item", "Price")
    var1 = StringVar(root1)
    var2 = StringVar()
    var3 = StringVar()
    var4 = StringVar()
    var5 = StringVar()
    var6 = StringVar()
    var7 = StringVar()
    e1 = Entry(root1, textvariable=var1, width=5, font=('Helvetica', 29), bg="#C4C4C4")
    e1.place(x=290, y=183)
    e2 = Entry(root1, textvariable=var2, width=5, font=('Helvetica', 29), bg="#C4C4C4")
    e2.insert(END, 1)
    e2.place(x=290, y=253)
    e3 = Entry(root1, textvariable=var3, width=5, font=('Helvetica', 29), bg="#C4C4C4")
    e3.place(x=290, y=323)
    e4 = Entry(root1, textvariable=var4, width=5, font=('Helvetica', 29), bg="#C4C4C4")
    e4.insert(END, 1)
    e4.place(x=290, y=386)
    e5 = Entry(root1, textvariable=var5, width=5, font=('Helvetica', 29), bg="#C4C4C4")
    e5.insert(END, 0)
    e5.place(x=290, y=460)
    box1 = Text(root1, height=9, width=62, font=('Arial', 10), bg="#C4C4C4")
    box1.place(x=25, y=606)
    box2 = Text(root1, height=9, width=62, font=('Arial', 10), bg="#C4C4C4")
    box2.place(x=500, y=606)
    # ------------------------1st table -------------------------

    menutable = ttk.Treeview(root1, show="headings", height="10", columns=col)
    menutable.column('0', width=30, anchor=CENTER)
    menutable.column('1', width=300, anchor=CENTER)
    menutable.column('2', width=80, anchor=CENTER)
    menutable.heading('0', text="ID")
    menutable.heading('1', text="ITEM")
    menutable.heading('2', text="PRICE")
    menutable.place(x=525, y=182)
    for data in row:
        menutable.insert('', 'end', values=data)
    # ------------------------2nd table -------------------------

    menutable2 = ttk.Treeview(root1, show="headings", height="3", columns=col)
    menutable2.column('0', width=30, anchor=CENTER)
    menutable2.column('1', width=300, anchor=CENTER)
    menutable2.column('2', width=80, anchor=CENTER)
    menutable2.heading('0', text="ID")
    menutable2.heading('1', text="ITEM")
    menutable2.heading('2', text="PRICE")
    menutable2.place(x=525, y=423)
    for data in row2:
        menutable2.insert('', 'end', values=data)
    btn1 = Button(root1, text="Show Details", font=('Helvetica', 20), bg="#70AF20", command=validate)
    btn1.place(x=133, y=770, width=220)

    Label(text="**In case if you face any issue please contact us on +91-9654785214", fg="white", bg="#322C2C").place(
        x=0, y=839)
    root1.mainloop()


def register():
    root.destroy()
    import RegistrationPage


# ------------------------Registration button fn -------------------------
# --------

# ------------------------GUI of LOGIN WINDOW -------------------------

root = Tk()
root.geometry("453x300")
image = Image.open("Screenshot (23).png")
photo = ImageTk.PhotoImage(image)
photo_label = Label(image=photo)
photo_label.place(x = 0,y = 0)
Uname = StringVar()
Pass = StringVar()
Entry(root, textvariable = Uname,font = ('Helvetica',15),bg = "#C4C4C4").place(x = 190,y = 100,width = 215)
Entry(root, textvariable = Pass,font = ('Helvetica',15),bg = "#C4C4C4").place(x = 190,y = 155,width = 215)
Button(root,text = "login",font = ('Helvetica',13),bg = "#70AF20",command = login).place(x = 180,y = 210,width = 90)
Button(root,text = "Register",font = ('Helvetica',13),bg = "#70AF20",command = register).place(x = 180,y = 258,width = 90)
username = Uname.get()
root.mainloop()
