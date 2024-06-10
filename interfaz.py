import tkinter as tk
from tkinter import Frame, ttk
from PIL import Image, ImageTk

def cargar_imagen(ruta):
    print(ruta)
    imagen = Image.open(ruta)
    imagen_tk = ImageTk.PhotoImage(imagen)

    label_imagen = tk.Label(frame, image=imagen_tk)
    label_imagen.image = imagen_tk
    label_imagen.pack()
    

def seleccionar_opcion(event):
    seleccion = comboBox.get()
    label_seleccion.config(text=f"Has seleccionado: {seleccion}")
    ruta = 'imagenes/'+seleccion
    cargar_imagen(ruta)

ventana = tk.Tk()
ventana.title('LFP 202007092')

frame_botones = Frame(ventana, width=800, height=100)
frame_botones.pack(side=tk.TOP, pady=10)

frame_lista = Frame(ventana)
frame_lista.pack(side=tk.TOP, pady=10)

opciones = ['image.png']
comboBox = ttk.Combobox(frame_lista, values=opciones)
comboBox.set('Imagenes')
comboBox.pack()

frame = Frame(ventana, width=800, height=600)
frame.pack_propagate(False)
frame.pack()

#comboBox.bind('<<ComboboxSelected>>', cargar_imagen)

comboBox.bind("<<ComboboxSelected>>", seleccionar_opcion)

# Crear un label para mostrar la opción seleccionada
label_seleccion = tk.Label(frame_lista, text="")
label_seleccion.pack(pady=10)


#botones
#boton para cargar archivo
boton1 = tk.Button(frame_botones, text='Cargar archivo')
boton1.pack(side=tk.LEFT, padx=10)
#boton para ejecutar archivo
boton2 = tk.Button(frame_botones, text='Ejecutar archivo')
boton2.pack(side=tk.LEFT, padx=10)
#boton para reporte de tokens
boton3 = tk.Button(frame_botones, text='Reporte de Tokens')
boton3.pack(side=tk.LEFT, padx=10)
#boton para reporte de errores
boton4 = tk.Button(frame_botones, text='Reporte de errores')
boton4.pack(side=tk.LEFT, padx=10)

#tabla con las imagenes




ventana.mainloop()