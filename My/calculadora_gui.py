
import tkinter as tk
from tkinter import messagebox

class CalculadoraApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora 🧮")
        master.geometry("320x400")
        master.resizable(False, False)

        self.entrada = tk.Entry(master, font=("Arial", 24), borderwidth=2, relief="groove", justify="right")
        self.entrada.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        self.criar_botoes()

    def adicionar(self, valor):
        self.entrada.insert(tk.END, valor)

    def calcular(self):
        try:
            resultado = eval(self.entrada.get())
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, str(resultado))
        except Exception:
            messagebox.showerror("Erro", "Expressão inválida")

    def limpar(self):
        self.entrada.delete(0, tk.END)

    def criar_botoes(self):
        botoes = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=']
        ]

        frame = tk.Frame(self.master)
        frame.pack()

        for i, linha in enumerate(botoes):
            linha_frame = tk.Frame(frame)
            linha_frame.pack(expand=True, fill='both')
            for j, botao in enumerate(linha):
                if botao == '=':
                    btn = tk.Button(linha_frame, text=botao, font=("Arial", 20), bg="#4CAF50", fg="white",
                                    command=self.calcular)
                    btn.pack(side="left", expand=True, fill='both')
                elif botao == 'C':
                    btn = tk.Button(linha_frame, text=botao, font=("Arial", 20), bg="#f44336", fg="white",
                                    command=self.limpar)
                    btn.pack(side="left", expand=True, fill='both')
                else:
                    btn = tk.Button(linha_frame, text=botao, font=("Arial", 20), command=lambda val=botao: self.adicionar(val))
                    btn.pack(side="left", expand=True, fill='both')

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()
