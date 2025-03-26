from tkinter import *
tela = Tk()

#Configurações tela
tela.title("Cálculo Soma")
tela.configure(background="turquoise")
tela.geometry("700x700")
tela.resizable(False, False)

# Titles
lbl_titulo = Label(tela, text="CÁLCULO SOMA", font="Arial 20 bold", bg="Turquoise").pack()
lbl_numUm = Label(tela, text="Digite o primeiro número: ", bg="Turquoise").place(x=15, y=50)
lbl_numDois = Label(tela, text="Digite o segundo número: ", bg="Turquoise").place(x=15, y=80)
lbl_resultado = Label(tela, text="Resultado: ", bg="Turquoise").place(x=15, y=110)

#Entries
txt_numUm = Entry(tela, width=15, borderwidth=2)
txt_numUm.place(x=180, y=50)
txt_numUm.insert(0, "Insira o número")
txt_numDois = Entry(tela, width=15, borderwidth=2)
txt_numDois.place(x=180, y=80)
txt_numDois.insert(0, "Insira o número")

# Função cálculo soma
def calculoSoma():
    lbl_res = Label((txt_numUm.get()) + (txt_numDois.get()))

# Botão calcular
btn_calc = Button(tela, text="Calcular Soma", command=calculoSoma)
btn_calc.place(x=50, y=130)

# Função apagar campo do entry quando em foco
def verificaFocus(event):
    txt_numUm.delete(0, END)

txt_numUm.bind("<FocusIn>", verificaFocus)

# Inicialização tela
tela.mainloop()
