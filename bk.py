import math
a = int(input("digite o valor de a" ))
b = int(input("digite o valor de b" ))
c = int(input("digite o valor de c" ))
delta = b**2 - 4*a*c

if delta>0:
    bk1=-b + math.sqrt((b**2-4*a*c))
    bk2 = bk1/2*a
    bk3=-b - math.sqrt((b**2-4*a*c))
    bk4 = bk3 /2*a
    print(bk2,bk4)

if delta==0:
    bk5 = -b/2*a
    print("delta0", bk5)

if delta<0:
    print("nao tem valor real cria")
    



