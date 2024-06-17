from analizador_prueba import Lexer
import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import Frame, ttk
from PIL import Image, ImageTk
from nodosGrafo import NodoGrafo
import graphviz



grafo_imagenes_agregadas = []



def convertir_imagen(i,ruta):
    with open(ruta, 'r') as file:
        dot_data = file.read()

    dot = graphviz.Source(dot_data)
    dot.render((f'imagenes/grafo{i}'), format='png')
    



rut = ''


def crear_grafo_imagen(i,grafo_imagen):
    
    with open(f'grafos/imagen{i}.dot', 'w') as file:
        file.write("""digraph G {
	fontname="Helvetica,Arial,sans-serif"
	node [fontname="Helvetica,Arial,sans-serif"]
	edge [fontname="Helvetica,Arial,sans-serif"]

	subgraph cluster_0 {
		style=filled;
		color=lightgrey;
		node [style=filled,color=white];\n""")
        for graf in grafo_imagen.nodos:
            file.write(graf[1].replace("'",'"'))
            file.write('\n')
        file.write(';')
        file.write(f'label="{grafo_imagen.nombre}";')
        file.write('}')

        contador = 0

        for conexiones in grafo_imagen.conexiones:
            global conexion1
            global conexion2
            conexion1 = ''
            conexion2 = ''
            for graf in grafo_imagen.nodos:
                if graf[0] == conexiones[0]:
                    conexion1=graf[1]
            for graf in grafo_imagen.nodos:
                if graf[0]== conexiones[1]:
                    conexion2=graf[1]

            file.write(f'{conexion1.replace("'",'"')} -> {conexion2.replace("'",'"')};')
        file.write('}')


def crear_grafo(tokens):
    global estado
    estado = 0
    contador = 0
    global nombre_grafo
    global nombre_nodos
    global conexiones_dos
    global conexiones_nodos
    nombre_grafo = ''
    nodo_solo = []
    nombre_nodos = []
    conexiones_dos = []
    conexiones_nodos = []
    i = 0
    
    for token in tokens:
        #print(token.lexema())
        if token.lexema()=='nombre':
            estado = 1
        elif estado==1 and token.lexema()=='->':
            estado=2
        elif estado == 2:
            estado = 3
            nombre_grafo = token.lexema()
            #print(f'el nombre es: {token.lexema()}')
        elif estado==3 and token.lexema()==';':
            estado=4
        elif estado == 4 and token.lexema()=='nodos':
            estado =5
        elif estado == 5 and token.lexema()=='->':
            estado=6
        elif estado == 6 and token.lexema()=='[':
            estado=7
        elif estado ==7:
            nodo_solo.append(token.lexema())
            #print(f'nombre del nombre: {token.lexema()}')
            estado=8
        elif estado==8 and token.lexema()==':':
            estado=9
        elif estado==9:
            nodo_solo.append(token.lexema())
            nombre_nodos.append(nodo_solo)
            nodo_solo=[]
            #print(f'nombre del nodo: {token.lexema()}')
            estado = 10
        elif estado==10 and token.lexema()==',':
            estado=7
        elif estado == 10 and token.lexema()==']':
            estado=11
        elif estado == 11 and token.lexema()==';':
            estado = 12
        elif estado == 12 and token.lexema()=='conexiones':
            estado = 13
        elif estado == 13 and token.lexema()=='->':
            estado = 14
        elif estado == 14 and token.lexema()=='[':
            estado = 15
        elif estado == 15 and token.lexema()=='{':
            
            estado = 16
        elif estado == 16:
            #print('primer nodo: ', token.lexema())
            conexiones_dos.append(token.lexema())
            estado = 17
        elif estado == 17 and token.lexema()=='>':
            estado =18
        elif estado == 18:
            conexiones_dos.append(token.lexema())
            #print(f'conectado a {token.lexema()}')
            estado = 19
        elif estado == 19 and token.lexema()=='}':
            conexiones_nodos.append(conexiones_dos)
            estado = 20
            conexiones_dos = []
        elif estado == 20 and token.lexema()==',':
            estado = 15
        elif estado == 20 and token.lexema()==']':
            print('------finalizo el primer grafo-------')
            nuevo = NodoGrafo(nombre_grafo,nombre_nodos,conexiones_nodos)
            crear_grafo_imagen(contador,nuevo)
            convertir_imagen(contador,(f'grafos/imagen{contador}.dot'))
            grafo_imagenes_agregadas.append(f'grafo{contador}.png')

            contador+=1
            print(nuevo.nombre)
            for nodo in nuevo.nodos:
                print(f'{nodo[0]} ---> {nodo[1]}')
            for nodos in nuevo.conexiones:
                print(f'{nodos[0]} -> {nodos[1]}')

            nombre_grafo = ''
            nombre_nodos = []
            conexiones_dos = []
            conexiones_nodos = []


            estado = 21
        elif estado ==21 and token.lexema()=='.':
            
            estado == 22
        elif estado == 22 and token.lexema()=='.':
            estado=23
        elif estado == 23 and token.lexema()=='.':
            estado = 24
        elif estado == 24 and token.lexema()=='nombre':
            

            
            estado=1
        else:
           
            estado = 50

def crear_html_tokens( tokens):
    with open('reportes/tabla_tokens.html', 'w') as file:
        file.write("""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tokens Detectados</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <h1>Ejemplo de Tabla en HTML</h1>
    <table>
        <thead>  <tr>
                <th>Tipo</th>
                <th>Token</th>
                <th>Fila</th>
                <th>Columan</th>
            </tr>
        </thead>
        <tbody>""")
        for token in tokens:
            file.write('<tr>')
            file.write(f'<th>{token.nombre()}</th>')
            file.write(f'<th>{token.lexema()}</th>')
            file.write(f'<th>{token.fila()}</th>')
            file.write(f'<th>{token.columna()}</th>')
            file.write('</tr>')
        file.write('</tbody>')

        file.write("""</table>

    """)
        
        file.write("""

</body>
</html>""")
        

def crear_html_errores( errores):
    with open('reportes/tabla_errores.html', 'w') as file:
        file.write("""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tokens Detectados</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    """)
        

        file.write("""

    <h1>Errores detectados</h1>

    <table>
        <thead>
            <tr>
                <th>Tipo</th>
                <th>Caracter</th>
                <th>Fila</th>
                <th>Columna</th>
                <th>Caracter</th>
            </tr>
        </thead>
        <tbody>""")
        for error in errores:
            file.write('<tr>')
            file.write(f'<th>{error.toke()}</th>')
            file.write(f'<th>{error.lex()}</th>')
            file.write(f'<th>{error.fila()}</th>')
            file.write(f'<th>{error.colum()}</th>')
            file.write(f'<th>{error.carac()}</th>')
            file.write('</tr>')
        file.write("""</tbody>
    </table>

</body>
</html>""")
        

def operar_archivo(ruta):
    global lexer


    archivo = open(ruta, "r", encoding="utf-8")
    texto = archivo.read()

    lexer = Lexer(texto)

    lexer.analizar()
            

    crear_grafo(lexer.tokens)

def crar_errores():
    crear_html_errores(lexer.errores)

def crear_token():
    crear_html_tokens(lexer.tokens)





def cargar_imagen(ruta):
    print(ruta)
    
    imagen = Image.open(ruta)
    imagen = imagen.resize((400, 400))
    imagen_tk = ImageTk.PhotoImage(imagen)

    label_imagen = tk.Label(frame, image=imagen_tk)
    label_imagen.image = imagen_tk
    label_imagen.place(x=150,y=20, width=400, height=400)
    label_imagen.config(bg='black')

def cargar_archivo():
    global rut
    rut = filedialog.askopenfilename(title='abrir')

def analizar():
    operar_archivo(rut)
    
def actualizar_combobox():
    
    comboBox['values'] = grafo_imagenes_agregadas

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


comboBox = ttk.Combobox(frame_lista, values=grafo_imagenes_agregadas)
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
boton1 = tk.Button(frame_botones, text='Cargar archivo', command=cargar_archivo)
boton1.pack(side=tk.LEFT, padx=10)
#boton para ejecutar archivo
boton2 = tk.Button(frame_botones, text='Ejecutar archivo', command=analizar)
boton2.pack(side=tk.LEFT, padx=10)
#boton para reporte de tokens
boton3 = tk.Button(frame_botones, text='Reporte de Tokens', command=crear_token)
boton3.pack(side=tk.LEFT, padx=10)
#boton para reporte de errores
boton4 = tk.Button(frame_botones, text='Reporte de errores', command=crar_errores)
boton4.pack(side=tk.LEFT, padx=10)

boton = tk.Button(frame_botones, text="Actualizar", command=actualizar_combobox)
boton.pack(pady=10)
#tabla con las imagenes




ventana.mainloop()

print(grafo_imagenes_agregadas)