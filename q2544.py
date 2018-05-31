def ilusão():
  while True:
      try:
          ativar= int(input())
      except EOFError:
          break
      clones = 0
      clonar = 1  
      if clonar == ativar: 
          print(0)
      else:
          while clonar != ativar:  
              clones += 1  
              clonar *= 2  
          print(clones)
