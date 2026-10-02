while True:
    try:
        numero = int(input("digite um número para ver sua tabuada:"))
        break
    except ValueError:
        print("apenas números inteiros")

for i in range(1,11):
    R=numero * i
    print(f"{numero} X {i} = {i * numero}")
    