print(
    "\t\nOla, bem vindo! Hoje faremos uma simulação de valor do custo de um carro ao consumidor, com base nos custos de fabrica e nos lucros do destribuidor!")

print(
    "\nPrimeiro, informe o custo de fabrica do carro que possui interesse: ")
custecar = input()

porcdist = (float(custecar) * 0.28)
imposts = (float(custecar) * 0.45)
fynalcust = (float(custecar) + float(porcdist) + float(imposts))

print(
    "\nO custo final do carro, para o consumidor e de: ", fynalcust, "\n")

print(
    "\nInformativo detalhado: ")
print(
    "\nPreco de fabrica: ", custecar)
print(
    "\nImpostos: ", imposts)
print(
    "\nLucro do distribuidor: ", porcdist)
print(
    "\nCusto final ao consumidor: ", fynalcust, "\n")
