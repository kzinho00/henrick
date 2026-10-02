produtos = [
    {"nome" : "computador", "preco" : 80.00},
    {"nome" : "monitor", "preco" : 120.00},
    {"nome" : "mouse","preco" : 20.00},
]

for i in produtos:
    if i["preco"] > 50.00:
        print(i["nome"])
