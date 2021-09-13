from tkinter import  *
from tkinter import Checkbutton
from tkinter import messagebox
from PIL import Image,ImageTk
import pymysql
# ------------------------working after submitting the order -------------------------

def Submit():
   if Fname.get()=="" or Phone.get()=="" or Email.get()=="" or password.get()=="" or Address.get(1.0, "end-1c")=="" :
       messagebox.showerror("Input Value", "Please Fill All Required Fields", parent=root2)
   elif len(Phone.get())<10:
       messagebox.showerror("Phone No", "Please Enter Your 10 Digit Phone No.", parent=root2)
   elif len(password.get())<5:
       messagebox.showerror("Password", "Password Must be More that 5 characters ", parent=root2)
   elif password.get()!=ConfPass.get():
       messagebox.showerror("Password", "Please Enter The same Password", parent=root2)
   elif check.get()==0:
       messagebox.showerror("T&C", "Please Accept Terms and Conditions", parent=root2)
       print(check.get())
   else:
        db1 = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = 'Death@123',
            database = 'hotelui'

        )
        mycommand = db1.cursor()
        try:
            command = "insert into customerinformation(First_Name,Last_Name,Phone_No,Alt_No,Email,Password,Address) values(%s,%s,%s,%s,%s,%s,%s)"
            val =(Fname.get(),Lname.get(),Phone.get(),AltPhone.get(),Email.get(),password.get(),Address.get(1.0, "end-1c"))
            mycommand.execute(command,val)
            db1.commit()
            db1.close()
            val2 = messagebox.askyesno("Registration Successfull","you Have Registered Succcessfully",parent=root2)
            if val2 == True:
                root2.destroy()
                import loginpage
            else:
                pass
        except Exception as e:
            print(e)
            db1.rollback()
            db1.close()
# ------------------------GUI OF REGISTRATION PAGE -------------------------

root2 =Tk()
root2.geometry("447x742")
root2.resizable(False,False)
image = Image.open("Screenshot (20).png")
photo = ImageTk.PhotoImage(image)
photo_label = Label(image=photo).place(x = 0,y = 0)
Fname = StringVar()
Lname = StringVar()
Phone = StringVar()
AltPhone = StringVar(root2)
Email = StringVar()
password = StringVar()
ConfPass = StringVar()
check = IntVar()
Label(root2,text="*",font = ('Helvetica',20),bg="#778C4B").place(x=97,y=335)
Entry(root2,textvariable = Fname,width = 24,font = ('Helvetica',15),bg = "#C4C4C4").place(x=150,y=135)
Entry(root2,textvariable = Lname,width = 24,font = ('Helvetica',15),bg = "#C4C4C4").place(x=150,y=172)
Entry(root2,textvariable = Phone,width = 24,font = ('Helvetica',15),bg = "#C4C4C4").place(x=150,y=210)
Entry(root2,textvariable = AltPhone,width = 24,font = ('Helvetica',15),bg = "#C4C4C4").place(x=150,y=255)
Entry(root2,textvariable = Email,width = 24,font = ('Helvetica',15),bg = "#C4C4C4").place(x=150,y=300)
Entry(root2,textvariable = password,width = 21,font = ('Helvetica',15),bg = "#C4C4C4").place(x=183,y=340)
Entry(root2,textvariable = ConfPass,width = 21,font = ('Helvetica',15),bg = "#C4C4C4").place(x=183,y=380)
Address = Text(root2,height = 6,width = 24,font = ('Helvetica',15),bg = "#C4C4C4")
Address.place(x = 150,y = 430)
check1 = Checkbutton(root2,text = "I Agree Terms & Conditions",variable = check,font = ('Helvetica',10),bg = "#778C4B")
check1.place(x = 140,y = 600)
Button(root2,text = "Register",font = ('Helvetica',15),bg = "#70AF20", command = Submit).place(x = 155,y = 645,width = 150)

root2.mainloop()
