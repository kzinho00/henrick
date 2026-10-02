notas = {"Ana": 8.5, "Pedro": 6.0, "Maria": 9.0, "João":5.5}

nota = 0

for i in notas.values():
    nota += i

media = nota / len(notas)

print(media)