while True:
    try:
        numero = int(input("digite um número inteiro:"))
        break
    
    except ValueError:
        print("digite apenas números inteiros:")

if numero % 2 == 0:
    print(f"{numero} é par")
else:
    print(f"{numero} é ímpar")