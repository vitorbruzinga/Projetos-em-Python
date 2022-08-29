print(
    "\t\t\nOla, como esta? Seja bem vindo e qualquer erro no programa contate o adminstrador!")
print(
    "\t\nHoje verificaremos e informaremos a media final do aluno com base em suas 3 provas feitas no periodo! ")

print(
    "\nPrimeiro, digite o nome do aluno: ")
name = input()

print(
    "\nInforme a nota na primeira prova: ")
n1 = input()

print(
    "\nInforme agora, a nota na segunda prova: ")
n2 = input()

print(
    "\nE informe por fim, a nota na terceira prova prova: ")
n3 = input()

finalmedia = (float(n1)+float(n2)+float(n3))/3

print(
    "\t\nInformativo final: ")
print(
    "\t\nNome do aluno: ", name)
print(
    "\t\nMedia final do aluno: ", finalmedia, "\n")
