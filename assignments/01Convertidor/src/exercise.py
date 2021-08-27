# Escribe tus funciones abajo de esta línea

def pies_cm(pies):
    total_cm = pies * 30.48
    return total_cm
def pulgadas_cm(pulgadas):
    total_cm = pulgadas * 2.54
    return total_cm
def yardas_cm(yardas):
    total_cm = yardas * 91.44
    return total_cm
def main():
    print('1. pies a cm, 2. pulgadas a cm, 3. yardas a cm')
    opcion = int(input('Introduce una opcion: '))
    cantidad = int(input('Introduce la cantidad: '))
    if cantidad > 0:
        if opcion == 1:
            cm = pies_cm(cantidad)
            print (cm)
        elif opcion == 2:
            cm = pulgadas_cm(cantidad)
            print (cm)
        elif opcion == 3:
            cm = yardas_cm(cantidad)
            print (cm)
        else:
            print ('Error')
    else :
        print ('Error')
    

if __name__ == '__main__':
    main()
