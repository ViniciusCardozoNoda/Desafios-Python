print(20*'-=-')
print('Criando um Menu de Opções')
print(20*'-=-')
from time import sleep
primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: ')) 
escolha = 0
maior = 0
menor = 0
while escolha != 5:
    print('''        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] sair do programa''' )
    escolha = (int(input('>>>>> Qual é a sua opção? ')))
    if escolha == 1:
        escolha == 1
        somar = primeiro + segundo
        print('A soma entre {} + {} é {}'.format(primeiro, segundo, somar))
        print(10*'=-==')
    if escolha == 2:
        escolha == 2
        somar2 = primeiro * segundo
        print('O resultado de {} x {} é {}'.format(primeiro, segundo, somar2))
        print(10*'=-==')
    if escolha == 3:
        if primeiro > segundo:
            maior = primeiro
        else:
            maior = segundo
        print('Entre {} e {} o maior valor é {}'.format(primeiro, segundo, maior))
        print(10*'=-==')
    if escolha == 4:
        print('Informe os números novamente:')
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: '))
        print(10*'=-==')
    if escolha > 5:
        print('Opção inválida. Tente novamente ')
        print(10*'=-==')
    elif escolha == 5:  
            escolha == 5
            print('Finalizando...')
            sleep(2)
            print(10*'=-==')
            print('Fim do programa! Volte sempre!')
