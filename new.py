from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#ตัวGUI
GUI = Tk()
GUI.title('โปรแกรมยันทึกข้อมูล')
GUI.geometry('500x400')

#หัวข้อของโปรแกรม
L1 = Label(GUI,text='Schedule program',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)

#ฟังก์ชั่น
def Button1():
    text = 'On Monday you have งานช่างx2 นาฎสิน  วิทย์x2 ภาษาไืทย คณิตหลัก คณิตเสริม'
    messagebox.showinfo('ตารางสอน',text)

def Button2():
    text = 'On Tuesday you have พละ เคมีx2 สังคม ประวัติ Listening อังกฤษ'
    messagebox.showinfo('ตารางสอน',text)

def Button3():
    text = 'On Wednesday you have คณิตเสริม สังคม  นาฎสิน ฟิสิกส์x2 คณิตหลัก ลูกเสือ อังกฤษ'
    messagebox.showinfo('ตารางสอน',text)

def Button4():
    text = 'On Thursday you have สุขศึกษา ภาษาไืทย Listening โปรแกรมx2 คณิตเสริม แนะแนว วิทย์'
    messagebox.showinfo('ตารางสอน',text)

def Button5():
    text = 'On Friday you have ภาษาไืทย คณิตหลัก คณิตเสริม สังคม อังกฤษ ธรรมศึกษา  ชีวะx2  '
    messagebox.showinfo('ตารางสอน',text)

def Button6():
    text = 'Today\'s homework ไืทยืแบบฝึกหัด 2 หน้า คณิตหลัก ทำแบบฝึกหัด 2.3 คณิตเสริมส่งแก้ข้อสอบเรื่องการสร้าง สังคมอ่านหน้า56-60 อังกฤษทำหน้า 69 หัวข้อ exploit'
    messagebox.showinfo('การบ้าน',text)



#กำหนดตำแหน่ง
FB1 = Frame(GUI)
FB1.place(x=30,y=125)

FB2 = Frame(GUI)
FB2.place(x=250,y=125)

FB3 = Frame(GUI)
FB3.place(x=30,y=225)

FB4 = Frame(GUI)
FB4.place(x=250,y=225)

FB5 = Frame(GUI)
FB5.place(x=30,y=325)

FB6 = Frame(GUI)
FB6.place(x=250,y=325)

#ปุ่ม
B1 = ttk.Button(FB1,text='วันจันทร์เรียนอะไรบ้าง',command=Button1)
B1.pack(ipadx=20,ipady=20)

B2 = ttk.Button(FB2,text='วันอังคาร์เรียนอะไรบ้าง',command=Button2)
B2.pack(ipadx=20,ipady=20)

B3 = ttk.Button(FB3,text='วันพุธ์เรียนอะไรบ้าง',command=Button3)
B3.pack(ipadx=20,ipady=20)

B4 = ttk.Button(FB4,text='วันพฤหัส์เรียนอะไรบ้าง',command=Button4)
B4.pack(ipadx=20,ipady=20)

B5 = ttk.Button(FB5,text='วันศุกร์เรียนอะไรบ้าง',command=Button5)
B5.pack(ipadx=20,ipady=20)

B6 = ttk.Button(FB6,text='การบ้านวันนี้',command=Button6)
B6.pack(ipadx=20,ipady=20)



GUI.mainloop()
