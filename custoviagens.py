print('\t\t\tNesse programa voce verifica o custo da sua viagem, seja com gasolina ou com Etanol')

distancia = input(
    "\nPrimeiro, informe de quantos km sera a sua viagem(ida e volta):")

precog = input(
    "\nAgora, informe o preco da gasolina no posto que ira abastecer seu veiculo:")
precoe = input("\nInforme tambem, o preco do etanol no mesmo posto:")

consumog = input(
    "\nFeito isso, informe o consumo que seu veiculo faz na estrada com gasolina(em km/l):")
consumoe = input(
    "\nAgora, informe o consumo que seu veiculo faz na estrada com etanol(em km/l):")

custo1 = float(distancia) / float(consumog) * float(precog)
margem_de_erro1 = (custo1 * 0.3) + custo1

custo2 = float(distancia) / float(consumoe) * float(precoe)
margem_de_erro2 = (custo2 * 0.3) + custo2


print('\n\nO custo de sua viagem com abastecimento em gasolina sera de:',
      "%.2f" % custo1, ' reais!')
print('\nObservacao: Para a sua segurança, consideramos uma margem de erro que considera 30 por cento do valor, devido a fatores que alteram o consumo, como rapida ou lenta velocidade, ar condicionado e etc... ')
print('\nPor tanto, o preco estimado com a margem de seguranca e de:',
      "%.2f" % margem_de_erro1, "reais!(gasolina)")


print('\n\nO custo de sua viagem com abastecimento em etanol sera de:',
      "%.2f" % custo2, ' reais!')
print('\nObservacao: Para a sua segurança, consideramos uma margem de erro que considera 30 por cento do valor, devido a fatores que alteram o consumo, como rapida ou lenta velocidade, ar condicionado e etc... ')
print('\nPor tanto, o preco estimado com a margem de seguranca e de:',
      "%.2f" % margem_de_erro2, "reais!(etanol)")
