from dataclasses import dataclass

@dataclass
class cpf:
    @classmethod
    def check(cls, cpf: str) -> bool:
        if len(cpf) != 14 and len(cpf) != 11:
            return print('Erro: CPF com tamanho inválido.') 
        cpf = cpf.replace('.', '').replace('-', '') if len(cpf) == 14 else cpf
        penultimo = cls.__digito(cls.__soma(cpf)%11)
        ultimo = cls.__digito((cls.__soma(cpf, 1) + penultimo*2)%11)
        return True if cpf[9] + cpf[10] == f'{penultimo}{ultimo}' else False
    def __digito(vare):
        return 11-vare if vare >= 2 else 0
    def __soma(cpf, add=0):
        return sum(int(cpf[i])*(10+add-i) for i in range(9))
    @classmethod
    def checklist(cls, cpfs: list) -> bool:
        return validalista(cls, cpfs)
    @classmethod
    def checkarray(cls, cpfs: list) -> bool:
        return validamatriz(cls, cpfs)

@dataclass
class cnpj:
    @classmethod
    def check(cls, cnpj: str) -> bool:
        if len(cnpj) != 18 and len(cnpj) != 14:
            return print('Erro: CNPJ com tamanho inválido.')
        cnpj = cnpj.replace('.', '').replace('-', '').replace('/','') if len(cnpj) == 18 else cnpj
        penultimo = cls.__digito(cls.__soma(cnpj, 1)%11)
        ultimo = cls.__digito((cls.__soma(cnpj)+penultimo*2)%11)
        return True if cnpj[12] + cnpj[13] == f'{penultimo}{ultimo}' else False
    def __digito(vare):
        return 11-vare if vare >= 2 else 0
    def __soma(cnpj, add = 0, ref = '6543298765432'):
        return sum(int(cnpj[i])*(int(ref[i+add])) for i in range(12))
    @classmethod
    def checklist(cls, cnpjs: list) -> bool:
        return validalista(cls, cnpjs)
    @classmethod
    def checkarray(cls, cnpjs: list) -> bool:
        return validamatriz(cls, cnpjs)

@dataclass
class isbn:
    def check(isbn: str) -> bool:
        return geral(isbn.replace('-', '') if len(isbn) == 17 else isbn)
    @classmethod
    def checklist(cls, isbns: list) -> bool:
        return validalista(cls, isbns)
    @classmethod
    def checkarray(cls, isbns: list) -> bool:
        return validamatriz(cls, isbns)

@dataclass
class upc:
    def check(upc: str) -> bool:
        if len(upc) != 12: 
            return print('Erro: CNPJ com tamanho inválido.')
        digito = sum(int(upc[i]) * 3 if not i%2 else int(upc[i]) for i in range(11))%10
        digito = 10-digito if digito !=0 else digito
        return False if upc[11] != str(digito) else True
    @classmethod
    def checklist(cls, upcs: list) -> bool:
        return validalista(cls, upcs)
    @classmethod
    def checkarray(cls, upcs: list) -> bool:
        return validamatriz(cls, upcs)

@dataclass
class ean:
    def check(ean: str) -> bool:
        return geral(ean)
    @classmethod
    def checklist(cls, eans: list) -> bool:
        return validalista(cls, eans)
    @classmethod
    def checkarray(cls, eans: list) -> bool:
        return validamatriz(cls, eans)
 
######ignore######ignore######ignore######ignore######ignore######ignore######ignore######
def geral(variable):
    if len(variable) != 13: 
        return print('Erro: CNPJ com tamanho inválido.')
    digito = sum(int(variable[i]) * 3 if i%2 else int(variable[i]) for i in range(12))%10
    digito = 10-digito if digito !=0 else digito
    return False if variable[12] != str(digito) else True
def validalista(cls, algo):
    resultado = [cls.check(elemento) for elemento in algo]
    return resultado
def validamatriz(cls, linha):
    resultado = [validalista(cls, algo)for algo in linha]
    return resultado
######ignore######ignore######ignore######ignore######ignore######ignore######ignore######