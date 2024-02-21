class Producto:
    def __init__(self, codigo, precio):
        self.codigo = codigo
        self.precio = precio

A = Producto("A",2.00) # 4 por $7
B = Producto("B",12.00)
C = Producto("C",1.25) #6 por $6
D = Producto("D",0.15)

cant = int(input("Ingrese la cantidad de productos a scanear: "))
lista = []
while(cant > 0):
    scan = input("Ingrese el codigo de su producto(A,B,C,D): ")
    if scan == 'A':
        lista.append(A.precio)
    elif scan == 'B':
        lista.append(B.precio)
    elif scan == 'C':
        lista.append(C.precio)
    elif scan == 'D':
        lista.append(D.precio)
    else:
        print("Codigo incorrecto")
    cant -= 1

suma_total = 0
descuento = 0
countA = 0
countC= 0
for i in lista:
    suma_total += i
print(suma_total)

# Se intentó... 
 ''' for i in lista:
    suma_total += i
    if(lista[i] == 'A'):
        countA +=1
    if(lista[i] == 'C'):
        countC += 1

if(countA == 4):
    suma_total -= 1
if(countC == 6):
    suma_total -= 1.5
print(suma_total) '''