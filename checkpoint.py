listaEmails = []
inserir = "Sim"

while len(listaEmails) <= 30:
    listaEmails.append(input("Digite o email: ").lower())

while inserir == "Sim" and len(listaEmails) > 30:
    listaEmails.append(input("Digite o email: ").lower())
    inserir = input("Deseja cadastrar mais um email?")

emailBuscado = input("Qual é o email que está buscando? ")

if emailBuscado in listaEmails:
    print("O e-mail " + emailBuscado + " consta na lista.")
else:
    print("O email não existe.")




