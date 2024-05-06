# SECCION 1
# Autor: Jaime Tomás Espinosa Araya 06-05-2024

print ("\n¡ Bienvenido a la calculadora [kWh] de ShockingBlue !\n")
from random import randint
def random(x,y):
    return randint(x,y)
def artefactos(x):
    valor = 0
    personas = []
    artefactos = ["hervidor",5.9] , ["microondas 800 watts",0.8],["aspiradora 1400 watts",7.0],["secador de pelo 1800 watts",4.5],["lavadora/secadora",2.1]
    flag = True
    contador = 0
    eleccion_old= []
    while flag == True:
        eleccion = random(0,4)
        while eleccion in eleccion_old:
            eleccion = random(0,4)
        eleccion_old.append(eleccion)
        for i in range(0,x):
            personas .append( artefactos[eleccion][0])
            valor += artefactos[eleccion][1]
            break
        if contador == x-1:
            flag = False
            break
        contador += 1
    valor += 7.6
    return personas,valor

flag = True
while flag == True:
    try:
        familia = int(input("Cuantos integrantes tiene la familia (máximo de 5): "))
        flag = False
        if familia > 5 or familia < 1:
            print ("Debe ser como máximo 5, y positivo :)")
            flag = True
    except:
        print ("Debe ser un número, no letras")
        flag = True
print ("")
glob= 0
usuario = familia
contador_integrante =1
while usuario >0:
    kwh = 0
    dia = 1
    contador = 0
    repetir = True
    while familia >= 1 and dia < 8  or repetir == True:
        artefactos_1 = artefactos(random(1,3))
        kwh += artefactos_1[1]
        familia -= 1
        str= ""
        for ordenadito in artefactos_1[0]:
            str += ordenadito + " " + ","
        print (f"El integrante {contador_integrante} usa el dia {dia}: {str} y el refrigerador que es obligatorio, el gasto acumulado es de {round(kwh,1)} [kwh]")
        dia+=1
        if contador == 6:
            repetir = False
        contador+=1
        if usuario == familia:
            repetir = False
    usuario -= 1
    print (f"\nEl gasto total semanal individual del integrante {contador_integrante} es de: {round(kwh,1)} [kwh]\n")
    glob+= round(kwh,1)
    contador_integrante += 1

print (f"El gasto total semanal Familiar es de: {glob} [kwh], Recordar que se agregó el uso del refrigerador :)\n\nGracias por utilizar este programa :D")