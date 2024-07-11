from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import csv,random
from tkinter.ttk import Notebook
from datetime import datetime
# DATABASE
from db_vocab import * # import file DB ที่เขียนแยก

# def writecsv(record_list):
# 	with open('data.csv','a',newline='',encoding='utf-8') as file:
# 		fw = csv.writer(file)
# 		fw.writerow(record_list)


GUI = Tk()

GUI.title('โปรแกรมจำคำศัพท์')
GUI.geometry('1100x600+0+0')
GUI.state('zoomed')
####FONT#####
FONT1 = ('Angsana New',20,'bold')
FONT2 = ('Angsana New',15)
FONT3 = ('Angsana New',13)

def RandomFlashcard(event=None):
	# pass
	update_table()
	random_vocab = view_vocab()

	v_check.set('')
	global checked
	checked = False
	vc = random.choice(random_vocab)
	global current_vocab
	current_vocab = vc
	#print(vc)
	v_vocab.set(vc[2])
	v_trans.set('')
	v_sentence.set('')
	# v_sentence.set('')
	# global playagain
	# playagain = True
	
def ShowTranslate(event=None):
	# pass
	print('------------',current_vocab[4])
	v_trans.set(current_vocab[4])
	# v_sentence.set(current_vocab[5])

def Showsentence(event=None):
	v_sentence.set(current_vocab[5])

def CheckTranslate(event=None):
	# pass
	global checked
	print([v_check.get()],[current_vocab[4]])
	if v_check.get() == current_vocab[4].replace(' ','') and checked != True:
		v_score.set(int(v_score.get()) + 1)
		
		checked = True
		messagebox.showinfo("showinfo", "คำตอบถูกต้อง")
		v_sentence.set(current_vocab[5])
		
		RandomFlashcard() #uncomment this if autonextword
		
		
	else:
		RandomFlashcard()
		messagebox.showwarning("showwarning", "คำตอบผิด") 
	
	check_vocab.focus()
	 
def Save():
	vocab = E1_vocab.get() # .get คือการดึงออกมาจาก StringVar
	partofspeech = E2_partofspeech.get()
	translate = addtranslate.get()
	sentence = E2_sentence.get()

	dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	# Generate Transaction
	tsid = str(int(datetime.now().strftime('%y%m%d%H%M%S')) + 114152147165)
	insert_vocab(tsid,vocab,partofspeech,translate,sentence)
	print(tsid,vocab,partofspeech,translate,sentence)
	# Clear data of entry
	update_table()
	addvocab.set('')
	add_partofspeech.set('')
	addtranslate.set('')
	addsentence.set('')
	E1_vocab.focus()
	CountVocab()

	
def CountVocab():
	
	countvocab = view_vocab()
	count = len(countvocab)
	v_countvocab.set(count)



Tab = Notebook(GUI)

F1 = Frame(Tab)
F2 = Frame(Tab)
F3 = Frame(Tab)
Tab.pack(fill=BOTH, expand=1)

try:
	flashcard = PhotoImage(file='tab_flashcard.png')
	vocab = PhotoImage(file='tab_vocab.png')
	transicon = PhotoImage(file='translate.png')

	Tab.add(F1, text='Flashcard', image=flashcard,compound='top')
	Tab.add(F2, text='All vocab', image=vocab,compound='top')
	Tab.add(F3, text='Translate', image=transicon,compound='top')
except:
	Tab.add(F1, text='Flashcard')
	Tab.add(F2, text='All vocab')
	Tab.add(F3, text='Translate')
FB0 = Frame(F1)
FB0.place(x=100,y=200)


check_label = ttk.Label(FB0,text='ตรวจความหมาย',font=('Angsana New',20))
check_label.grid(row=0,column=0)

v_check = StringVar()
check_vocab = ttk.Entry(FB0,textvariable=v_check,font=('Angsana New',20),width=50)
check_vocab.grid(row=0,column=1,padx=20,pady=20)
check_vocab.focus()
#### BIND #####


FB1 = Frame(F1)
FB1.place(x=100,y=300)

v_vocab = StringVar()
v_trans = StringVar()
v_sentence = StringVar()

show_vocab = ttk.Label(F1, textvariable=v_vocab,font=('Angsana New',50,'bold'))
show_vocab.place(x=100,y=20)

show_vocab = ttk.Label(F1, textvariable=v_trans,font=('Angsana New',50,'bold'))
show_vocab.place(x=100,y=100)

show_sentence = ttk.Label(F1, textvariable=v_sentence,font=('Angsana New',50,'bold'))
show_sentence.place(x=500,y=100)


nextvocab = ttk.Button(FB1,text='คำศัพท์ถัดไป',command=RandomFlashcard)
nextvocab.grid(row=1,column=1,padx=20,ipadx=20,ipady=10)

showvocab = ttk.Button(FB1,text='โชว์คำแปล',command=ShowTranslate)
showvocab.grid(row=1,column=2,padx=20,ipadx=20,ipady=10)

checkvocab = ttk.Button(FB1,text='ตรวจคำตอบ',command=CheckTranslate)
checkvocab.grid(row=1,column=3,padx=20,ipadx=20,ipady=10)

speak = ttk.Button(FB1,text='Show sentence',command=Showsentence)# ,command=SpeakNow
speak.grid(row=1,column=4,padx=20,ipadx=20,ipady=10)


v_score = StringVar()
v_countvocab = StringVar()
v_score.set('0')

score_label =ttk.Label(F1,text='คะแนน',font=('Angsana New',30))
score_label.place(x=50,y=400)

score = ttk.Label(F1, textvariable=v_score,font=('Angsana New',30,'bold'),foreground='red')
score.place(x=150,y=400)
########### TAB2 ###############

FB2 = Frame(F2)
FB2.place(x=1000,y=100)

L1T2 = ttk.Label(F2,text='คำศัพท์ทั้งหมด:',font=('Angsana New',20)).place(x=50,y=30)
L1 = ttk.Label(F2,textvariable=v_countvocab,font=('Angsana New',20)).place(x=200,y=30)
#'TSID'
header = ['คำศัพท์','ประเภทของคำ','คำแปล','ตัวอย่างประโยค']
headerw = [150,150,150,400]

vocablist = ttk.Treeview(F2,columns=header,show='headings',height=20)
vocablist.place(x=50,y=100)

##### ADD Vocab ########
L1_vocab = ttk.Label(FB2,text='เพิ่มคำศัพท์',font=('Angsana New',20))
L1_vocab.pack()
# L1_vocab.place(x=800,y=100)

addvocab = StringVar()
E1_vocab = ttk.Entry(FB2,textvariable=addvocab,font=('Angsana New',20),width=50)
# E1_vocab.place(x=800,y=150)
E1_vocab.pack()

L2_part_of_spepch = ttk.Label(FB2,text='ประเภทของคำ',font=('Angsana New',20))
# L2_part_of_spepch.place(x=800,y=250)
L2_part_of_spepch.pack()

add_partofspeech = StringVar()
E2_partofspeech = ttk.Entry(FB2,textvariable=add_partofspeech,font=('Angsana New',20),width=50)
# E2_partofspeech.place(x=800,y=350)
E2_partofspeech.pack()

L1_Translate = ttk.Label(FB2,text='ความหมาย',font=('Angsana New',20))
# L1_Translate.place(x=800,y=400)
L1_Translate.pack()

addtranslate = StringVar()
E2_Translate = ttk.Entry(FB2,textvariable=addtranslate,font=('Angsana New',20),width=50)
# E2_Translate.place(x=800,y=450)
E2_Translate.pack()

L2_sentence = ttk.Label(FB2,text='ตัวอย่างประโยค',font=('Angsana New',20))
# L2_sentence.place(x=800,y=500)
L2_sentence.pack()

addsentence = StringVar()
E2_sentence = ttk.Entry(FB2,textvariable=addsentence,font=('Angsana New',20),width=50)
# E2_sentence.place(x=800,y=550)
E2_sentence.pack()

bt_save = ttk.Button(F2,text='บันทึก',command=Save)
bt_save.place(x=1200,y=450)
# bt_save.pack(ipadx=30,ipady=30)

#ปรับขนาดฟอนต์และตารางให้ใหญ่ขึ้น

style = ttk.Style()
style.configure('Treeview.Heading',font=('Angsana New',20,'bold'))
style.configure('Treeview',rowheight=25,font=('Angsana New',15))

for h,w in zip(header,headerw):
	# h='TSID', w=50 ---> h='ชื่อ' w=100
	vocablist.heading(h,text=h)
	vocablist.column(h,width=w,anchor='center')

def update_table():
	#clear ข้อมูลเก่า จะได้ไม่ใส่ข้อมูลไม่ซ้ำ
	vocablist.delete(*vocablist.get_children())
	data = view_vocab()
	# print(data)
	for d in data:
		d = list(d[1:]) #แปลง tuple เป็น list
		del d[0] # ลบ ID จาก database ออก
		vocablist.insert('','end',values=d)

######## คีย์ลัด ##########
GUI.bind('<F1>',RandomFlashcard) #คำศัพท์ถัดไป
GUI.bind('<F2>',ShowTranslate)
GUI.bind('<F3>',Showsentence)
check_vocab.bind('<Return>',CheckTranslate)

########### Start UP ################
RandomFlashcard()
update_table()
CountVocab()

GUI.mainloop()