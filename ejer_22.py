#Ejercicio_22

mochila=["agua","peluche","tiramisu","cafe","Sable de luz","comunicador","dinero","espada"]
objeto= "Sable de luz"

def usar_la_fuerza(mochila,objeto, objetos_sacados=0):

    if len(mochila) == 0:
        print("No se encontró el ", objeto, " en la mochila.")
        return objetos_sacados
    
    if mochila[0] == objeto:
        objetos_sacados += 1
        print("Se encontró el", objeto, "en la mochila después de sacar", objetos_sacados, "objetos.")
        return objetos_sacados
    
    objetos_sacados += 1
    mochila.pop(0)
    return usar_la_fuerza(mochila,objeto, objetos_sacados)
