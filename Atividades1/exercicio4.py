print(
    "\t\t\nOla, como esta? Seja bem vindo e qualquer erro no programa contate o adminstrador!")
print(
    "\t\nHoje verificaremos e informaremos o quanto resultara o seu salario no fim do mes, com base nas suas vendas, comissoes e salario fixo!")


print(
    "\nPrimeiro, informe o seu nome")
name = input()

print(
    "\nAgora, informe qual o seu salario fixo")
fixsalary = input()

print(
    "\nInforme tambem, o numero de vendas que fez nesse mes")
sales = input()

commission = float(fixsalary) * 0.15
finalsalary = (float(commission) * float(sales)) + float(fixsalary)

print(
    "\nInformativo final :")
print(
    "\nNome do funcionario: ", name)
print(
    "\nSalario fixo: ", fixsalary, "reais")
print(
    "\nSalario final: ", finalsalary, "reais", "\n")
