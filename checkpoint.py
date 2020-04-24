listaEmails = []
inserir = "Sim"
naLista = "Sim"

while inserir == "Sim":
    listaEmails.append(input("Digite o email: ").lower())
    inserir = input("Deseja cadastrar mais um email?")

pergunta = input("Qual é o email que está buscando? ")

for email in listaEmails:
    if pergunta == email:
        print(email)
    else:
        print("O email não existe.")




