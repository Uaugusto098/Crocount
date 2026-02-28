import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


#estabelecer conexão no banco de dados



def conexao():
    return sqlite3.connect('itens.db')



#criar tabela

conn=conexao()
c=conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS pecas(
                   nome TEXT NOT NULL,
                   tipo TEXT NOT NULL,
                   linhas INTEGER NOT NULL
                   )
                   ''')
conn.commit()
conn.close()



#Adicionar usuario na tabela sql
def addpeca():
    
    nome=entry_nome.get()
    tipo=entry_valor.get()
    linhas=entry_p.get()

    if nome and tipo:
        conn=conexao()
        c=conn.cursor()
        answer=messagebox.askyesno('Aviso','Deseja salvar esta peça ? ')
    
        if answer is True:
            conn=conexao()
            c=conn.cursor()
            c.execute('INSERT INTO pecas(nome,tipo,linhas) VALUES (?,?,?)',(nome,tipo,linhas))
            conn.commit()
            conn.close()
            showuser()
        

        

       

    else:
        messagebox.showerror('Erro,tente novamente !')

#Mostar usuario na interface ttk
def showuser():
    for row in tree.get_children():
        tree.delete(row)
    conn=conexao()
    c=conn.cursor()
    c.execute('SELECT * FROM pecas')
    itens=c.fetchall()
    for usuario in itens:
        tree.insert("","end",values=(usuario[0],usuario[1],usuario[2]))
        conn.close()

#deletar usuario da tabela 
def deletarpeca():
    dado_del=tree.selection()
    if dado_del:
        dado_del=tree.item(dado_del)['values'][0]
        conn=conexao()
        c=conn.cursor()
        c.execute('DELETE FROM pecas WHERE nome=?',(dado_del,))
        conn.commit()
        conn.close()
        showuser()
    

def buttonv():
    global bottonT
    global entry_nome
    global entry_valor
    global entry_p
    
    bottonT=True
    

    if bottonT==True:
        screen2=tk.Tk()
        screen2.title('Adicionar peça')
        screen.geometry('1200x480')

        box_name=tk.Label(screen2,text='Nome:')
        box_name.grid(row=0,column=0,padx=30,pady=10 )
        #caixa de entrada
        entry_nome=tk.Entry(screen2)
        entry_nome.grid(row=0,column=1,padx=30,pady=10)
        #criação da label
        box_conta=tk.Label(screen2,text='Tipo de linha:')
        box_conta.grid(row=2,column=0,padx=10,pady=10 )
        #caixa de entrada
        entry_valor=tk.Entry(screen2)
        entry_valor.grid(row=2,column=1,padx=10,pady=10)
        #criação da label
       


        #criação da label
        box_l=tk.Label(screen2,text='Linha:')
        box_l.grid(row=3,column=0,padx=10,pady=10 )
        #caixa de entrada
        entry_p=tk.Entry(screen2)
        entry_p.grid(row=3,column=1,padx=10,pady=10)


        
        botton_user=tk.Button(screen2,text='Adicionar peça',command=addpeca)
        botton_user.grid(row=5,column=0,padx=30,pady=10)

        




#INTERFACE GRAFICA UTILIZANDO TKINTER
screen=tk.Tk()
screen.title('Teste Banco de Dados para o Crocount')
screen.geometry("680x480")
#Posicionar tabela
bottonT=False
botton_user=tk.Button(screen,text='Adicionar peça',command=buttonv)
botton_user.grid(row=3,column=0,padx=30,pady=10)

botton_delete=tk.Button(screen,text='Deletar peça',command=deletarpeca)
botton_delete.grid(row=3,column=1,padx=30,pady=10)









#TREE

columns=('Nome','Tipo','Linha')

tree=ttk.Treeview(screen,columns=columns,show='headings')
tree.grid(row=5,column=0,columnspan=2,padx=10,pady=10)


for col in columns:
    tree.heading(col,text=col)

for col in columns:
    tree.column(col,width=80)


conexao()
showuser()
screen.mainloop()