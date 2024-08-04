def check(variable):
    if len(variable) != 13: 
        return print('Erro: CNPJ com tamanho inválido.')
    digito = sum(int(variable[i]) * 3 if i%2 else int(variable[i]) for i in range(12))%10
    digito = 10-digito if digito !=0 else digito
    return False if variable[12] != str(digito) else True