n1=float(input("insira 4 numeros: "))
n2=float(input())
n3=float(input())
n4=float(input())
produto=(n1*n2*n3*n4)
print(f"o produto é {produto}")
if produto>0:
    print(f"o produto é positivo")
elif produto<0:
    print("o produto é negativo")