import tkinter as tk

#  Criar a ajanela 
window = tk.Tk()
window.geometry("300x150")
window.title("Gerenciador de frases")

# Adicionar um frame
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill='x', expand=True)
# Adicionar um label
label = tk.Label(frame, text="Olá Mundo!")
label.pack(fill='x', expand=True)

# Adicionando o imput text
frase_labe = tk.Label(frame, text="Frase:")
frase_labe.pack(fill='x', expand=True)

frase_inp = tk.Entry(frame)
frase_inp.pack(fill='x', expand=True)

# Alterar o texto do label ao clicar no botão
def click():
    label.config(text=frase_inp.get())

# Adicionar um botão
button = tk.Button(frame, text="Enviar", command=click)
button.pack()


window.mainloop()