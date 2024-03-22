entrada = int(input("Digíte um número: "))
while entrada != 0:
  for x in range(1,11):
    print(f'{entrada} x {x} = {entrada*x}')
  print('=' * 20)
  entrada = int(input("Digíte um número: "))
print('Fim da tabuada')