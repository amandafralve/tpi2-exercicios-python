from tkinter import *
tela = Tk()

# Configurações tela
tela.title("Cálculo Média")
tela.configure(background="light pink")
tela.geometry("700x500")
tela.resizable(False, False)

# Titles
lbl_titulo = Label(tela, text="CÁLCULO MÉDIA", font="Arial 20 bold", bg="Light pink").pack()
lbl_numUm = Label(tela, text="Digite a primeira nota:", font="Arial 10 bold", bg="Light pink").place(x=15, y=50)
lbl_numDois = Label(tela, text="Digite a segunda nota:",font="Arial 10 bold", bg="Light pink").place(x=15, y=80)
lbl_numTres = Label(tela, text="Digite a terceira nota:",font="Arial 10 bold", bg="Light pink").place(x=15, y=110)
lbl_resultado = Label(tela, text="Resultado: ", font="Arial 15 bold", bg="Light pink")
lbl_resultado.pack()

# Entries
txt_numUm = Entry(tela, text="Primeira nota")
txt_numUm.place(x=170, y=50)
txt_numDois = Entry(tela, text="Segunda nota")
txt_numDois.place(x=170, y=80)
txt_numTres = Entry(tela, text="Terceira nota")
txt_numTres.place(x=170, y=110)

# Button

# Função    
def verificaFocus(event):
    txt_numUm.delete(0, END)

txt_numUm.bind("<FocusIn>", verificaFocus)

tela.mainloop()