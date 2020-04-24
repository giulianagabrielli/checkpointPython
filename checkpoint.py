listaEmails = []
inserir = "S"

while len(listaEmails) <= 30:
    listaEmails.append(input("Digite o email: ").lower())

while inserir == "S" and len(listaEmails) > 30:
    listaEmails.append(input("Digite o email: ").lower())
    inserir = input("Deseja cadastrar mais um email? (S / N)").upper()

emailBuscado = input("Qual é o email que está buscando? ")

if emailBuscado in listaEmails:
    print("O e-mail " + emailBuscado + " consta na lista.")
else:
    print("O email não existe.")




