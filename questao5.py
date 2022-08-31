print(
    "\t\t\nOla, uma novidade! A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco) prestações sem juros, simule aqui!")

print(
    "\nPara simularmos, insira o valor da compra que deseja parcelar: ")
value1 = input()

parcelas = (float(value1)/(5))

print(
    "\nCada parcela dessa compra ficara no valor de R$: ", parcelas, "\n")
