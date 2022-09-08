#!/usr/bin/python

numbersToTest = int (input('Hur många tal vill du undersöka'))


for i in range(1,numbersToTest+1):
 provenNotPrime = False
 for k in range(2,i):
  if i % k == 0:
   print(f'{i} ej ett primtal')
   provenNotPrime = True
   break
 if provenNotPrime == False:
  print(f'*** {i} är ett Primtal! ***')
