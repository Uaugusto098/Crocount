import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
import webview
from tkhtmlview import HTMLLabel
import threading
import multiprocessing
from time import strftime
from Functions import *
count=0
count1=0
#funções
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


def screenbuttonremv():
        global count1
        count1-=1
        global numerador
        numerador.config(text=str(count1))
        if count1<0:
                numerador.config(text='0')
                count1=0
def screenbuttonadd():
        global count1
        count1+=1
        global numerador
        numerador.config(text=str(count1))

        if count1<0:
                numerador.config(text='0')
                count1=0

def screen2():
      global numerador
      
      janela_separada=tk.Toplevel()
      janela_separada.title("Player")
      janela_separada.geometry("400x100")
      janela_separada.config(bg='PINK')
      janela_separada.resizable(False,False)
      janela_separada.wm_attributes("-topmost",True)
      frame_centro=tk.Frame(janela_separada,bg='PINK')
      frame_centro.pack(expand=True)

      soma=tk.Button(frame_centro,text='      +      ',bg='PINK',font=("Sweet Apricot",20,'bold'),command=screenbuttonadd)
      soma.pack(side=tk.LEFT,padx=20)
      numerador=tk.Label(frame_centro,text='0',bg='PINK',font=("Sweet Apricot",20,'bold'))
      numerador.pack(side=tk.LEFT,padx=20)
      subtração=tk.Button(frame_centro,text='      -      ',bg='PINK',font=("Sweet Apricot",20,'bold'),command=screenbuttonremv)
      subtração.pack(side=tk.LEFT,padx=20)



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
frame_botoes.pack(side=tk.BOTTOM, pady=50)
frame_botoes.config(bg='PINK')

frame_botoes1 = tk.Frame(screen)
frame_botoes1.pack(side=RIGHT)
frame_botoes1.config(bg='PINK',pady=100)

frame_tabela=tk.Frame(screen)
frame_tabela.pack(side=LEFT)
frame_tabela.config(bg='PINK',pady=100)




frame_time=tk.Frame(screen)
frame_time.pack(side=tk.TOP,pady=100)


labeltime=tk.Label(screen,bg='PINK', font=("Sweet Apricot",20,'bold'))
labeltime.place(relx=0.0, rely=1.0, anchor='sw')
time()



botao1 = tk.Button(frame_botoes, text="   -   ",bg='PINK', font=("Sweet Apricot",20,'bold'),command=botaoremove)
linhas=tk.Label(frame_botoes,text='                 Linhas de croche               ',bg='PINK',font=("Sweet Apricot",14,'bold'))
botao2 = tk.Label(frame_botoes, text='0',bg='PINK',font=("Sweet Apricot",20,'bold'))
botao3 = tk.Button(frame_botoes, text="   +   ",bg='PINK', font=("Sweet Apricot",20,'bold'),command=botaoadd)
botao4= tk.Button(frame_botoes1,text='Youtube',bg='PINK', font=("Sweet Apricot",14,'bold'),command=process)
botao5=tk.Button(frame_botoes1,text='instagram',bg='PINK', font=("Sweet Apricot",14,'bold'),command=processinsta)
botao6=tk.Button(frame_botoes1,text='Netflix',bg='PINK', font=("Sweet Apricot",14,'bold'),command=processnetflix)
botao7=tk.Button(frame_botoes1,text='Miniplayer',bg='PINK', font=("Sweet Apricot",14,'bold'),command=screen2)


teste=tk.Label(frame_tabela,text='TESTE',bg='PINK',font=('Sweet Apricot',14,'bold'),)





linhas.pack(side=tk.BOTTOM, pady=10)
botao1.pack(side=tk.LEFT, padx=100)
botao2.pack(side=tk.LEFT, padx=100)
botao3.pack(side=tk.LEFT, padx=100)
botao4.pack()
botao5.pack()
botao6.pack()
botao7.pack()
teste.pack()


#finally
def spacebar1(event):
      botao1.invoke()
def spacebar2(event):
       botao3.invoke()
def spacebar3(event):
       botao7.invoke()
screen.bind('<p>',spacebar3)
screen.bind('<Left>',spacebar1)
screen.bind('<Right>',spacebar2)
if __name__ == '__main__':
    multiprocessing.freeze_support()
    screen.mainloop()