import tkinter as tk
import random
import string

# Función para generar contraseñas
def generar_contrasena_especial(longitud=26):
    if longitud < 2:
        return "La longitud mínima debe ser 2 para incluir 'Ñ' y 'Ç'."
    
    obligatorios = ['Ñ', 'Ç']
    letras_minusculas = string.ascii_lowercase
    letras_mayusculas = string.ascii_uppercase
    numeros = string.digits
    simbolos = string.punctuation
    caracteres = letras_minusculas + letras_mayusculas + numeros + simbolos
    
    if longitud < len(obligatorios):
        return "La longitud debe ser mayor o igual a la cantidad de caracteres obligatorios."
    
    contrasena = obligatorios[:]
    while len(contrasena) < longitud:
        contrasena.append(random.choice(caracteres))
    
    random.shuffle(contrasena)
    return ''.join(contrasena)

# Crear la ventana principal
def crear_interfaz():
    ventana = tk.Tk()
    ventana.title("PWDGEN_GlitchBane")
    ventana.geometry("400x200")  # Tamaño de la ventana
    #ventana.configure(bg="#df9e95")  # Cambiar color de fondo

    # Etiqueta
    etiqueta = tk.Label(ventana, text="Haz clic para generar una contraseña especial:", font=("Arial", 12))
    etiqueta.pack(pady=10)

    # Campo de texto para mostrar la contraseña
    resultado = tk.Entry(ventana, font=("Courier", 14), width=30, justify="center")
    resultado.pack(pady=10)

    # Frame para los botones
    botones_frame = tk.Frame(ventana)
    botones_frame.pack(pady=10)

    # Función para manejar el botón de generación
    def generar():
        contrasena = generar_contrasena_especial(26)  # Llama a la función
        resultado.delete(0, tk.END)  # Borra el campo actual
        resultado.insert(0, contrasena)  # Muestra la nueva contraseña
    
    # Botón para generar contraseñas
    boton = tk.Button(botones_frame, text="Generar Contraseña", font=("Arial", 12), command=generar)
    boton.pack(side=tk.LEFT, padx=5)

    # Función para copiar la contraseña
    def copiar_al_portapapeles():
        contrasena = resultado.get()
        if contrasena:
            ventana.clipboard_clear()
            ventana.clipboard_append(contrasena)
            ventana.update()  # Mantiene el portapapeles actualizado
    
    # Botón para copiar
    boton_copiar = tk.Button(botones_frame, text="Copiar al Portapapeles", font=("Arial", 12), command=copiar_al_portapapeles)
    boton_copiar.pack(side=tk.LEFT, padx=5)

    # Ejecutar la ventana
    ventana.mainloop()

# Llamar a la interfaz
crear_interfaz()
