print(20*'-=-')
print('Estatísticas em produtos')
print(20*'-=-')
print('-' * 35)
print('LOJA SUPER BARATÃO')
print('-' * 35)
tot = preço = produto = tot2 = tot3 = cont = 0
barato = ''
while True:
    nome = str(input('Nome do Produto: '))
    pre = int(input('Preço: R$'))
    cont = +1
    if pre > 0:
        preço += pre
    if pre >= 1000:
        tot2 += 1
    if cont == 1:
        produto = cont
        barato = nome
    else:
        if cont < produto:
            produto = cont
            barato = nome
    cont = (str(input('Quer continuar? [S/N] '))).strip().upper() [0]
    if cont not in 'Ss':
        break
print(11*'-', 'FIM DO PROGRAMA', 11*'-') 
print(f'O total de compra foi {preço:.2f}')
print(f'Temos {tot2} custando mais de 1000.00')
print(f'O produto mais barato foi {barato} que custa {produto:.2f}')
