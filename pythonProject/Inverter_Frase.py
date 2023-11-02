def inverter_frase(frase):
    return frase[::-1]

def main():
    frase = input('Digite uma frase para ser invertida: ')
    frase_invertida = inverter_frase(frase)
    print(f'Frase invertida: {frase_invertida}')

main()
