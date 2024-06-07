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

# lidando com o clique do jogador
def square_clicked(linha,coluna):
    quadrado = quadrados[linha][coluna]
    cor = quadrado['bg']
    if cor=='black':
        quadrado['bg'] = grid[linha][coluna]
        quadrado_mostrado.append(quadrado)
        if len(quadrado_mostrado) == 2:
            check_match()


# verificando se os quadrados sao iguais
def check_match():
    quadrado1, quadrado2 = quadrado_mostrado
    if quadrado1['bg'] == quadrado2['bg']:
        quadrado1.after(1000, quadrado1.destroy)
        quadrado2.after(1000, quadrado2.destroy)
        quadrado_correspondente.extend([quadrado1, quadrado2])
        check_win()
    else:
        quadrado1.after(1000, lambda:quadrado1.config(bg='black'))
        quadrado2.after(1000, lambda:quadrado2.config(bg='black'))
    quadrado_mostrado.clear()
    uptade_score()


# verificando se o jogador ja ganhou
def check_win():
    if len(quadrado_correspondente) == NUM_LINHAS * NUM_COLUNAS:
        messagebox.showinfo("Parabéns!", "Voce ganhou o jogo!")
        janela.quit()


# atualiza a pontuação e verifica se o jogador perdeu
def uptade_score():
    global numero_tentativas
    numero_tentativas += 1
    label_tentativas.config(text='Tentativas: {}/{}'.format(numero_tentativas, MAX_TENTATIVAS))
    if numero_tentativas >= MAX_TENTATIVAS:
        messagebox.showinfo("Fim de Jogo", "Voce perdeu!")
        janela.quit()
    

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
        quadrado = tk.Button(janela, command=lambda r=linha, c=coluna:square_clicked(r,c), width=QUADRADO_SIZE_WIDTH, height=QUADRADO_SIZE_HEIGHT, bg='black', relief=tk.RAISED, bd=3)
        quadrado.grid(row=linha, column=coluna, padx=5, pady=5)
        linha_quadrados.append(quadrado)
    quadrados.append(linha_quadrados)


# personalizando o botao
button_style = {'activebackground': '#f8f9fa', 'font':FONT_STYLE, 'fg':COR_LETRA}
janela.option_add('*Button', button_style)

# label para o numero de tentativas
label_tentativas = tk.Label(janela, text='Tentativas: {}/{}'.format(numero_tentativas, MAX_TENTATIVAS), fg=COR_LETRA, bg=COR_FUNDO, font=FONT_STYLE)
label_tentativas.grid(row=NUM_LINHAS, columnspan=NUM_COLUNAS, padx=10, pady=10)


janela.mainloop()