condicao = True
valor = int(input("Digite o valor que deseja ser gerado a tabuada: "))
multiplicado = 1

for multiplicado in range(1, 11):
    if valor > 10: 
        while valor > 10:
            valor = int(input("Digite o valor que deseja ser gerado entre 1 à 10 somente: "))
        else:
            continue
    elif multiplicado <= 10:
        resultado = valor * multiplicado
        print(f"{valor} x {multiplicado} = {resultado}")
        multiplicado += 1
    else:
        break