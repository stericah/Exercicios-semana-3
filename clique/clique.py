import tkinter as tk
import webbrowser

def abrir_link():
    webbrowser.open("https://www.youtube.com/watch?v=M3Keg5XKJO8")

def nao_hover(event):
    nao_label.place(x=1000, y=1000)

def criar_janela():
    janela = tk.Tk()
    janela.geometry("400x200")
    janela.title("Pedido de Casamento")

    pergunta_label = tk.Label(janela, text="Quer se casar comigo?", font=("Arial", 14))
    pergunta_label.pack(pady=20)

    sim_button = tk.Button(janela, text="Sim", command=abrir_link, font=("Arial", 12))
    sim_button.pack(side=tk.LEFT, padx=20)

    global nao_label
    nao_label = tk.Label(janela, text="Não", font=("Arial", 12))
    nao_label.pack(side=tk.RIGHT, padx=20)

    nao_label.bind("<Enter>", nao_hover)

    janela.mainloop()

criar_janela()
