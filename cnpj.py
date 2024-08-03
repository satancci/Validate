def check(cnpj):
    if len(cnpj) != 18 and len(cnpj) != 14:
        return print('Erro: CNPJ com tamanho inválido.')
    cnpj = cnpj.replace('.', '').replace('-', '').replace('/','') if len(cnpj) == 18 else cnpj
    penultimo = digito(soma(cnpj, 1)%11)
    ultimo = digito(soma(cnpj)%11)
    return True if cnpj[12] + cnpj[13] == f'{penultimo}{ultimo}' else False
def digito(vare):
    return 11-vare if vare >= 2 else 0
def soma(cnpj, add = 0, ref = '6543298765432'):
    return sum(int(cnpj[i])*(int(ref[i+add])) for i in range(12))