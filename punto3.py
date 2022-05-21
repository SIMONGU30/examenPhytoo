from ast import If
from operator import index, length_hint


opcion=0
productos=[]


print("///////////////////// MENU A LA CARTA //////////////////////")
print("1.Registre el nombre de un producto")
print("2.Mostrar todos los productos")
print("3.Editar producto")
print("4.Eliminar producto")
print("0.Salir")
print("////////////////////////////////////////////////////////////")
opcion=int(input("ingrese una opcion del menu: "))
while(opcion!=0): 
    if opcion ==1:
      producto=input("ingrese nombre del producto: ")
      productos.append(producto)
    elif opcion==2:
            print(productos)

    elif opcion==3:
        
        productoCambio=input("ingrese producto a cambiar: ")
        if(productoCambio==cambio):
            cambio=input("ingrese por el que lo va a cambiar: ")
            for i in range (len(productos)):
             if (productos[i]==productoCambio):
                    productos[i]=cambio
        
    elif opcion==4:
        for producto in productos:
            productoEliminado=input("ingrese producto a Eliminar: ")
            if(productoEliminado==producto):
                productos.remove(productoEliminado)
                print("producto eliminado con exito ")
    elif opcion==0:
        print("Suerte gonorreaaaaa")
    else:
        print("opcion no valida")

    opcion=int(input("Ingrese una opcion del menu: "))