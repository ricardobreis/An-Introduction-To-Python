## Exercise 1
Build a Python program that tests if an integer is prime.
Use a FOR loop.

## Exercise 1
print('Digite um número inteiro:')
n = int(input())
prime = True

for i in range(2,n-1):
        if n % i == 0:
            prime = False
            break
        
if prime: 
    print('O número é primo.')
else: 
    print('O número não é primo.')

## Exercise 2
Build a Python program that tests if an integer is prime.
Use a WHILE loop.

## Exercise 2
print('Digite um número inteiro:')
n = int(input())
prime = True
divider = 2 

while (divider < n) and prime:
    if n % divider == 0:
        prime = False
    divider = divider + 1

if prime: 
    print('O número é primo.')
else: 
    print('O número não é primo.')
