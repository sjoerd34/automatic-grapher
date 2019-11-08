import math
from decimal import Decimal, ROUND_UP, ROUND_05UP, ROUND_HALF_UP
'''
from PIL import Image, ImageDraw
Im = Image.open('grafiek_papier-1.png')
CopyIm = Im.copy()
draw = ImageDraw.Draw(CopyIm)
draw.rectangle((20, 30, 60, 60), fill='red')
CopyIm.save('drawing.png')
'''

volume = [0.000, 1.000, 2.000, 3.000, 4.000, 5.000, 6.000, 7.000,
        8.000, 9.000, 10.000, 11.000, 11.1, 11.2, 11.3, 11.4, 11.5, 11.6,
        11.7, 11.8, 11.9, 12.0, 12.1, 12.2, 12.3,]

ph = [3.89, 4.13, 4.38, 4.57, 4.75, 4.90, 5.05, 5.21, 5.37,
        5.56, 5.83, 6.28, 6.36, 6.44, 6.55, 6.68, 6.87, 7.15, 7.98,
        9.60, 10.07, 10.32, 10.51, 10.65, 10.75,]

'''
ph_difference = max(ph) - min(ph)
for i in range(10,30):
    print(ph_difference/i)
'''


minutes = [5, 10, 20, 30, 60]
enzym_activity = [0.000463, 0.000717, 0.000616, 0.000654, 0.000679]

number = Decimal('0.00000212')


i = 0
for c in str(number):

    if c == '0':
        i += 1
    elif c == '.':
        continue
    else:
        break

#number.adjusted() gives the power the number is raised to, like scientific notation

#quantize takes a decimal value like 0.1 and then rounding up round the number up to to the nears 10th  place
#0.04 becomes 0.1, 0.06 becomes 0.1, 0.101 becomes 0.2 etc
#by multiplying times two and then dividing by two we can obtain values like 0.15 and 0.25 that would have otherwise
#been rounded to 0.2 and 0.3 respectively
#example: 0.14*2 = 0.28 round it up we get 0.3 devided by two gives us 0.15
def auto_scaler(ind_var, ticks):
    ''''this fucntion automatically creates scale and tick distance'''
    value_range = (max(ind_var) - min(ind_var))
    dist_per_tick = Decimal(value_range / ticks)
    exponent = dist_per_tick.adjusted()

    g = ((dist_per_tick*2).quantize(Decimal(str(10**(dist_per_tick.adjusted()))), rounding=ROUND_UP))/2
    if round((g / Decimal(10**exponent)), 1) == 2.5 or round((g/Decimal(10**exponent)), 1) == 7.5:
        b = g
    else:
        b = dist_per_tick.quantize(Decimal(str(10**(dist_per_tick.adjusted()))), rounding=ROUND_UP)

    lower_bound = b * (Decimal(min(ind_var)) // b)
    if Decimal(max(ind_var)) % b == 0:
	    upper_bound = max(ind_var)
    else: 
        upper_bound = b * (1 + Decimal(max(ind_var)) // b)
    
    print(lower_bound)
    print(upper_bound)
    print(b)

auto_scaler(minutes, 28)
