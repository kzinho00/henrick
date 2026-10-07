nome = str(input("digite uma palavra:"))
vogal = []

vop = ['a','e','i','o','u']

for letra in nome:
    if letra in vop:
        print(f"'{letra}' é uma vogal")
        vogal.append(letra)

print(vogal)