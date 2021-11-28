print("Hola Mundo¡¡ Soy KW")

print("Hola Mundo")



# Soy un comentario
# COMENTARIO
# QUE LINDO COMENTARIO :p

"""
sOY MUCHO COMENTARIO
hOLA QUE HACE
"""

print("Chao Mundo")

""""

#VARIABLES: CAJAS DONDE GURADO COSAS


texto= "Repaso de Python con Victor"
nombre=" Victor Robles"
altura= "187cm"
year =2020


print(texto)
print(year)


#CONCATENAR


print(f"{texto}-{nombre}-{altura}")


print(f"{texto}-{nombre}-{altura} - {year}")
print(f"{texto}-{nombre}-{altura} - {str(year)}")

print(texto + "-" + nombre + "-" + altura + "-" + str(year) )



#ENTRADA

sitioweb = input("¿Cúal es tu sitio Web?:")
print("El sitio web es: " + sitioweb)


#CONDICIONESS

#IF
altura=input("¿Cual es tua altura:")
altura= int(altura)
if altura >80:
    print("Eres una persona alta")
else:
    print("Eres Bajito")


    #FUNCIONES


def mostratAltura():
    altura=input("¿Cual es tua altura:")
    altura= int(altura)
    alt=altura
    if altura >= 180:
        print("Eres alto")
    else:
        print("Erese bjaito")

    return altura

mostratAltura()

mostratAltura()


alt=mostratAltura()
def mostratAltura(alt):
    if alt >= 180:
        print("Eres alto")
    else:
        print("Erese bjaito")

mostratAltura(alt)

mostratAltura(alt)
"""
#LISTAS

personas= ["Victor", "Paco", "Pepe", "Lala", "Nene", "piña"]

print(personas[1])
print(personas[-2:3])
print(personas[:])
print(personas[4:])
print(personas[1:2]) # <-- Porque no imprime el 2? solo el 1 ?
print(personas[2])


for prsona in personas:
    print("-" + prsona)