# PROJETO INTERDISCIPLINAR
# Conversão de Decimal para: Binário, Octal e Hexadecimal
# TURMA 1H (Noturno - ADS)

#NOME:            RGM:
# Matheus Gondim: 29606420
# Estevão Basso: 27789144
# Igor Fernandes: 30033799
# Diego Canha: 299003831
# Flávio Avelar: 29592861
# Rafael Dantas: 24429732



while True:
    # ENTRADA
    n = int(input('Digite um número Decimal para conversão: '))
    pgnt = pgtn = str(input('[1] - Binário\n[2] - Octal\n[3] - Hexadecimal\n[4] - Sair\nDigite a opção que deseja converter: '))

    #DEC - BINÁRIO
    if pgnt == '1':
        x=n
        k=[]
        while (n>0):
            a=int(float(n%2))
            k.append(a)
            n=(n-a)/2
        k.append(0)
        string = ''
        for j in k[::-1]:
            string = string+str(j)
        print('Valor convertido em Binário é:', string)

    # DEC - OCTAL
    elif pgnt == '2':
        string = ''
        while n > 0:
            remainder = n%8
            n = n // 8
            string = str(remainder) + string
        print('Valor convertido em Octal é:', string)

    # DEC - HEXADECIMAL
    elif pgnt == '3':
        he = ''
        dic = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

        while(n != 0):
            c = n%16
            he = dic[c] + he
            n = int(n/16)
        print(f'Valor convertido em Hexadecimal é:', he)
        
    elif pgtn == '4': break

    else:
        print('Digite uma opção válida!')
