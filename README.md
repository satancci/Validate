# Validador de Documentos e Códigos

Este projeto fornece um conjunto de ferramentas para validação de diversos tipos de identificadores e códigos, incluindo CNPJ, CPF, EAN, ISBN e UPC. A biblioteca é escrita em Python e oferece métodos para verificar a validade desses identificadores de forma simples e eficiente.

## Funcionalidades

- **Validação de CNPJ** (Cadastro Nacional da Pessoa Jurídica)
- **Validação de CPF** (Cadastro de Pessoas Físicas)
- **Validação de EAN** (European Article Number)
- **Validação de ISBN** (International Standard Book Number)
- **Validação de UPC** (Universal Product Code)

## Requisitos

- Python 3.10 ou superior

## Instalação

Clone o repositório e instale usando `pip` (não há dependências necessárias):

```bash
git clone https://github.com/satancci/autocheck.git
```
## Uso

O módulo de validação pode ser usado diretamente importando as classes para validar CNPJ, CPF, EAN, ISBN e UPC. Veja os exemplos abaixo para saber como usar as classes de validação.

```python
from validate import cnpj, isbn, cpf, upc, ean

# Validar CNPJ (Cadastro Nacional da Pessoa Jurídica)
ex = "12.345.678/0001-95" # com ou sem pontuação 
print(cnpj.check(ex))  # Saída: True ou False

# Validar CPF (Cadastro de Pessoas Físicas)
ex = "123.456.789-09" # com ou sem pontuação
print(cpf.check(ex))  # Saída: True ou False

# Validar EAN (European Article Number)
ex = "1234567890123"  
print(ean.check(ex))  # Saída: True ou False

# Validar ISBN (International Standard Book Number)
ex = "978-3-16-148410-0"  # com ou sem pontuação
print(isbn.check(ex))  # Saída: True ou False

# Validar UPC (Universal Product Code)
ex = "012345678912"
print(upc.check(ex))  # Saída: True ou False

# Validar listas e matrizes de códigos
ex_lista = ["12.345.678/0001-95", "12.345.678/0001-96"]  # com ou sem pontuação
print(cnpj.checklist(ex_lista))  # Saída: lista composta por elementos booleanos (True ou False)

ex_matrix = [["1234567890123"], ["123456789012"]]  # com ou sem pontuação
print(ean.checkarray(ex_matrix))  # Saída: array bidimensional composta por elementos booleanos (True ou False)
```

## Métodos de Validação

Cada tipo de identificador possui uma classe correspondente com os seguintes métodos:

- **check(code: str) -> bool**: Valida um único código ou identificador.
- **checklist(codes: list) -> bool**: Valida uma lista de códigos.
- **checkarray(codes: list) -> bool**: Valida uma matriz de códigos.

### Notas Adicionais:

- **CNPJ (Cadastro Nacional da Pessoa Jurídica):** Identificador único de empresas e entidades no Brasil.
- **CPF (Cadastro de Pessoas Físicas):** Identificador único de cidadãos no Brasil.
