print(20*'-=-')
print('Análise de dados do grupo')
print(20*'-=-')
print('-' * 25)
print('CADASTRE UMA PESSOA')
print('-' * 25)
tot = tot2 = tot3 = sexo = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper() [0]
    if idade > 18:
        tot += 1
    if sexo in 'Mm':
        tot2 += 1
    if sexo in 'Ff' and idade < 20:
        tot3 += 1
    print('-' * 25)
    cont = str(input('Quer continuar? [S/N] ')).strip().upper() [0]
    print('-' * 25)
    if cont not in 'Ss':
        break
print(f'Total de pessoas com mais de 18 anos: {tot}')
print(f'Ao todo temos {tot2} homens cadastrados')
print(f'E temos {tot3} mulheres com menos de 20 anos')
