print(
    "\t\nOla, bem vindo! Hoje faremos uma simulação de rendimento do seu deposito, que rende 0,70% ao mes!")

print(
    "\nPrimeiro, informe o valor que ira depositar: ")
dep = input()

rend = (float(dep)*0.007) + float(dep)

print(
    "\nO valor final ao mes da sua operacao, considerando rendimentos, sera de: ", rend, "\n")
