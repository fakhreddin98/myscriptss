#!/usr/bin/python

#Fråga Klaudia om hon är hungrig

nuTemp = input('Hur många grader är det? \n')


if nuTemp < '25':
 print(f'Tempen är {nuTemp} mindre än 25, Sätt på värme ')
elif nuTemp > '25':
 print(f'Tempen är {nuTemp} större än 25, Stäng av värme')
elif nuTemp == '25':
 print(f'perfekt tempen är {nuTemp} behöver inte göra något')
else:
 print('Förstår ej svar')



