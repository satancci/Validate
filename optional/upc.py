def check(upc: str) -> bool:
    if len(upc) != 12: 
        return print('Erro: CNPJ com tamanho inválido.')
    digito = sum(int(upc[i]) * 3 if not i%2 else int(upc[i]) for i in range(11))%10
    digito = 10-digito if digito !=0 else digito
    return False if upc[11] != str(digito) else True