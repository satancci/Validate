def check(cpf):
    if len(cpf) != 14 and len(cpf) != 11:
        return print('Erro: cpf com tamanho inválido.') 
    cpf = cpf.replace('.', '').replace('-', '') if len(cpf) == 14 else cpf
    penultimo = digito(soma(cpf)%11)
    ultimo = digito((soma(cpf, 1) + penultimo*2)%11)
    return True if cpf[9] + cpf[10] == f'{penultimo}{ultimo}' else False
def digito(vare):
    return 11-vare if vare >= 2 else 0
def soma(cpf, add=0):
    return sum(int(cpf[i])*(10+add-i) for i in range(9))