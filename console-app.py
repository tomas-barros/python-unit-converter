from unit_converter import *

print('VALID INPUTS: \nkm, cm, in, mt')
print('Select the from unit to convert:')
tmp_inp = input('>> ')

if (tmp_inp == 'km'):
    print('Nice, now type the unit to convert:')

tmp_inp2 = input('>> ')

if (tmp_inp2 == 'cm'):
    print('Nice, now, type a integer to convert:')
    unit_inp = int(input('>> '))
    print(f'The total is: {km_to_cms(unit_inp)}cm')
