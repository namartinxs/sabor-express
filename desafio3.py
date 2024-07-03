list_numeros =  []
total = 0
for i in range(1,11):
  list_numeros.append(i)
    
for numero in list_numeros:
  if numero % 2 == 0:
    continue
  else:
    total += numero

print(total)