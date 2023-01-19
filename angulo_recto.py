#Le pedimos al usuario que entre los 3 lados
lado=0
lista=[]
angulo_recto = None
for i in range(3):
    lado = float(input("Introducir longitud de Lado: "))
    lista.append(lado)
lado_mayor=max(lista)
lista.remove(lado_mayor)
if (lado_mayor * 2) == ((lista[0]*2) + (lista[1]*2)):
    angulo_recto = True
    print(angulo_recto)
else:
    angulo_recto = False
    print(angulo_recto)
