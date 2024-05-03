#ESTRUCTURA DE CONTROL
a=5
b=10
#IF
if a<b:
    print("a es menor que b")
    #hacer algo
elif a>b:
    print("a es mayor que b")
    #hacerotra cosa
else:
    print("a y b son iguales")
    #hacer algo por defecto

#For
numeros=[1,2,3,4,5]
for n in numeros:
    print(n)

for i in range(0,10,2):
    print(i)

#WHILE
x=1
while x < 5:
    print(x)
    x+=1