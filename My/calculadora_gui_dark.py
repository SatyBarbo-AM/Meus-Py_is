
import tkinter as tk
from tkinter import messagebox

class CalculadoraApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora 🧮")
        master.geometry("320x400")
        master.resizable(False, False)
        master.configure(bg="#2e2e2e")  # fundo escuro

        self.entrada = tk.Entry(master, font=("Segoe UI", 24), borderwidth=0, relief="flat", justify="right", bg="#1e1e1e", fg="#00ffcc", insertbackground="#00ffcc")
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

        frame = tk.Frame(self.master, bg="#2e2e2e")
        frame.pack()

        for i, linha in enumerate(botoes):
            linha_frame = tk.Frame(frame, bg="#2e2e2e")
            linha_frame.pack(expand=True, fill='both')
            for j, botao in enumerate(linha):
                if botao == '=':
                    btn = tk.Button(linha_frame, text=botao, font=("Segoe UI", 20), bg="#00cc66", fg="white",
                                    activebackground="#00e676", activeforeground="white",
                                    command=self.calcular, relief="flat", bd=0)
                elif botao == 'C':
                    btn = tk.Button(linha_frame, text=botao, font=("Segoe UI", 20), bg="#ff4444", fg="white",
                                    activebackground="#ff6b6b", activeforeground="white",
                                    command=self.limpar, relief="flat", bd=0)
                else:
                    btn = tk.Button(linha_frame, text=botao, font=("Segoe UI", 20), bg="#3e3e3e", fg="#ffffff",
                                    activebackground="#5e5e5e", activeforeground="white",
                                    command=lambda val=botao: self.adicionar(val), relief="flat", bd=0)
                btn.pack(side="left", expand=True, fill='both', padx=1, pady=1)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()
