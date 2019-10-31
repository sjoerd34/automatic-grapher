'''
from PIL import Image, ImageDraw
Im = Image.open('grafiek_papier-1.png')
CopyIm = Im.copy()
draw = ImageDraw.Draw(CopyIm)
draw.rectangle((20, 30, 60, 60), fill='red')
CopyIm.save('drawing.png')
'''

