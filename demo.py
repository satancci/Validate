from validate import cpf, cnpj, isbn, ean, upc
print(cpf.check('811.260.180-15'))  # saída: True
print(cpf.checklist(['05746029219', '247.593.160-43', '811.260.180-15']))  # saída: [True, True, True]
print(cnpj.checklist(['58.582.487/0001-48', '06.217.917/0001-29', '22.244.177/0001-76']))  # saída: [True, True, True]
print(isbn.checklist(['978-0-306-40615-7', '978-0-538-49887-6', '9788522106608']))  # saída: [True, True, True]
print(upc.checklist(['012345678912', '423242324237', '042000011112']))  # saída: [True, True, True]# saída True
print(upc.checkarray([['012345678912', '423242324237', '042000011112'], ['012345678912', '423242324237', '042000011112']]))  # saída: [[True, True, True], [True, True, True]]
print(ean.checkarray([['4006381333931', '9780201379624', '4232423242330'], ['4006381333931', '9780201379624', '4232423242330']]))  # saída: [[True, True, True], [True, True, True]]
