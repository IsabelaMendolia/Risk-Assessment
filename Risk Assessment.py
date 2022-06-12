name = input('name: ')
age = int(input('age: '))

print('\ndo you have any of these symptoms and or habits?')
fever = int(input('fever (0= no, 1= yes): '))
cough = int(input('cough (0= no, 1= yes): '))
sob = int(input('shortness of breath (0= no, 1= yes): '))
sore = int(input('sore throat or runny nose (0= no, 1= yes): '))
vomit = int(input('vomiting (0= no, 1= yes): '))
ill = int(input('Diabetes, Kidney, or Heart Disease, Smoker over 75 (0= no, 1= yes): '))
immune = int(input('Is Your Immune System weak or compromised (0= no, 1= yes): '))
epi = int(input('Have you been in an epidemic region, or in contact with person from that region in last 14 days (0= no, 1= yes): '))



print('\nRisk Assessment:, Dear', name,)
print('You have risk of infection, you should wear an N-95 mask outdoors and remain isolated until your C-19 test is confirmed negative.')