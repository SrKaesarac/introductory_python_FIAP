print("Hello World!")
nome = "Augusto Cesar"
empresa = 'Taxinha'
qtde_funcionarios = 50
mediaSalarios = 4000.25

print(nome + " trabalha na Empresa " + empresa)
print("Possui: ", qtde_funcionarios, " funcionarios.")
print("A media dos salarios e de: ", mediaSalarios)

nome = input("Digite um funcionário: ")
empresa = input("Digite a instituição: ")
qtde_funcionarios = int(input("Digite a qtde de funcionários: "))
mediaSalarios = float(input("Digite a média da mensalidade: "))
print(nome + " trabalha na empresa " + empresa)
print("Possui: ", qtde_funcionarios, " funcionarios.")
print("A média dos salarios e de: " + str(mediaSalarios))