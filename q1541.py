import math
def build()
  while True:

    data = list(map(int, input().split()))
    if data[0] == 0:
        break
    a = data[0]
    b = data[1]
    c = data[2]
    print(math.floor(math.sqrt((a * b * 100) / c)))
