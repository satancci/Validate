from dataclasses import dataclass

@dataclass
class isbn:
    isbn: str
    def check(isbn) -> bool:
        if len(isbn) != 17 and len(isbn) != 13:
            return print('Erro: ISBN com tamanho inválido.')
        isbn = isbn.replace('-', '') if len(isbn) == 17 else isbn
        digito = sum(int(isbn[i]) * 3 if i%2 else int(isbn[i]) for i in range(12))%10
        digito = 10-digito if digito !=0 else digito
        return False if isbn[12] != str(digito) else True
    
@dataclass
class cpf:
    @classmethod
    def check(cls, cpf: str) -> bool:
        if len(cpf) != 14 and len(cpf) != 11:
            return print('Erro: CPF com tamanho inválido.') 
        cpf = cpf.replace('.', '').replace('-', '') if len(cpf) == 14 else cpf
        penultimo = cls.digito(cls.soma(cpf)%11)
        ultimo = cls.digito((cls.soma(cpf, 1) + penultimo*2)%11)
        return True if cpf[9] + cpf[10] == f'{penultimo}{ultimo}' else False
    def digito(vare):
        return 11-vare if vare >= 2 else 0
    def soma(cpf, add=0):
        return sum(int(cpf[i])*(10+add-i) for i in range(9))
    
@dataclass
class cnpj:
    @classmethod
    def check(cls, cnpj: str) -> bool:
        if len(cnpj) != 18 and len(cnpj) != 14:
            return print('Erro: CNPJ com tamanho inválido.')
        cnpj = cnpj.replace('.', '').replace('-', '').replace('/','') if len(cnpj) == 18 else cnpj
        penultimo = cls.digito(cls.soma(cnpj, 1)%11)
        ultimo = cls.digito(cls.soma(cnpj)%11)
        return True if cnpj[12] + cnpj[13] == f'{penultimo}{ultimo}' else False
    def digito(vare):
        return 11-vare if vare >= 2 else 0
    def soma(cnpj, add = 0, ref = '6543298765432'):
        return sum(int(cnpj[i])*(int(ref[i+add])) for i in range(12))