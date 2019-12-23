# A função confere_CPF recebe como parâmetro uma string
# com o CPF (sem pontos ou hífen). 
# Retorna True se o CPF for válido.

# Função para testar se os números do CPF são iguais
def caracteresIguais(s) : 
    n = len(s) 
    for i in range(1, n) : 
        if s[i] != s[0] : 
            return False
  
    return True

def confere_CPF(cpf): 
  if (len(cpf) != 11 or not cpf.isdigit() or caracteresIguais(cpf)):
    return False

  a=10
  total=0
  for i in range(0,9):
    total=total+int(cpf[i])*a
    a=a-1
  digito_1= 0 if int(total%11) == 0 or int(total%11) == 1 else 11 - int(total%11)
  
  a=11
  total=0
  for i in range(0,10):
    total=total+int(cpf[i])*a
    a=a-1
  
  digito_2= 0 if int(total%11) == 0 or int(total%11) == 1 else 11 - total%11
  return (int(cpf[9]) == int(digito_1) and int(cpf[10]) == int(digito_2))

# Programa principal para testar a função confere_CPF.

x = "12345678909"
resultado = confere_CPF(x)
print(resultado)
