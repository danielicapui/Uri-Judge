import re
def data(loops):
  for i in range(loops):
      data = input()
      placa = re.compile('([A-Z]{3})-([0-9]{4})')  
      if placa.match(data) and len(data) == 8:
          ultimo = data[-1]
          if ultimo in ["1", "2"]:
              print("MONDAY")
          elif ultimo in ["3", "4"]:
              print("TUESDAY")
          elif ultimo in ["5", "6"]:
              print("WEDNESDAY")
          elif ultimo in ["7", "8"]:
              print("THURSDAY")
          elif ultimo in ["0", "9"]:
              print("FRIDAY")
      else:
          print("FAILURE")
