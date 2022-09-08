
#!/usr/bin/python

#Fråga Klaudia om hon är hungrig

svar = input('Är Klaudia Hungrig?')


#skriv ut mata Klaudia om svar 'ja'. skriv ut 'Klaudia är mätt' om svaret är nej
#Annars, Skriv ut 'Förstår ej'.


if svar.lower() == 'ja': 
 print(f'Hon sa {svar}, Mata henne annars blir hon grinig')
elif svar.lower() == 'nej':
 print(f'Hon sa {svar}, bra')
else:
 print('Förstår ej svar')

print('***Då är vi klara för idag***')


