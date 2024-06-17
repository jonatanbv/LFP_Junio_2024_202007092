import graphviz


def convertir_imagen(i,ruta):
    with open(ruta, 'r') as file:
        dot_data = file.read()

    dot = graphviz.Source(dot_data)
    dot.render('imagenes/grafo1', format='png')
    
convertir_imagen(1,'grafos/imagen1.dot')