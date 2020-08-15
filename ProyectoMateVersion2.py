import math
men=True
lista_usuario = []
#funcions
def primer_funcion(x):
    resultado = 3*x+2
    return resultado

def segunda_funcion(x):
    resultado = x +1
    return resultado

def tercera_funcion(x):
    return math.pow(x, 2)

def clasificar_inyectiva(imagenes, tipo_numeros, funcion):
    es_inyectiva = False
    existe_imagen = False
    if(tipo_numeros == 1):
        for img in imagenes:
            ciclo = 0
            verificar = 0
            for i in range(-100, 100):
                if(funcion == 1):
                    if(img == primer_funcion(i)):
                        verificar = img
                        ciclo += 1
                        existe_imagen = True
                        if(ciclo > 1):
                            if(verificar == primer_funcion(i)):
                                return es_inyectiva
                elif(funcion == 2):
                    if(img == segunda_funcion(i)):
                        verificar = img
                        ciclo += 1
                        existe_imagen = True
                        if(ciclo > 1):
                            if(verificar == segunda_funcion(i)):
                                return es_inyectiva
                elif(funcion == 3):
                    if(img == tercera_funcion(i)):
                        verificar = img
                        ciclo += 1
                        existe_imagen = True
                        if(ciclo > 1):
                            if(verificar == tercera_funcion(i)):
                                return es_inyectiva
        if(existe_imagen):
            es_inyectiva = True
            return es_inyectiva
        else:
            return es_inyectiva
        
def clasificar_sobreyectiva(imagenes, tipo_numeros, funcion):
    es_sobreyectiva = False
    verificar = len(imagenes)
    resultado = 0
    if(tipo_numeros == 1):
        for img in imagenes:
            for i in range(-100, 100):
                if (funcion == 1):
                    if (img == primer_funcion(i)):
                        verificar -= 1
                        if(verificar == 0):
                            es_sobreyectiva = True
                            return es_sobreyectiva
                elif (funcion == 2):
                    if (img == segunda_funcion(i)):
                        verificar -= 1
                        if(verificar == 0):
                            es_sobreyectiva = True
                            return es_sobreyectiva
                elif (funcion == 3):
                    if (img == tercera_funcion(i)):
                        verificar -= 1
                        if(verificar == 0):
                            es_sobreyectiva = True
                            return es_sobreyectiva
        return es_sobreyectiva

def clasificar_biyectiva(imagenes, tipo_numeros, funcion):
    es_biyectiva = False
    if(clasificar_inyectiva(imagenes, tipo_numeros, funcion) == True and clasificar_sobreyectiva(imagenes, tipo_numeros, funcion) == True):
        es_biyectiva = True
    else:
        return es_biyectiva
    return es_biyectiva
    
#Definiciones
def defin():
    volver= ""
    op=True
    while op:
        definicion=int(input("¿Cual definicion quiere? \n 1. Inyectiva \n 2. Sobreyectiva \n 3. Biyectiva\n"))
        if definicion==1:
            print("\nInyectivas: Cada imagen tiene no más de una preimagen en el dominio\n")
        elif definicion ==2:
            print("\nSobreyectivas: Todos los elementos de las imagenes tienen una preimagen\n")
        elif definicion==3:
            print("\nBiyectiva: Es inyecyiva y sobreyectiva el mismo tiempo\n")
        else:
            print("Invalido")
        volver = input("Quiere verificar otra definición? ¿Si o no?\n")
        volver = volver.lower()
        if (volver=="si" or volver=="s"):
            op= True
        else:
            op = False
#Datos calificador 
def cali():
    print("Calificador de Funciones\n")
    repito= ""
    opcion = True
    while opcion:
        tipo_numeros= 1
        funcion = int(input('Seleccione una funcion para comprobar: \n 1. 3x+2 \n 2. x+1 \n 3. x^2 \n'))
        cantidad_imagenes = int(input('Cuantas imagenes desea agregar: \n'))
        imagenes= []
        print('Ingrese las imagenes que desea comprabar: \n')
        for i in range(0, cantidad_imagenes):
            imagenes.append(float(input('Ingrese la imagen ' + str((i+1)) +':\n')))
        if(clasificar_inyectiva(imagenes, tipo_numeros, funcion)):
            print('La funcion es inyectiva')
        else:
            print('No es inyectiva')
        if(clasificar_sobreyectiva(imagenes,tipo_numeros, funcion)):
            print('Es sobreyectiva')
        else:
            print('No es sobreyectiva')
        if(clasificar_biyectiva(imagenes, tipo_numeros, funcion)):
            print('Es biyectiva')
        else:
            print('No es biyectiva')
        repito = input("\nQuiere verificar otra funcion? ¿Si o no?\n")
        repito = repito.lower()
        if (repito=="si" or repito=="s"):
            opcion= True
        else:
            opcion = False
#Salida
def fin():
    print("Gracias")

while men:
    menuSelect = ""
    print("Menu")
    print("1. Definiciones")
    print("2. Calificador de Funciones")
    print("3. Salir")
    menuSelect= int(input("\nSeleccióne una de las opciones \n"))
    if (menuSelect == 1):
        defin()
    elif menuSelect == 2:
        cali()
    elif menuSelect == 3:
        fin()
        men=False
    else:
        print("Invalido")

#Definiciones

