def check(isbn):
    if len(isbn) != 17 and len(isbn) != 13:
        return print('Erro: ISBN com tamanho inválido.')
    isbn = isbn.replace('-', '') if len(isbn) == 17 else isbn
    digito = sum(int(isbn[i]) * 3 if i%2 else int(isbn[i]) for i in range(12))%10
    digito = 10-digito if digito !=0 else digito
    return False if isbn[12] != str(digito) else True