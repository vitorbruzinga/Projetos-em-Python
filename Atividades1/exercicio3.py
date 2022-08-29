print(
    "\t\t\nOlá, bem vindo! \t\nPara que não haja erros nesse programa, preciso que digite apenas numeros e pressione enter depois de digitar! \nObrigado :D")
print(
    "\t\nHoje verificaremos o quanto seu carro consumiu em media, com base na distancia que voce percorreu e em quanto combustivel gastou!")

print(
    "\nInforme a distancia percorrida em km")
distance = input()

print(
    "\nAgora, informe quantos litros de combustivel foram consumidos nessa distancia")
consume = input()

consumo_medio = float(distance)/float(consume)

print(
    "\t\nSeu veiculo teve um consumo medio de :", consumo_medio, " km/L ")
