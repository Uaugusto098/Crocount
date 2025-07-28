import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
import webview
from tkhtmlview import HTMLLabel
import threading
import multiprocessing
from time import strftime
#funções
count=0 
def time():
      now=strftime('%H:%M:%S')
      labeltime.config(text=f'Horas: {now}')
      labeltime.after(1000,time)
      

def botaoremove():
        global count
        count-=1
        global botao2
        botao2.config(text=str(count))

        if count<0:
                botao2.config(text='0')
                count=0
             
def botaoadd():
       global count
       count+=1 
       global botao2
       botao2.config(text=str(count))

def webb(): 
    url="https://www.youtube.com/"
    webview.create_window('Player Mor',url,on_top=True)
    webview.start()
    
def insta():
      url='https://www.instagram.com/'
      webview.create_window('Insta',url,on_top=True)
      webview.start()

def netflix():
      url='https://www.netflix.com/browse'
      webview.create_window('Netflix',url,on_top=True)
      webview.start()
    
def process():
       multiprocessing.Process(target=webb).start()

def processinsta():
      multiprocessing.Process(target=insta).start()

def processnetflix():
      multiprocessing.Process(target=netflix).start()




#screen
screen = tk.Tk()
screen.title("Crocount")
screen.geometry("1080x720")
screen.config()

largura = screen.winfo_screenwidth()
altura = screen.winfo_screenheight()

img=Image.open('imagemmor.jpg')
dms=img.resize((largura,altura))
imgtk=ImageTk.PhotoImage(dms)
imglabel=tk.Label(screen,image=imgtk)
imglabel.place(x=0,y=0,relwidth=1,relheight=1)


#widgets
frame_botoes = tk.Frame(screen)
frame_botoes.pack(side=tk.BOTTOM, pady=100)
frame_botoes.config(bg='PINK')

frame_time=tk.Frame(screen)
frame_time.pack(side=tk.LEFT,pady=100)


labeltime=tk.Label(screen,bg='PINK', font=("Sweet Apricot",20,'bold'))
labeltime.place(relx=0.0, rely=1.0, anchor='sw')
time()



botao1 = tk.Button(frame_botoes, text="+",bg='PINK', font=("Sweet Apricot",14,'bold'),command=botaoadd)
linhas=tk.Label(frame_botoes,text='Linhas de croche               ',bg='PINK',font=("Sweet Apricot",14,'bold'))
botao2 = tk.Label(frame_botoes, text='0',bg='PINK',font=("Sweet Apricot",20,'bold'))
botao3 = tk.Button(frame_botoes, text="-",bg='PINK', font=("Sweet Apricot",14,'bold'),command=botaoremove )
botao4= tk.Button(frame_botoes,text='Youtube',bg='PINK', font=("Sweet Apricot",14,'bold'),command=process)
botao5=tk.Button(frame_botoes,text='instagram',bg='PINK', font=("Sweet Apricot",14,'bold'),command=processinsta)
botao6=tk.Button(frame_botoes,text='Netflix',bg='PINK', font=("Sweet Apricot",14,'bold'),command=processnetflix)

linhas.pack(side=tk.BOTTOM, pady=10)
botao1.pack(side=tk.LEFT, padx=100)
botao2.pack(side=tk.LEFT, padx=100)
botao3.pack(side=tk.LEFT, padx=100)
botao4.pack()
botao5.pack()
botao6.pack()






#finally


      
    

if __name__ == '__main__':
    multiprocessing.freeze_support()
    screen.mainloop()

















































