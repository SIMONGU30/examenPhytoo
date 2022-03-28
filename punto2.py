contador=0
contador1=0
while(10>contador):

    numero=int(input("Ingrese por favor  en que año nacio : "))
    if(numero<2022):
        resultado= 2022-numero
        print(f"usted tiene {resultado} años ")
    else:
        print(f"usted no ha nacido ")
        
    if(resultado>=22):
        contador1=contador1+1
    
    contador=contador+1

print(f"los mayores a 22 son  : {contador1} ")
