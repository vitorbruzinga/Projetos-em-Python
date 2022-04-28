

print('\t\t\tNesse programa voce verifica se o seu carro tera um melhor custo-beneficio com alcool ou com etanol')
print('\nNesse site, caso voce nao saiba, ha o consumo do seu carro em etanol e em gasolina, caso precise, copie e cole no seu navegador e depois retorne aqui! Link: https://combustivel.app/carros')

consumogc = input(
    "\nFeito isso, informe o consumo que seu veiculo faz na cidade com gasolina(em km/l):")
consumoec = input(
    "\nAgora, informe o consumo que seu veiculo faz na cidade com etanol(em km/l):")

consumoge = input(
    "\nFeito isso, informe o consumo que seu veiculo faz na estrada com gasolina(em km/l):")
consumoee = input(
    "\nAgora, informe o consumo que seu veiculo faz na estrada com etanol(em km/l):")

precog = input(
    "\nAgora, informe o preco da gasolina no seu posto de confianca:")
precoe = input("\nAgora, informe o preco do etanol no seu posto de confianca:")

custobeneficio1 = float(consumogc) * float(precog)
custobeneficio2 = float(consumoec) * float(precoe)

custobeneficio3 = float(consumoge) * float(precog)
custobeneficio4 = float(consumoee) * float(precoe)


if custobeneficio1 > custobeneficio2 and custobeneficio3 > custobeneficio4:
    print('\n\t\tPara o seu veiculo, no dia de hoje, com esses precos e considerando o consumo informado, para rodar na CIDADE é mais economico abastecer com GASOLINA e para rodar na ESTRADA tambem GASOLINA!')

elif custobeneficio1 > custobeneficio2 and custobeneficio4 > custobeneficio3:
    print('\n\t\tPara o seu veiculo, no dia de hoje, com esses precos e considerando o consumo informado, para rodar na CIDADE é mais economico abastecer com GASOLINA, porem, na ESTRADA sera mais economico abastecer com ETANOL!')

elif custobeneficio2 > custobeneficio1 and custobeneficio4 > custobeneficio3:
    print('\n\t\tPara o seu veiculo, no dia de hoje, com esses precos e considerando o consumo informado, para rodar na CIDADE é mais economico abastecer com ETANOL, e na ESTRADA sera mais economico tambem abastecer com ETANOL!')

elif custobeneficio2 > custobeneficio1 and custobeneficio3 > custobeneficio4:
    print('\n\t\tPara o seu veiculo, no dia de hoje, com esses precos e considerando o consumo informado, para rodar na CIDADE é mais economico abastecer com ETANOL, porem, na ESTRADA sera mais economico abastecer com GASOLINA!')
