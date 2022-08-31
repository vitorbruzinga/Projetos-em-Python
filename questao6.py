print(
    "\t\nOla, bem vindo! Hoje faremos uma simulação de valor de venda de um produto, de acordo com o preco de custo e margem de lucro desejada!")

print(
    "\nPrimeiro, informe o preco de custo do produto em questao(Em reais): ")
custeprice = input()

print(
    "\nAgora, informe quantos % de lucro tera de margem nesse produto(Digite apenas numeros, o programa converte para porcentagem automaticamente!) :")
marginlucro = input()

porcmargin = (float(marginlucro))/(100)

salevalue = float(custeprice) + (float(porcmargin)*float(custeprice))

print(
    "\nO valor de venda desse produto, sera de: ", salevalue, "\n")
