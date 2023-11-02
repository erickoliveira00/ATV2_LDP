a=int(input('Digite o primeiro número:'))
b=int(input('Digite o segundo número:'))
c=int(input('Digite o terceiro número:'))
menor=a
if b<a and b<c:
   menor=b
if c<b and c<a:
   menor=c

print(' O menor valor digitado foi:{}'.format(menor))
