import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
import webview
from tkhtmlview import HTMLLabel
import threading

#funções
count=0 
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
    url="https://www.youtube.com/watch?v=hrJCIFmu8Yc"
    webview.create_window('Player Mor',url)
    webview.start()
    threading.Thread(target=webb).start()
    screen.mainloop()

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
frame_botoes.pack(side=tk.BOTTOM, pady=90)
frame_botoes.config(bg='PINK')


botao1 = tk.Button(frame_botoes, text="+",bg='PINK', font=("Sweet Apricot",14,'bold'),command=botaoadd)
botao2 = tk.Label(frame_botoes, text='0',bg='PINK',font=("Sweet Apricot",14,'bold'))
botao3 = tk.Button(frame_botoes, text="-",bg='PINK', font=("Sweet Apricot",14,'bold'),command=botaoremove )
botao4= tk.Button(frame_botoes,text='Player',bg='PINK', font=("Sweet Apricot",14,'bold'),command=webb)


botao1.pack(side=tk.LEFT, padx=100)
botao2.pack(side=tk.LEFT, padx=100)
botao3.pack(side=tk.LEFT, padx=100)
botao4.pack()



frame_player=tk.Frame(screen,bg='BLACK')
frame_player.place(relx=0.5,rely=0.5,anchor='center')

#finally
screen.mainloop()









































