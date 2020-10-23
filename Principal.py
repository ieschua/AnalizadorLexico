#Principal.py
#Programado por Ieschua S.  - Compiladores / 4NV50

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from Buffer import Buffer
from AnalizadorLexico import AnalizadorLexico

if __name__ == '__main__':

    import_file_path = ''
    
    #Creando Interfaz Grafica
    root = tk.Tk()
    root.resizable(width=False, height=False)


    canvas1 = tk.Canvas(root, width = 750, height = 250, bg = 'AntiqueWhite2', relief = 'raised')
    canvas1.pack()

    label2 = tk.Label(root, text='          Compiladores - Martínez García Ieschua S.', bg = 'AntiqueWhite2')
    label2.config(font=('helvetica', 10))
    canvas1.create_window(350, 30, window=label2)
    
    label1 = tk.Label(root, text='       Analizador Lexico de ANSI C', bg = 'AntiqueWhite2')
    label1.config(font=('helvetica', 20))
    canvas1.create_window(350, 60, window=label1)
    
    Buffer = Buffer()
    Analizador = AnalizadorLexico()
    
    def getANSIC ():
        import_file_path = filedialog.askopenfilename(title = "Seleccionar Archivo",filetypes = ((".c Files","*.c"),))
        Buffer.cargar_buffer(import_file_path)
        
        # Listas para cada lista devuelta lista de la función tokenizar
        token = []
        lexema = []
        fila = []
        columna = []
        total = []
            
        # tokenizar y recargando el buffer
        for i in Buffer.cargar_buffer(import_file_path):
            t, lex, lin, col, tot = Analizador.tokenizar(i)
            token += t
            lexema += lex
            fila += lin
            columna += col
            total += [str(tot)]
            
        S = tk.Scrollbar(root)
        T = tk.Text(root, height=20, width=92)
        S.pack(side=tk.RIGHT, fill=tk.Y)
        T.pack(side=tk.LEFT, fill=tk.Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        
        
        
        res = '\nTokens reconocidos:\n\n' + str(token) + '\n\n\nLISTA DE TOKENS DETALLADA: \n\n' + '\n'.join([str(elem) for elem in total])
        T.insert(tk.END, res)

    label3 = tk.Label(root, text='          Introduce el archivo .c para iniciar el analisis léxico.', bg = 'AntiqueWhite2')
    label3.config(font=('helvetica', 10))
    canvas1.create_window(350, 130, window=label3)
    
    browseButton_C = tk.Button(text = "           Importar Archivo .c          ", command=getANSIC, bg='blue4', fg='white', font=('helvetica', 12, 'bold'))
    canvas1.create_window(375, 180, window=browseButton_C)

    

    def exitApplication():
        MsgBox = tk.messagebox.askquestion ('Salir','¿Seguro que desea salir de la aplicación?',icon = 'warning')
        if MsgBox == 'yes':
           root.destroy()
    
    root.mainloop()
