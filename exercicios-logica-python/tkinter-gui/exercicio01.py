from tkinter import *
tela = Tk()

# Configurações tela
tela.title("Cadastro de Clientes")
tela.configure(background="#00308F")
tela.geometry("780x500")
tela.resizable(False, False)

# Titulos 
lbl_titulo = Label(tela, text="CADASTRO DE CLIENTES",font="Arial 20 bold italic", fg="Turquoise", bg="#00308f").pack()
lbl_nome = Label(tela, text="Digite o nome:",font="Arial 15 bold" ,bg="#00308f", fg="White").place(x=10, y=50)
lbl_email = Label(tela, text="Digite o e-mail:",font="Arial 15 bold" ,bg="#00308f", fg="White").place(x=10, y=90)
lbl_telefone = Label(tela, text="Digite o telefone:",font="Arial 15 bold" ,bg="#00308f", fg="White").place(x=10, y=130)
lbl_endereco = Label(tela, text="Digite o endereço:",font="Arial 15 bold" ,bg="#00308f", fg="White").place(x=10, y=170)

# Entradas
txt_nome = Entry(tela, width=50, borderwidth=2,fg="Blue")
txt_nome.place(x=200, y=55)
txt_nome.insert(0, "Digite seu nome")
txt_email = Entry(tela, width=50, borderwidth=2,fg="Blue")
txt_email.place(x=200, y=95)
txt_email.insert(0, "Digite seu email")
txt_telefone = Entry(tela, width=50, borderwidth=2,fg="Blue")
txt_telefone.place(x=200, y=135)
txt_telefone.insert(0, "Digite seu telefone")
txt_endereco = Entry(tela, width=50, borderwidth=2,fg="Blue")
txt_endereco.place(x=200, y=175)
txt_endereco.insert(0, "Digite seu endereco")

#Função
def mostrarDados():
    lbl_tit = Label(tela, text="Dados do cliente", font="Arial 15 bold").place(x=280, y=270)
    lbl_out = Label(tela, text="Nome: "+ txt_nome.get()+"\nEmail: "+txt_email.get()+
"\nTelefone: "+txt_telefone.get()+"\nendereço: "+txt_endereco.get()).place(x=280, y=310)

# botão de cadastro
btn_botao = Button(tela, text="CADASTRAR CLIENTE", command=mostrarDados)
btn_botao.place(x=300, y=220)

# Função apagar campo do entry quando em foco
def verificaFocusCaixa(event):    
    txt_nome.delete(0,END)

txt_nome.bind("<FocusIn>", verificaFocusCaixa)

tela.mainloop()
