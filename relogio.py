# Import das bibliotecas

from tkinter import *
from time import strftime 

# Criando função para atualizar o relógio~
def atualizar_relogio():
    horario_atual = strftime("%H:%M:%S %p")
    rotulo_relogio.config(text=horario_atual)
    rotulo_relogio.after(1000, atualizar_relogio)

# Criação da interface
janela = Tk()
janela.tittle("Relogio Digital")

# Exibição do relógio
rotulo_relogio = Label(
    janela,
    font=("Arial", 40, "bold"),
    background="purple",
    foreground="white"
)

# Posiciona o rótulo no centro da tela
rotulo_relogio.pack(anchor="center")

# Chama a função da a atualiazação do relógio 
atualizar_relogio()

# Inicia o loop principal da interface
janela.mainloop()