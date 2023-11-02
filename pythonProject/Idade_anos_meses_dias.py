idade = int(input('Digite sua Idade em dias:'))

def calcular_idade (idade):
    anos = idade // 365
    meses = (idade % 365) // 30
    dias = (idade % 365) % 30
    return anos, meses, dias

anos, meses, dias = calcular_idade(idade)
print(f'Sua idade é: {anos} anos, {meses} meses, {dias} dias')



