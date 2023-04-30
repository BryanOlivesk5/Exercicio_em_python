numero = input('Digite um numero aqui: ')

if numero.isdigit():
    int_numero = int(numero)
    par_impar = int_numero % 2 == 0

    if par_impar:
        par_impar = 'par'
    else:
        par_impar = 'ímpar'  

    print(f'O número {int_numero} é um número {par_impar}')

else:
    print('Você não digitou um número inteiro')