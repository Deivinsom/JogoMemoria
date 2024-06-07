import tkinter as tk
from tkinter import messagebox
import random

# definindo as config do game
NUM_LINHAS = 4
NUM_COLUNAS = 4
QUADRADO_SIZE_WIDTH = 10
QUADRADO_SIZE_HEIGHT = 5
CORES_QUADRADO = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'cyan', 'magenta']
COR_FUNDO = '#343a40'
COR_LETRA = '#ffffff'
FONT_STYLE = ('Arial', 12, 'bold')
MAX_TENTATIVAS = 25 

# criando uma grade aleatória de cores para os quadrados
def create_square_grid():
    cores = CORES_QUADRADO * 2
    random.shuffle(cores)
    grid = []

    for _ in range(NUM_LINHAS):
        linha = []
        for _ in range(NUM_COLUNAS):
            cor = cores.pop()
            linha.append(cor)
        grid.append(linha)
    return grid

# criando a interface principal
janela = tk.Tk()
janela.title('Jogo da Memória')
janela.configure(bg=COR_FUNDO)

# criando grid dos quadrados
grid = create_square_grid()
quadrados = []
quadrado_mostrado = []
quadrado_correspondente = []
numero_tentativas = 0

for linha in range(NUM_LINHAS):
    linha_quadrados = []
    for coluna in range(NUM_COLUNAS):
        quadrado = tk.Button(janela, width=QUADRADO_SIZE_WIDTH, height=QUADRADO_SIZE_HEIGHT, bg='black', relief=tk.RAISED, bd=3)
        quadrado.grid(row=linha, column=coluna, padx=5, pady=5)
        linha_quadrados.append(quadrado)
    quadrados.append(linha_quadrados)


# personalizando o botao
button_style = {'activebackground': '#f8f9fa', 'font':FONT_STYLE, 'fg':COR_LETRA}
janela.option_add('*Button', button_style)

# label para o numero de tentativas
label_tentativas = tk.Label(janela, text='Tentativas: {}/{}'.format(9,MAX_TENTATIVAS), fg=COR_LETRA, bg=COR_FUNDO, font=FONT_STYLE)
label_tentativas.grid(row=NUM_LINHAS, columnspan=NUM_COLUNAS, padx=10, pady=10)


janela.mainloop()