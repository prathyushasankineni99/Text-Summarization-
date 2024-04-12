import tkinter as tk

from tkinter import *

from tkinter import ttk

from tkinter.scrolledtext import *

import tkinter.filedialog

import time

timeStr=time.strftime("%Y%m%d-%H%M%S")

from nltk_summarization import nltk_summarizer

from bs4 import BeautifulSoup

from urllib.request import urlopen

window=Tk()

window.title("Text Summary")

window.geometry('760x510')

#Style

style=ttk.Style(window)

style.configure('lefttab.TNotebook',tabposition='wn')

#Tab Layout

tab_control=ttk.Notebook(window,style='lefttab.TNotebook')

tab1=ttk.Frame(tab_control)

tab2=ttk.Frame(tab_control)

tab3=ttk.Frame(tab_control)

#Add tab

tab_control.add(tab1,text=f' {"Text":^20s}')

tab_control.add(tab2,text=f' {"File":^20s}')

tab_control.add(tab3,text=f' {"URL":^20s}')

# Labels

label1=Label(tab1,text='Summarizer',padx=5,pady=5)

label1.grid(column=0,row=0)

label2=Label(tab2,text='File Processing',padx=5,pady=5)

label2.grid(column=0,row=0)

label3=Label(tab3,text='URL',padx=5,pady=5)

label3.grid(column=0,row=0)

tab_control.pack(expand=1,fill='both')

#Functions

def get_summary():

    raw_text=entry.get('1.0',tk.END)

    final_text=nltk_summarizer(raw_text)

    print(final_text)

    result='\nSummary: {}'.format(final_text)

    tab1_display.insert(tk.END,result)

def save_summary():

    raw_text=entry.get('1.0',tk.END)

    final_text=nltk_summarizer(raw_text)

    file_name='your_summary' + timeStr + '.txt'

    with open(file_name,'w') as f:

        f.write(final_text)

    result='\nName of File: {} ,\nSummary: {}'.format(file_name,final_text)

    tab1_display.insert(tk.END,result)

#Clear Function

def clear_text():

    entry.delete('1.0',END)

def clear_display_result():

    tab1_display.delete('1.0',END)

def clear_text_file():

    displayed_file.delete('1.0',END)

def clear_text_result():

    tab2_display_text.delete('1.0',END)

def clear_url_entry():

    url_entry.delete(0,END)

def clear_url_display():

    tab3_display_text.delete('1.0',END)

#Open File Functions

def openfiles():

    file1=tkinter.filedialog.askopenfilename(filetype=(('Text Files',".txt"),("All files","*")))

    if(file1.lower().endswith(('.png',',jpeg','jpg','mp3'))):

       print("File Not containing text")

    else:

        read_text=open(file1).read()

        displayed_file.insert(tk.END,read_text)

def get_file_summary():

    raw_text=displayed_file.get('1.0',tk.END)

    final_text=nltk_summarizer(raw_text)

    result='\nSummary: {}'.format(final_text)

    tab2_display_text.insert(tk.END,result)

#URL Functions

#Fetch Text from Url

def get_text():

    raw_text=str(url_entry.get())

    page=urlopen(raw_text)

    soup=BeautifulSoup(page,'lxml')

    fetched_text=' '.join(map(lambda p:p.text,soup.find_all('p')))

    url_display.insert(tk.END,fetched_text)

def get_url_summary():

    raw_text=url_display.get('1.0',tk.END)

    final_text=nltk_summarizer(raw_text)

    result='\nSummary: {}'.format(final_text)

    tab3_display_text.insert(tk.END,result)

#Main Home Tab

l1=Label(tab1,text='Enter Text to Summarize',padx=5,pady=5)

l1.grid(column=0,row=1)

entry=ScrolledText(tab1,height=10)

entry.grid(row=2,column=0,columnspan=2,padx=5,pady=5)

#Buttons

button1=Button(tab1,text="Reset",command=clear_text,width=12,bg='#01579B',fg='#fff')

button1.grid(row=4,column=0,pady=10,padx=10)

button2=Button(tab1,text="Summarize",command=get_summary,width=12,bg='#000000',fg='#fff')

button2.grid(row=4,column=1,pady=10,padx=10)

button3=Button(tab1,text="Clear Result",command=clear_display_result,width=12,bg='#FFEB3B')

button3.grid(row=5,column=0,pady=10,padx=10)

button4=Button(tab1,text="Save",command=save_summary,width=12,bg='#CD201F',fg='#fff')

button4.grid(row=5,column=1,pady=10,padx=10)

#Display Screen for Result

tab1_display=ScrolledText(tab1,height=10)

tab1_display.grid(row=7,column=0,columnspan=3,padx=5,pady=5)

#File Processing Tab

l1=Label(tab2,text="Open File To Summarize")

l1.grid(row=1,column=1)

displayed_file=ScrolledText(tab2,height=7)

displayed_file.grid(row=2,column=0,columnspan=3,padx=5,pady=3)

#BUTTONS FOR SECOND TAB

b0=Button(tab2,text="Open File",width=12,command=openfiles,bg='#C51162',fg='#fff')

b0.grid(row=3,column=0,padx=10,pady=10)

b1=Button(tab2,text="Reset",width=12,command=clear_text_file,bg='#01579B',fg='#fff')

b1.grid(row=3,column=1,padx=10,pady=10)

b2=Button(tab2,text="Summarize",width=12,command=get_file_summary,bg='#000000',fg='#fff')

b2.grid(row=3,column=2,padx=10,pady=10)

b3=Button(tab2,text="Clear Result",width=12,command=clear_text_result,bg='#FFEB3B')

b3.grid(row=5,column=1,padx=10,pady=10)

b4=Button(tab2,text="Close",width=12,command=window.destroy)

b4.grid(row=5,column=2,padx=10,pady=10)

#Display screen tab2

tab2_display_text=ScrolledText(tab2,height=10)

tab2_display_text.grid(row=7,column=0,columnspan=3,padx=5,pady=5)

tab2_display_text.config(state=NORMAL)

#URL tab

l1=Label(tab3,text="Enter URL to Summarize")

l1.grid(row=1,column=0)

raw_entry=StringVar()

url_entry=Entry(tab3,textvariable=raw_entry,width=50)

url_entry.grid(row=1,column=1)

#Buttons

button1=Button(tab3,text="Reset",command=clear_url_entry,width=12,bg='#01579B',fg='#fff')

button1.grid(row=4,column=0,padx=10,pady=10)

button2=Button(tab3,text="Get Text",command=get_text,width=12,bg='#C51162',fg='#fff')

button2.grid(row=4,column=1,padx=10,pady=10)

button3=Button(tab3,text="Clear Result",command=clear_url_display,width=12,bg='#FFEB3B')

button3.grid(row=5,column=0,padx=10,pady=10)

button4=Button(tab3,text="Summarize",command=get_url_summary,width=12,bg='#000000',fg='#fff')

button4.grid(row=5,column=1,padx=10,pady=10)

#Display Screen For Result

url_display=ScrolledText(tab3,height=10)

url_display.grid(row=7,column=0,columnspan=3,padx=5,pady=5)

tab3_display_text=ScrolledText(tab3,height=10)

tab3_display_text.grid(row=10,column=0,columnspan=3,padx=5,pady=5)

window.mainloop()

