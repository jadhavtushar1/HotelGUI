from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import ttk
import pymysql
db1 = pymysql.connect(host='localhost', user='root', password='#', database='hotelui')
cr1 = db1.cursor()
cr2 = db1.cursor()
cr1.execute("select * from menu")
cr2.execute("select * from menuoption")
row=cr1.fetchall()
row2=cr2.fetchall()

# ------------------------updating first table -------------------------

def update():
    id = (entry1.get())
    itemp =(entry2.get())
    price = (entry3.get())
    if entry1.get()=="" or entry2.get()=="" or entry3.get()=="":
        messagebox.showerror("Error", "Please Enter all values", parent=root)

    elif id.isdigit() and price.isdigit():
        if  int(id)>15 or int(id)<=0 :
            messagebox.showerror("Error","Please Enter Correct ID value",parent = root)
        else:
            cr2 = db1.cursor()
            id = en1.get()
            nm = en2.get()
            pr = en3.get()
            query = "update menu set item =%s,price=%s where id=%s"
            vals = (nm,pr,id)
            cr2.execute(query,vals)
            db1.commit()

# ------------------------updating second table -------------------------

def update2():
    id = (entry1.get())
    itemp = (entry2.get())
    price = (entry3.get())
    if entry1.get() == "" or entry2.get() == "" or entry3.get() == "":
        messagebox.showerror("Error", "Please Enter all values", parent=root)

    elif id.isdigit() and price.isdigit():
        if int(id) > 15 or int(id) <= 0:
            messagebox.showerror("Error", "Please Enter Correct ID value", parent=root)
        else:
            cr3 = db1.cursor()
            id = en1.get()
            nm = en2.get()
            pr = en3.get()
            query2 = "update menuoption set item =%s,price=%s where id=%s"
            vals = (nm, pr, id)
            cr3.execute(query2,vals)
            db1.commit()



# ------------------------GUI of UPDATING WINDOW -------------------------

root = Tk()
col = ("Id","Item","Price")
root.geometry("710x550")
image = Image.open("Screenshot (26).png")
photo = ImageTk.PhotoImage(image)
photo_label = Label(image=photo).place(x=0,y=0)

# ------------------------1st menu table -------------------------

menutable =ttk.Treeview(root,show = "headings",height ="10",columns =col )
menutable.column('0',width = 50,anchor = CENTER)
menutable.column('1',width = 500,anchor = CENTER)
menutable.column('2',width = 150,anchor = CENTER)
menutable.heading('0',text = "ID")
menutable.heading('1',text = "ITEM")
menutable.heading('2',text = "PRICE")
menutable.place(x = 5,y = 80)
for data in row:
    menutable.insert('','end', values=data)
# ------------------------2nd menu table -------------------------

menutable2 =ttk.Treeview(root,show = "headings",height ="3",columns =col )
menutable2.column('0',width = 50,anchor = CENTER)
menutable2.column('1',width = 500,anchor = CENTER)
menutable2.column('2',width = 150,anchor = CENTER)
menutable2.heading('0',text = "ID")
menutable2.heading('1',text = "ITEM")
menutable2.heading('2',text = "PRICE")
menutable2.place(x = 5,y = 325)
for data in row2:
    menutable2.insert('','end', values=data)
menutable.insert("","end",text = "Name",values=("0","1","2"))
l1 = Label(root,text = "ID  :",font = ('Helvetica',10),bg="#778C4B").place(x = 20 , y = 434)
l2 = Label(root,text = "ITEM  :",font = ('Helvetica',10),bg="#778C4B").place(x = 200 , y = 434)
l3 = Label(root,text = "PRICE  :",font = ('Helvetica',10),bg="#778C4B").place(x = 530 , y = 434)
en1 = StringVar()
en2 = StringVar()
en3 = StringVar()
entry1 = Entry(root, textvariable = en1,font = ('Helvetica',15),bg = "#C4C4C4")
entry1.place(x = 100,y = 430,width = 55)
entry2 = Entry(root, textvariable = en2,font = ('Helvetica',15),bg = "#C4C4C4")
entry2.place(x = 270,y = 430)
entry3 = Entry(root, textvariable = en3,font = ('Helvetica',15),bg = "#C4C4C4")
entry3.place(x = 600,y = 430,width = 75)
btn = Button(root,text="UPDATE MENU1",font = ('Helvetica',13),bg = "#70AF20",command = update).place(x = 190,y = 480)
btn2 = Button(root,text="UPDATE MENU2",font = ('Helvetica',13),bg = "#70AF20",command = update2).place(x = 370,y = 480)
root.mainloop()
