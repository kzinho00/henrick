boletim = []



while True:
    escolha = str(input("você deseja adicionar um aluno? \n1-Sim \n2-Não \n:"))
    
    if escolha == '1':
        nome = input("digite o nome do aluno:")
        
    
        try:
            nota = float(input("digite a nota do aluno:"))
        except ValueError:
            print("digite apenas uma nota válida")
            continue
        
        aluno ={"nome": nome, "nota": nota}
        boletim.append(aluno)
        print(f"aluno {aluno} adicionado")
    
    elif escolha == '2':
        print("encerrando...")
        break
        
    else:
        print("opção inválida")

for aluno in boletim:
    if aluno["nota"] >= 60:
        print(f"aluno {aluno['nome']} aprovado")
        print(boletim)
    else:
        print(f"aluno {aluno['nome']} reprovado")
        print(boletim)
