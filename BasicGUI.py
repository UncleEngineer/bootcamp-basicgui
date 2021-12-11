# BasicGUI.py

from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
#######################
def timestamp(thai=True):
	if thai == True:
		stamp = datetime.now()
		stamp = stamp.replace(year=stamp.year+543) # บวกเป็น พ.ศ.
		stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
	else:
		stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	return stamp

def writetext(quantity,total):
	# stamp = datetime.now()
	# stamp = stamp.replace(year=stamp.year+543) # บวกเป็น พ.ศ.
	# stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
	stamp = timestamp()
	filename = 'data.txt'
	with open(filename,'a',encoding='utf-8') as file:
		file.write('\n'+ 'วัน-เวลา: {} ทุเรียน: {} กก. รวมยอดทั้งหมด: {:,.2f} บาท'.format(stamp,quantity,total))

def writecsv(data):
	# data = ['Time',10,500]
	with open('data.csv','a',newline='',encoding='utf-8') as file:
		fw = csv.writer(file) # fw = file writer
		fw.writerow(data)
	print('Success')

#######################
GUI = Tk()
GUI.geometry('600x700')
GUI.title('โปรแกรมของลุง')

file = PhotoImage(file='durian.png')
IMG = Label(GUI,image=file,text='')
IMG.pack()

L1 = Label(GUI,text='โปรแกรมคำนวณทุเรียน',font=('Angsana New',30,'bold'),fg='green')
L1.pack() # .place(x,y) , .grid(row=0,column=0)

L2 = Label(GUI,text='กรุณากรอกจำนวนทุเรียน',font=('Angsana New',20))
L2.pack()

v_quantity = StringVar() #ตำแหน่งตัวแปรที่ใช้เก็บข้อมูลของช่องกรอก

E1 = ttk.Entry(GUI,textvariable=v_quantity,font=('impact',30))
E1.pack()

def Calculate():
	quantity = v_quantity.get()
	price = 100
	print('จำนวน', float(quantity) * price)
	cal = float(quantity) * price
	# EN DATE
	# stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	# writetext(quantity,cal)
	data = [timestamp(), quantity, cal]
	writecsv(data)

	# pop up
	messagebox.showinfo('ยอดที่ลูกค้าต้องจ่าย','ทุเรียนจำนวน {} กิโลกรัม ราคาทั้งหมด: {:,.2f} บาท'.format(quantity,cal))

B1 = ttk.Button(GUI, text='คำนวณ',command=Calculate)
B1.pack(ipadx=30,ipady=20,pady=20)

GUI.mainloop()