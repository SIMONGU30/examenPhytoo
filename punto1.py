
cantidad=int(input("Ingrese la cantidad de numeros que desea : "))
contador=0
contador2=0
contador3=0
contador4=0

while(cantidad>contador):

    numero=int(input("digite un numero "))
    if(numero%2==0):
        contador2=contador2+1

        if(numero%3==0):
             contador3=contador3+1
    elif(numero%3==0):
        contador3=contador3+1
    

    elif(numero<0):
        contador4=contador4+1
      

    else: 
        print("diigite un numero valido ")
        
    contador=contador+1
print(f"la cantidad de multiplos de 2 fue : {contador2} ")
print(f"la cantidad de multiplos de 3 fue : {contador3} ")
print(f"la cantidad de multiplos negativos fue : {contador4 }")







    
