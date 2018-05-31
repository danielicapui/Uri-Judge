def q1001(a,b):
  x=a+b
  return("X =",x)
 
def q1002(r):
  n=3.14159
  a=n*(r**2)
  return("A={:.4f}".format(a))
 
def q1003(a+b):
  SOMA=a+b
  return("SOMA =", SOMA)
  
def q1004(a,b):
  PROD=a*b
  return("PROD =", PROD)
  
def q1005(a,b):
  MEDIA=((3.5*a)+(7.5*b))/11
  return("MEDIA = {:.5f}".format(MEDIA))
  
def q1006(a,b,c):
  MEDIA=((2*a)+(3*b)+(5*c))/10
  return("MEDIA = {:.1f}".format(MEDIA))

def q1007(a,b,c,):
  DIFERENCA=(a*b-c*d)
  print("DIFERENCA =", DIFERENCA)

def q1008(a,b,c):
  print("NUMBER =", a)
  SALARY= b*c
  print("SALARY = U$ {:.2f}". format(SALARY))
  
def q1009():
  a=input()
  b=float(input())
  c=float(input())
  d=float(c*0.15)
  TOTAL= d+b
  print("TOTAL = R$ {:.2f}". format(TOTAL))

def q1010():
  linha1 = input().split(" ")
  linha2 = input().split(" ")

  cod1, qtde1, valor1 = linha1
  cod2, qtde2, valor2 = linha2

  total = (int(qtde1) * float(valor1)) + (int(qtde2) * float(valor2))

  print("VALOR A PAGAR: R$ %0.2f" %total)
