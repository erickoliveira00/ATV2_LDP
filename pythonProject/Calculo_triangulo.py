a = int(input('Digite o primeiro lado do triângulo, A:'))
b = int(input('Digite o segundo lado do triângulo, B:'))
c = int(input('Digite o terceiro lado do triângulo, C:'))

if a > b + c :
    print('Os valores digitados não formam um triângulo !!!')
else:
     p = (a + b + c)/2
     area = ( p * ( p - a ) * ( p - b ) * ( p -c ) ) **0.5
     print(f' A área do triangulo é:{area:.2f}')
