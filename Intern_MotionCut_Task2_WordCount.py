#by SASHANG UMANATH S
#on 8.2.2024
#for MOTION CUT INTERN
##########################################    WORD COUNT(TKINTER)   #########################################################

###########################################      code start     ###########################################################
from tkinter import *
from PIL import ImageTk
from PIL import Image

#start app
def start_quiz():
    f.destroy()
    screen()

def get_value():
    global para
    para=text.get(1.0,"end-1c") 

#word count function
def word_count():
    global para,text,word
    words = para.split()
    word = len(words)
    print('Para\n\n',type(para))
    print('\nTotal no of words:',word)
 
 #display result window   
def disp_res():
    global para,word
    win3=Tk()
    win3.title('window 3')
    win3.geometry('632x360')
    win3.minsize(632,360)
    win3.configure(bg='gray')
    
    lab=Label(win3,width=52,font=("ariel",10," bold"),relief=FLAT,padx=10, 
          pady=9,bg='gray',borderwidth=0)
    lab.place(x=98,y=88)
    
    if (isinstance(para,str)==True or para!='' or para!='Enter text here'):
        lab.config(text='!!TEXT ENTERED!!\n\n'+(para)+'\n\nWORD COUNT\n'+str(word))
        if para=='':
            lab.config(text='\n\n!!!EMPTY TEXT ENTERED!!!\n\n')
        elif para=='Enter text here':
            lab.config(text='\n\n!!!PLEASE ENTER TEXT!!!\n\n')
    else:
        lab.config(text='\n\n!!!PLEASE TYPE STRING!!!\n\n')
            
    win3.after(3000,lambda:win3.destroy())
 
 #display main screen   
def screen():
    global para,text
    
    back_main=Label(win,image=bg_main,compound=CENTER)
    back_main.place(x=0,y=0) 
    
    scroll=Scrollbar(win,orient='vertical')
    scroll.pack(side=RIGHT,fill='y')
    
    Label(win,text='Enter text for word count ',width=42,font=("ariel",12," bold"),relief=RIDGE,padx=10, 
          pady=9,bg='slate gray',borderwidth=0).place(x=98,y=48)

    text=Text(win,font=("ariel",11," bold"),relief=RIDGE,bg='light slate gray',fg='black',
              width=50,height=10,yscrollcommand=scroll.set,cursor='plus white')
    text.insert(INSERT,'Enter text here')
    
    scroll.config(command=text.yview)
    text.place(x=118,y=93)
    
    #count button
    count_button=Button(win,text='Count',command=lambda:[get_value(),word_count(),disp_res()],relief=RAISED,bg='light slate gray',
                         fg='black',width=5,font=("ariel",10,"bold"))
    count_button.place(x=296,y=320)
    
    #quit button
    quit_button = Button(win, text="Quit", command=win.destroy,width=4,bg="light slate gray", 
                         fg="black",font=("ariel",10," bold"),relief=RAISED)
    quit_button.place(x=30,y=320)
     
#designing gui
if __name__ == "__main__":
    #setup main window
    win=Tk()
    win.title('window')
    win.geometry('632x360')
    win.minsize(632,360)
    
    f= Frame(win,width=631,height=360)
    f.pack(fill=X)
    
    img=(Image.open('D:\INTERNSHIP\MOTION CUT\TASK 2\word_count_bg.jpeg'))
    resized_image= img.resize((632,360),Image.ANTIALIAS)
    bg= ImageTk.PhotoImage(resized_image)
    
    img_main=(Image.open('D:\INTERNSHIP\MOTION CUT\TASK 2\word_count_bg_main.jpeg'))
    resized_image_main= img_main.resize((632,360),Image.ANTIALIAS)
    bg_main= ImageTk.PhotoImage(resized_image_main)
    
    back=Label(f,image=bg,compound=CENTER)
    back.place(x=0,y=0)
    
    
    title=Label(f,text='by SASHANG UMANATH S',width=52,font=("ariel",10," bold"),relief=FLAT,padx=10, 
          pady=9,bg='SteelBlue2',fg='black',borderwidth=0)
    title.place(x=98,y=28)
    
    start_button=Button(f, text="Start",command=start_quiz,relief=RIDGE,width=4,
                      height=1,bg="SteelBlue2",fg="black",font=("ariel",10,"bold"))
    start_button.place(x=296,y=290)
   
    win.mainloop()
#####################################################     code end     ##########################################    